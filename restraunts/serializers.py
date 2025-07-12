from rest_framework import serializers
from .models import Restaurant, MenuItem


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'owner', 'name', 'city','state', 'zipcode']
        
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','name','price','restaurant']
        read_only_fields = ['id']
        
class MenuItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'restaurant']