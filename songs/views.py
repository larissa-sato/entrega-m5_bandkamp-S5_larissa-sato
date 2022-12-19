from rest_framework import generics
from rest_framework.views import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics
import ipdb
from django.shortcuts import get_object_or_404


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer
    queryset = Song.objects.all()


    def get_queryset(self):
        songs = Song.objects.filter(album_id=self.kwargs['pk'])
        return songs
    
    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs['pk'])
        serializer.save(album=album)

