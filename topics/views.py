from django.shortcuts import render
from rest_framework import viewsets
from .models import Topic
from .serializers import TopicSerializer

from django.http import HttpResponse


class TopicView(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
