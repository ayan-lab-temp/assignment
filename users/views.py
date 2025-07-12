from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404 

from .models import User
from .serializers import UserSerializer

# Create your views here.
class UserList(generics.ListCreateAPIView):
    def get_queryset(self):
        return User.objects.all()
    
    def get_serializer_class(self):
        return UserSerializer
    
    
class UserDetail(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User,pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        user =  get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        user = get_object_or_404(User,pk=pk)
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)