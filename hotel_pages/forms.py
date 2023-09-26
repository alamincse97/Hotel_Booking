# from django.forms import ModelForm
# from hotel_pages.models import Review

# class ReviewForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ModelForm, self).__init__(*args, **kwargs)
#         self.fields['review'].widget.attrs.update({'class': 'form-control'})
#         self.fields['rating'].widget.attrs.update({'class': 'form-control'})
    
#     class Meta:
#         model = Review
#         fields = ['review', 'rating']
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review']
        widgets = {
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'review': forms.Textarea(attrs={'class': 'form-control'}),
        }

        
