from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Article
from .comment import CommentSerializer

User = get_user_model()


# 단일 게시글 정보
class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'nickname')

    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    like_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'content', 'comments', 'created_at', 'updated_at', 'like_users', 'like_count',)

# 게시글 목록
class ArticleListSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'nickname')
    user = UserSerializer(read_only=True)
    comment_count = serializers.IntegerField    # query annotate로 view에서 채워줄 것!
    like_count = serializers.IntegerField()
    class Meta:
        model = Article
        fields = ('pk', 'title', 'user', 'comment_count', 'like_count',)
