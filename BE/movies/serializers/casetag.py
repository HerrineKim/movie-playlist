from rest_framework import serializers
from ..models import Movie, CaseTag

# Case 태그 상세 정보
class CaseTagSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', 'poster_path', 'tagline',)

    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = CaseTag
        fields = '__all__'