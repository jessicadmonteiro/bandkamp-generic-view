from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema

@extend_schema(tags = ["User"])
class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
            operation_id = "user_post",
            description = "Route for user creation",
            summary = "Create user"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

@extend_schema(tags = ["User"])
@extend_schema(methods = ["PUT"], exclude = True)
class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "pk"

    @extend_schema(
            operation_id = "user_get",
            description = "User retrive route",
            summary = "Retrive user"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
            operation_id = "user_patch",
            description = "Route to update user",
            summary = "Update user",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @extend_schema(
            operation_id = "user_delete",
            description = "Route to delete user",
            summary = "Delete user",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    