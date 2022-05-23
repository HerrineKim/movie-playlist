from django.shortcuts import get_list_or_404, get_object_or_404

from .serializers.actor import ActorListSerializer, ActorSerializer
from .serializers.movie import MovieSerializer, MovieListSerializer, UserLikeMovieListSerializer, UserChoiceSimilarMovieSerializer
from accounts.serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Actor, Movie
from accounts.models import User

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


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
    movie = get_object_or_404(Movie, pk=movie_pk)
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
        listofMovies = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
        idx_collection.extend(listofMovies)
 
    # 인덱스를 pk로 바꾸기
    pk_collection = []
    for idx in idx_collection:
        pk_collection.append(movies.data[idx[0]]['pk'])

    return pk_collection