from django.urls import path, include

from . import views

urlpatterns = [
    path('details/<int:hotel_id>/', views.details, name='details'),
    path('create_review/<int:hotel_id>/', views.create_review, name='create_review')
]