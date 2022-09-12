from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_wishlist(request):
    """ A view that renders the wishlist contents page """

    return render(request, 'wishlist/wishlist.html')


# Based on Very Acadmey's Youtube Video
# https://www.youtube.com/watch?v=OgA0TTKAtqQ
def add_to_wishlist(request, item_id):
    """ Add a quantity of the specified product to the wishlist """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if request.user.is_authenticated:
        if request.POST:
            if product.user_wishlist.filter(id=request.user.id).exists():
                product.user_wishlist.remove(request.user)
                wishlist.pop(item_id)
                messages.success(
                    request,
                    f'{product.name} has been removed from your wishlist'
                )
            else:
                product.user_wishlist.add(request.user)
                messages.success(
                    request, f'{product.name} has been added to your wishlist'
                    )
                wishlist[item_id] = product.name

        request.session['wishlist'] = wishlist

        return redirect(redirect_url)
    else:
        messages.error(
            request,
            'You must be logged in to add an item to your wishlist'
        )
        return redirect(redirect_url)


def remove_from_wishlist(request, item_id):
    '''
    Removes the item from the users wishlist
    '''
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    product = get_object_or_404(Product, pk=item_id)
    wishlist.pop(item_id)
    product.user_wishlist.remove(request.user)
    messages.success(request, f'{ product.name } has been removed from your wishlist')

    request.session['wishlist'] = wishlist

    return redirect(redirect_url)
