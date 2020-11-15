from django.urls import path
from django.contrib.auth import views as auth_views
from . views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('create_user/', createUser_view, name='create_user'),
    path('login/', login_page, name='login'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_page, name='logout')
]