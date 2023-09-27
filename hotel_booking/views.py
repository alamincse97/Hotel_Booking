from django.shortcuts import render
from hotel_pages.models import Hotel

def home(request):
    searchItem = request.GET.get('searchItem')
    if searchItem:
        hotel = Hotel.objects.filter(Address__icontains=searchItem)
    else:
        hotel = Hotel.objects.all()
    return render(request, 'index.html', {'searchItem': searchItem, 'hotels': hotel})