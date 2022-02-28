from django.contrib import admin
from django.urls import URLPattern, path, include
from . import views

urlpatterns = [
    path('email/', views.emailview),
]