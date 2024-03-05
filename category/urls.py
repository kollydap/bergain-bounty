from django.urls import path
from . import views

app_name="category"
urlpatterns=[
    path("category_view/", views.CategoryView.as_view(), name="category-view"),
]