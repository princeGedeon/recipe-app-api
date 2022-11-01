
from django.urls import path

from accounts.views import UserPasswordResetView,SendPasswordResetEmailView,UserProfileView,UserChangePasswordView,UserRegistrationView,UserLoginView

app_name = 'user'
urlpatterns = [
   path('register/',UserRegistrationView.as_view(),name='register'),
   path('login/',UserLoginView.as_view(),name="login"),
   path('profile/',UserProfileView.as_view(),name="profile"),
path('changepassword/',UserChangePasswordView.as_view(),name="changepassword"),
   path('send-reset-password-mail/',SendPasswordResetEmailView.as_view(),name="reset_password_email"),
   path('reset-password/<str:uid>/<str:token>/',UserPasswordResetView.as_view(),name="reset-password")
]