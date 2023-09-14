from django.shortcuts import render

# Create your views here.

def room_details(request):
    return render(request, 'hotel_pages/room_details.html')

def blog_details(request):
    return render(request, 'hotel_pages/blog_details.html')