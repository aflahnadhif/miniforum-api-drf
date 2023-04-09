from rest_framework import serializers
from django.contrib.auth.models import User

class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
        ]
        
class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            'password',
        ]

class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password_confirmation'
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
        }
        
    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({"password_confirmation": "password is not equal"})
        
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        
        user = User.objects.create_user(**validated_data)
        
        return user
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
        }
        