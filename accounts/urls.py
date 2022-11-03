from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from banking import admin

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    # Get user profile update form
    path('update_user', views.update_user, name='update_user'),
    path('apply_user_update', views.apply_user_update, name='apply_update')

]
