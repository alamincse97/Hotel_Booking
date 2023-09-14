from django.urls import path, include
from . import views

urlpatterns = [
    path('rooms/', views.rooms, name='rooms'),
]