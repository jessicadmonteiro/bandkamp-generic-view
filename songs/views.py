from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from albums.models import Album
from .serializers import SongSerializer
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from drf_spectacular.utils import extend_schema

@extend_schema(tags = ["Song"])
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

    @extend_schema(
        operation_id = "song_get",
        description = "Song read route",
        summary = "Read song"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        operation_id = "song_post",
        description = "Route for song creation",
        summary = "Create song"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
