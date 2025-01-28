from rest_framework import viewsets
from blog.models import  Blog, BlogRating, Comment, Like
from blog.serializer import BlogSerializer, BlogRatingSerializer, CommentSerializer, LikeSerializer
from blog.user_serilizer import UserSerializer, RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from blog.permission import IsOwnerOrReadOnly
from user.models import CustomUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

user = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication] 
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = [
        "email",
    ]
    search_fields = ["email"]
    ordering_fields = ["email"]


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    authentication_classes = [JWTAuthentication]


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_queryset(self):
        """
        Override the default queryset to filter blogs by the logged-in user for unsafe actions
        (POST, PUT, DELETE) while making all blogs visible to everyone for GET requests.
        """
        if self.request.user.is_authenticated:
            return Blog.objects.filter(user=self.request.user)  # Only show the logged-in user's blogs for editing/deleting
        return Blog.objects.all()  # Make all blogs visible to everyone for viewing (GET)

    def perform_create(self, serializer):
        """
        Override the default perform_create method to automatically associate
        the logged-in user with the created blog post.
        """
        serializer.save(user=self.request.user)

class BlogRatingViewSet(viewsets.ModelViewSet):
    queryset = BlogRating.objects.all()
    serializer_class = BlogRatingSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return BlogRating.objects.filter(user=self.request.user)  
        return BlogRating.objects.all() 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Comment.objects.filter(user=self.request.user)  
        return Comment.objects.all() 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [JWTAuthentication]

