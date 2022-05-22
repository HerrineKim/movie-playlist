from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer
from movies.models import Movie

# Create your views here.

User = get_user_model()

@api_view(['GET'])
def profile(request, nickname):
    user = get_object_or_404(User, nickname=nickname)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)
