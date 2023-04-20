from .models import Album
from .serializers import AlbumSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Album"])
class AlbumView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        operation_id = "album_get",
        description = "Album read route",
        summary = "Read Album"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        operation_id = "album_post",
        description = "Route for album creation",
        summary = "Create album"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)