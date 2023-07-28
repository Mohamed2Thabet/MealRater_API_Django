from rest_framework import serializers 
from .models import Rating ,Meal

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','stars','user','meal')
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id','title','description')