from django import forms
from . models import Review


class ReviewForm(forms.ModelForm):
    """ Form to add/edit a review """
    # Credit Bunny The Compiler
    # https://blog.devgenius.io/lets-build-a-movie-review-django-app-47658f8e3751
    class Meta:
        model = Review
        fields = ["stars", "comment"]
