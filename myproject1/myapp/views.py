from rest_framework import viewsets
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
 
    
    
# class ProfileViewSet(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 # Atomic transaction ensures both User and Profile are saved together
#                 with transaction.atomic():
#                     serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             except Exception as e:
#                 return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
