from rest_framework import serializers
from .models import MyUser, Driver
from django.contrib.auth import authenticate

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

# from django.contrib.auth.hashers import make_password

# class CreateMyUserSerializer(serializers.ModelSerializer):
#     profilePicture = serializers.ImageField(max_length=None, use_url=True, required=False)
#     class Meta:
#         model = MyUser
#         fields = ['username', 'email', 'password', 'phoneNumber', 'profilePicture']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }

#     def create(self, validated_data):
#         # Hash the password before saving
#         validated_data['password'] = make_password(validated_data['password'])

#         user = MyUser.objects.create_user(**validated_data)
#         return user
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        username1 = data.get('username')
        password1 = data.get('password')

        if not username1 or not password1:
            raise serializers.ValidationError("Both username and password are required.")
        
        user = MyUser.objects.get(username=username1, password=password1)

        if not user:
           raise serializers.ValidationError("Invalid username or password.")

        # user = authenticate(username=username1, password=password1)

        # if not user:
        #     raise serializers.ValidationError("Invalid username or password.")

        data['user'] = user
        return data
