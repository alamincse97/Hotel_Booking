from django.shortcuts import render, get_object_or_404, redirect
from .models import hotel, ReviewRating
from .forms import ReviewForm


# Create your views here.

def room_details(request):
    return render(request, 'hotel_pages/room_details.html')

def blog_details(request):
    return render(request, 'hotel_pages/blog_details.html')

def details(request, hotel_id):
    Hotel = get_object_or_404(hotel, pk=hotel_id)
    return render(request, 'hotel_pages/details.html', {'Hotel': Hotel})

def submit_review(request, hotel_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.hotel_id = hotel_id
                data.user_id = request.user.id
                data.save()
                return redirect(url)
