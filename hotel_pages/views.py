# from django.shortcuts import render, get_object_or_404, redirect
# from .models import hotel, Review
# from .forms import ReviewForm
# from django.contrib.auth.decorators import login_required
 


# # Create your views here.

# def details(request, hotel_id):
#     Hotel = get_object_or_404(hotel, pk=hotel_id)
#     # reviews = Review.objects.filter(Hotel=Hotel)
#     # rating = Review.objects.filter(Hotel=Hotel)
#     return render(request, 'hotel_pages/details.html', {'Hotel': Hotel})

# @login_required
# def create_review(request, hotel_id):
#     Hotel = get_object_or_404(hotel, pk=hotel_id)
 
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             newReview = form.save(commit=False)
#             newReview.user = request.user
#             newReview.Hotels = Hotel  
#             newReview.save()
#             return redirect('details', hotel_id=Hotel.id)
#     else:
#         form = ReviewForm()
 
#     return render(request, 'hotel_pages/review.html', {'form': form, 'Hotel': Hotel})

from django.shortcuts import render, get_object_or_404, redirect
from .models import hotel, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def details(request, hotel_id):
    hotel_details = get_object_or_404(hotel, pk=hotel_id)
    reviews = Review.objects.filter(hotel=hotel_details)
    return render(request, 'hotel_pages/details.html', {'hotel': hotel_details, 'reviews': reviews})

# def details(request, hotel_id):
#     hoteldetails = get_object_or_404(hotel, pk=hotel_id)
#     reviews = Review.objects.filter(hoteldetails=hotel)
#     return render(request, 'hotel_pages/details.html', {'hotel': hoteldetails, 'reviews': reviews})

@login_required
def create_review(request, hotel_id):
    hotelreview = get_object_or_404(hotel, pk=hotel_id)

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
