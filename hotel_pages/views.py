from django.shortcuts import render, get_object_or_404
from .models import hotel


# Create your views here.

def room_details(request):
    return render(request, 'hotel_pages/room_details.html')

def blog_details(request):
    return render(request, 'hotel_pages/blog_details.html')

# def details(request, hotel_id):
#     hotels = hotel.objects.get(pk=hotel_id)
#     return render(request, 'details.html', {'Hotel': hotel})

def details(request, hotel_id):
    Hotel = get_object_or_404(hotel, pk=hotel_id)
    return render(request, 'hotel_pages/details.html', {'Hotel': Hotel})

