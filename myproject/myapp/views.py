# Create your views here.
from rest_framework import viewsets
# from .models import Book
from .models import User, Profile
# from .serializers import BookSerializer
from .serializers import UserSerializer, ProfileSerializer

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


    
    