from . import views
from django.urls import path

app_name = "cart"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create_cart_item, name="create_cart_item"),
    path("<int:pk>", views.get_user_cart, name="create_cart_item"),
    # path("cart_view/", views.CartView.as_view(), name="cart"),
    # path("cart_add/", views.CartAddView.as_view(), name="cart-add"),
    # path("cart_remove/",views.CartRemoveView.as_view(), name="cart-remove"),
]
