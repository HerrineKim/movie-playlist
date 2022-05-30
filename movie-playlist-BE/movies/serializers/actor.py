from rest_framework import serializers
from ..models import Movie, Actor

# 배우 목록 정보
class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

# 단일 배우 상세 정보
class ActorSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', 'poster_path',)

    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('name', 'profile_path', 'movies')