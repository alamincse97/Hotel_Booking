from django import forms
from .models import ReviewRating
from django.forms import ModelForm

class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs.update({'class': 'form-control'})
        self.fields['review'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['rating'].widget.attrs.update({'class': 'form-check-input'})
    
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
        
