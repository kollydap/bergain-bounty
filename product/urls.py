from . import views
from django.urls import path

app_name = "product"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>", views.product_detail, name="product_detail"),
    path("seller/<int:user_id>", views.getsellerproduct, name="getuserproduct"),
]
