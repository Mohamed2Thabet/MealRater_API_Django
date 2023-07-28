from django.shortcuts import render
from rest_framework import viewsets
from .models import Rating,Meal
from .serializers import RatingSerializer,MealSerializer
# Create your views here.

class MealViewSet(viewsets.ModelViewSet):
    queryset =Meal.objects.all()
    serializer_class =MealSerializer
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer