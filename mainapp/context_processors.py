from basketapp.models import Basket


def basket(request):
    basket_list = []

    if request.user.is_authenticated:
        basket_list = Basket.get_items(user=request.user)

    return {
        'basket': basket_list
    }