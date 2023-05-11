from django.db.models import Q
from django.utils import translation
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework import permissions
from news.models import News
from django.contrib.auth.models import User
from news.serializers import NewsSerializer, UserSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['branch', 'title']

    @action(methods=['POST'], detail=False)
    def news_date(self, request):
        if 'end' not in request.data:
            raise ValidationError({'error': 'end year is not specified'})

        if 'start' not in request.data:
            raise ValidationError({'error': 'start year is not specified'})

        result = News.objects.filter(Q(date__year=request.data['start']) and Q(date__year=request.data['end']))
        result = NewsSerializer(result, many=True)
        return Response(result.data)

    @action(detail=True)
    def news_text(self, request, pk=None):
        news = self.get_object()
        news = NewsSerializer(news)
        return Response(news.data['text'])

    @action(detail=False)
    def news_user(self, request):
        user = request.user
        result = News.objects.filter(owner=user)
        result = NewsSerializer(result, many=True)
        return Response(result.data)

    @action(detail=False)
    def news_branch(self, request):
        news = News.objects.all()
        branch = request.query_params.get('branch')
        if branch is not None:
            news = news.filter(branch=branch)
            news = NewsSerializer(news, many=True)
            return Response(news.data)
        raise ValidationError({'error': 'branch is not specified'})

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = News.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
