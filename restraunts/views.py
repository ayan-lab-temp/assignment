from django.shortcuts import render
from .models import Restaurant, MenuItem
from .serializers import RestaurantSerializer, MenuItemSerializer
from rest_framework import views
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404 

# Create your views here.



class restaurant_list(views.APIView):
    
    def get(self, request):
        restuarent = Restaurant.objects.all().prefetch_related('menu_items')
        serializer = RestaurantSerializer(restuarent, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
        
        
class restaurant_detail(views.APIView):
    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant,pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
    
    
    
class menu_list(views.APIView):
    def get(self, request, pk):
        menu = MenuItem.objects.select_related('restaurant').filter(restaurant_id=pk)
        serializer = MenuItemSerializer(menu, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        data = request.data.copy()
        data['restaurant'] = pk
        serializer = MenuItemSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    
class menu_detail(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        restaurant_id = self.kwargs.get('restaurant_id')
        return MenuItem.objects.filter(restaurant_id=restaurant_id)
    
    def get_serializer_class(self):
        return MenuItemSerializer
    
    