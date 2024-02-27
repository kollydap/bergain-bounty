from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user_auth import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/products/", include("product.urls", namespace="product")),
    path('api/v1/user_auth/', include("user_auth.urls")),
    path("api/v1/cart/", include("cart.urls", namespace="cart")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api-auth/", include("rest_framework.urls")),
    path('password-reset/<str:encoded_pk>/<str:token>/',views.ResetPasswordAPI.as_view(), name='reset-password'),
    path('password-reset/',views.PasswordReset.as_view(),name='password-reset' ),
]
