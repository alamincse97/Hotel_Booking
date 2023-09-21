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

def create_review(request, hotel_id):
    Hotel = get_object_or_404(hotel, pk=hotel_id)
    if request.method == 'GET':
        return render(request, 'hotel_pages/review.html', {'forms': ReviewForm(), 'Hotel': Hotel})
    
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.Hotel = Hotel
            newReview.save()
            return redirect('details', newReview.Hotel.id)
        except ValueError:
            return render(request, 'hotel_pages/review.html', {'form': ReviewForm(), 'Hotel': Hotel, 'error': 'Bad Data Given'})
    