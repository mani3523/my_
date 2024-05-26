from django.urls import path
from user import views
from django.contrib.auth import views as auth_views
# from .views import ResetPasswordView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
#     path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
#     path('password-reset-confirm/<uidb64>/<token>/',
#          auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
#          name='password_reset_confirm'),
#     path('password-reset-complete/',
#          auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
#          name='password_reset_complete'),
]
