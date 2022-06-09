from pyexpat import model
from rest_framework import serializers 
from .models import post, comment
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        mpdel = comment
        fields = '__all__'