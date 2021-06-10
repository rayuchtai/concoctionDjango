from rest_framework import generics
from .serializers import WorldSerializer
from .models import World

# Create your views here.

class WorldList(generics.ListCreateAPIView):
    queryset = World.objects.all().order_by('id')
    serializer_class = WorldSerializer

class WorldDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = World.objects.all().order_by('id')
    serializer_class = WorldSerializer
