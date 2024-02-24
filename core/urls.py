from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/products", include("product.urls", namespace="product")),
    path("api-auth/", include("rest_framework.urls")),
]
