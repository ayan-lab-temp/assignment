
from django.contrib import admin
from django.urls import path
from django.urls import include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls') ),
    path('',include('restraunts.urls') ),
] + debug_toolbar_urls()
