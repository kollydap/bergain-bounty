from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user_auth import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from django.views.static import serve

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/products/", include("product.urls", namespace="product")),
    path('api/v1/user_auth/', include("user_auth.urls", namespace="user_auth")),
    path("api/v1/order/", include("order.urls",namespace='order')),
    path('api/v1/category/', include("category.urls", namespace='category')),
    path('api-auth/', include('rest_framework.urls')),
    path("api/v1/cart/", include("cart.urls", namespace="cart")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password-reset/<str:encoded_pk>/<str:token>/',views.ResetPasswordAPI.as_view(), name='reset-password'),
    path('password-reset/',views.PasswordReset.as_view(),name='password-reset' ),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
