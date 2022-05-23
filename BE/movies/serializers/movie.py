from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Movie, Genre, Actor

User = get_user_model()

# 유저 정보
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'nickname')

# 단일 영화 상세 정보
class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    genre = GenreSerializer(Genre, read_only=True)
    actor = ActorSerializer(Actor, read_only=True)
    like_movies = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        exclude = ('popularity', 'tagline', 'vote_average', 'vote_count', 'words')

