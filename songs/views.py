from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from albums.models import Album
from .serializers import SongSerializer
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    lookup_url_kwarg = "pk"

    def get_queryset(self):
        songs = Song.objects.all()
        return songs.filter(album_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs["pk"])

        serializer.save(album=album)
