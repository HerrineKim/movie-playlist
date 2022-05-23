from django.shortcuts import get_list_or_404, get_object_or_404

from .serializers.actor import ActorListSerializer, ActorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Actor

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