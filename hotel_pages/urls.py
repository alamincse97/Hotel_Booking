from django.urls import path, include

from . import views

urlpatterns = [
    path('room_details/', views.room_details, name='room_details'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('details/<int:hotel_id>/', views.details, name='details'),
    path('create_review/<int:hotel_id>/', views.create_review, name='create_review'),
]