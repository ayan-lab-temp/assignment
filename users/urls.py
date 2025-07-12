from django.urls import include, path
from .views import UserList, UserDetail

urlpatterns =[
    path("users/", UserList.as_view()),
    path("users/<int:pk>", UserDetail.as_view()),
    
]