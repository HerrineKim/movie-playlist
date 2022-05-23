from rest_framework import serializers
from ..models import Movie, MoodTag

# Mood 태그 상세 정보
class MoodTagSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', 'poster_path', 'tagline',)

    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = MoodTag
        fields = '__all__'