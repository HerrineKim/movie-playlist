from django.shortcuts import get_list_or_404, get_object_or_404

from .serializers.actor import ActorListSerializer, ActorSerializer
from .serializers.genre import GenreSerializer
from .serializers.moodtag import MoodTagSerializer
from .serializers.casetag import CaseTagSerializer
from .serializers.movie import MovieSerializer, MovieListSerializer, RatingSerializer, UserLikeMovieListSerializer, UserChoiceSimilarMovieSerializer, MovieSearchSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Actor, Movie, Genre, MoodTag, CaseTag, Rating
from accounts.models import User

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from jellyfish import jaro_winkler_similarity

# Create your views here.
@api_view(['GET'])
def actor_list(request):
    actors = get_list_or_404(Actor)
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)

@api_view(['GET'])
def moodtag_detail(request, moodtag_pk):
    moodtag = get_object_or_404(MoodTag, pk=moodtag_pk)
    serializer = MoodTagSerializer(moodtag)
    return Response(serializer.data)

@api_view(['GET'])
def casetag_detail(request, casetag_pk):
    casetag = get_object_or_404(CaseTag, pk=casetag_pk)
    serializer = CaseTagSerializer(casetag)
    return Response(serializer.data)

@api_view(['GET'])
def search_movie(request, movie_name):
    movies = get_list_or_404(Movie)
    serializer = MovieSearchSerializer(movies, many=True)
    serializer = serach(serializer.data, movie_name)
    return Response(serializer[:6])

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializr = MovieSerializer(movie)
    return Response(serializr.data)

@api_view(['POST'])
def like_movie(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
def create_rating(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    rating = movie.ratings.filter(user=user).first()
    serializer = RatingSerializer(data=request.data)
    if not rating:
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)

            ratings = movie.ratings.all()
            serializer = RatingSerializer(ratings, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # 이미 평점을 등록했다면 평점 수정해버리기 - 한 사람이 한 영화에 대해 여러 평점 x
    else:
        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def rating_update_or_delete(request, movie_pk, rating_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    rating = get_object_or_404(Rating, pk=rating_pk)

    def update_rating():
        if request.user == rating.user:
            serializer = RatingSerializer(instance=rating, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                ratings = movie.ratings.all()
                serializer = RatingSerializer(ratings, many=True)
                return Response(serializer.data)

    def delete_rating():
        if request.user == rating.user:
            rating.delete()
            ratings = movie.ratings.all()
            serializer = RatingSerializer(ratings, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_rating()
    elif request.method == 'DELETE':
        return delete_rating()

@api_view(['GET'])
def user_like_movie(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserLikeMovieListSerializer(user)
    movies = get_list_or_404(Movie)
    movies_serializer = MovieListSerializer(movies, many=True)
    
    # user가 좋아요한 영화 key값 담기
    movie_key = [data['pk'] for data in serializer.data.get('like_movies')]

    # user가 좋아요 한 영화 index 담기
    idx = []
    for key in movie_key:
        for i in range(len(movies_serializer.data)):
            if key == movies_serializer.data[i]['pk']:
                idx.append(i)
                break
    # words 담기
    xMovie = [data.get('words') for data in movies_serializer.data]

    # 유사 영화 pk 반환
    result = recommend_movies_names(xMovie, idx, movies_serializer)

    # 유사 영화 pk 기반 querySet 생성
    final_movie = [get_object_or_404(Movie, pk=i) for i in result]
    final_serializer = UserChoiceSimilarMovieSerializer(final_movie, many=True)

    return Response(final_serializer.data)

@api_view(['GET'])
def similar_movie(request, movie_pk):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    
    idx = []
    for i in range(len(serializer.data)):
        if movie_pk == serializer.data[i]['pk']:
            idx.append(i)
            break

    xMovie = [data.get('words') for data in serializer.data]
    result = recommend_movies_names(xMovie, idx, serializer)
    final_movie = [get_object_or_404(Movie, pk=i) for i in result]
    final_serializer = UserChoiceSimilarMovieSerializer(final_movie, many=True)
    
    return Response(final_serializer.data)


# 추천 알고리즘
def recommend_movies_names(xMovie, idx, movies):
    
    # 불용어 제거
    countVec = CountVectorizer(max_features=10000, stop_words='english')

    # 영화 키워드 벡터라이징
    dataVectors = countVec.fit_transform(xMovie).toarray()

    # 코사인 유사도
    similarity = cosine_similarity(dataVectors)
    
    # 유사도 내림차순 5개 영화의 인덱스
    idx_collection = []
    for i in idx:
        distances = similarity[i]
        listofMovies = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:7]
        idx_collection.extend(listofMovies)
 
    # 인덱스를 pk로 바꾸기
    pk_collection = []
    for idx in idx_collection:
        pk_collection.append(movies.data[idx[0]]['pk'])

    return pk_collection

# 편집거리 알고리즘
def serach(lst, keyword):
    fetch_data = []
    for data in lst:
        tmp = {'pk': 0, 'title': '', 'poster_path':'', 'similarity':''}
        tmp['pk'] = data['pk']; tmp['title'] = data['title']; tmp['poster_path'] = data['poster_path']
        tmp['similarity'] = jaro_winkler_similarity(keyword, data['title'])
        fetch_data.append(tmp)
    fetch_data.sort(key=lambda x : -x['similarity'])
    return fetch_data