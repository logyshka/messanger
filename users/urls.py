from django.urls import path

from . import views

urlpatterns = [
    path('singin/', views.index),
]
