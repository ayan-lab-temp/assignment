from django.shortcuts import render
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework import views
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



class restaurant_list(views.APIView):
    
    def get(self, request):
        restuarent = Restaurant.objects.all()
        serializer = RestaurantSerializer(restuarent, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        