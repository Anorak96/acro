from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('register/', views.registerview, name='register'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('profile/<pk>', views.ProfileView.as_view(), name='profile'),
    path('profile/<pk>/edit', views.profileedit, name='edit_profile'),
    path('profile/<pk>/delete', views.UserDelete.as_view(), name='delete-user'),
    # path('change-password/', auth_views.PasswordChangeView.as_view(template_name='user/change-password.html'), name='change_password'),
]
