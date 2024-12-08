# myapp/serializers.py
from rest_framework import serializers
# from .models import Book
from .models import User, Profile


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nesting UserSerializer for easy serialization of related data

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'location']
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile

