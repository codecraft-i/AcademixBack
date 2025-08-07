from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["status"]
    ordering_fields = ["date"]