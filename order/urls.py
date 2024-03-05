from django.urls import path
from . import views
app_name="order"
urlpatterns=[
    path("list_create_order/", views.OrderView.as_view(), name="list-create-order"),
    path("order_detail/", views.OrderDetailView.as_view(),name="order-detail"),

]