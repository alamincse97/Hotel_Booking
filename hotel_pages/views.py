from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def details(request, hotel_id):
    hotel_details = get_object_or_404(Hotel, pk=hotel_id)
    reviews = Review.objects.filter(hotel=hotel_details)
    return render(request, 'hotel_pages/details.html', {'Hotel': hotel_details, 'reviews': reviews})

@login_required
def create_review(request, hotel_id):
    hotelreview = get_object_or_404(Hotel, pk=hotel_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.hotel = hotelreview
            new_review.save()
            return redirect('details', hotel_id=hotelreview.id)
    else:
        form = ReviewForm()

    return render(request, 'hotel_pages/review.html', {'form': form, 'hotel': hotelreview})
