from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_view, name='users-register'),
    path('login/', views.login_view, name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='users-logout'),
    path('profile/', views.profile, name='users-profile'),
]
