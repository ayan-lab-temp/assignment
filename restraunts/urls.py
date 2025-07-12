from . import views
from django.urls import include, path

urlpatterns =[
    path("restaurents/", views.restaurant_list.as_view())
]