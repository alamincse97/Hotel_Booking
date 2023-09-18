from django.shortcuts import render
from hotel_pages.models import hotel

def home(request):
    searchItem = request.GET.get('searchItem')
    if searchItem:
        Hotel = hotel.objects.filter(Name__icontains=searchItem)
    else:
        Hotel = hotel.objects.all()
    return render(request, 'index.html', {'searchItem': searchItem, 'Hotels': Hotel})