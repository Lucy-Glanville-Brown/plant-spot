from django.shortcuts import render, redirect
from . models import Review
from . forms import ReviewForm
from products.models import Product


def reviews(request, id):
    post = Product.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        user_profile = request.POST.get('user_profile')
        stars = request.POST.get('stars')
        comment = request.POST.get('comment')
        review = Review(user_profile=user_profile, stars=stars, comment=comment, product=post)
        review.save()
        return redirect('success')

    form = ReviewForm()
    context = {
        "form": form

    }
    return render(request, 'review/review.html', context)
