from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Movie, Genre, Actor, Rating

User = get_user_model()

# 유저 정보
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'nickname')

# 사용자가 좋아요 누른 영화
class UserLikeMovieListSerializer(serializers.ModelSerializer):
    
    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('pk', 'words',)
 
    like_movies = MovieSerializer(many=True)
    
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'like_movies',)


# 검색한 영화와 비슷한 영화
class MovieSearchSerializer(serializers.ModelSerializer):

    similarity = serializers.FloatField(default=0)

    class Meta:
        model = Movie
        fields = ('pk', 'words', 'title', 'poster_path', 'similarity',)


# 여러 영화 제공
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'words',)


# 사용자가 선택 또는 좋아요 한 영화와 비슷한 영화
class UserChoiceSimilarMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'poster_path', 'pk')

# 평점
class RatingSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields =('pk', 'username',)

    user = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields= '__all__'
        read_only_fields = ('movie',)

# 단일 영화 상세 정보
class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    genres = GenreSerializer(read_only=True, many=True)
    actors = ActorSerializer(read_only=True, many=True)
    like_movies = UserSerializer(read_only=True, many=True)
    ratings = RatingSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ('popularity', 'tagline', 'vote_average', 'vote_count', 'words',)

