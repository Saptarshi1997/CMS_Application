from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

class PostSerializer(serializers.ModelSerializer):
    num_likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'industry', 'created_at','updated_at', 'is_public', 'owner', 'num_likes')
        read_only_fields = ('owner',)

    def get_num_likes(self, obj):
        return obj.like_set.count()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
