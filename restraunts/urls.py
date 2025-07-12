from .views import menu_list, restaurant_list, restaurant_detail, menu_detail
from django.urls import include, path

urlpatterns =[
    path("restaurent/", restaurant_list.as_view()),
    path("restaurent/<int:pk>", restaurant_detail.as_view()),
    path("restaurent/<int:pk>/menu/",menu_list.as_view() ),
    path("restaurent/<int:restaurant_id>/menu/<int:pk>/", menu_detail.as_view())
]