from django.urls import path
from . import views

app_name="user_auth"
urlpatterns=[
    path('signup/',views.signup, name='signup'),
    path('login/', views.login,name='login'),
    path('logout/', views.log_out, name='log-out'),
    path('user_list/<str:username>/', views.list_user, name="list-user"),

]