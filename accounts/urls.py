from django.contrib.auth import views as auth_views
from django.urls import path
from .views import MyPassword
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('change-password/', MyPassword.as_view(), name='change-password'),
    # Get user profile update form
    path('update_user', views.update_user, name='update_user'),
    path('apply_user_update', views.apply_user_update, name='apply_update')

]
