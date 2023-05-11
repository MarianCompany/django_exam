from rest_framework import serializers
from news.models import News
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    news = serializers.PrimaryKeyRelatedField(many=True, queryset=News.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'news']


class NewsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = News
        fields = ['title', 'text', 'date', 'branch', 'owner']
