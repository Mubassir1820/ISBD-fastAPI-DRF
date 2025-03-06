from django.urls import path
from account.views import UserSignUp, VerifyEmail

urlpatterns = [
    path("signup/", UserSignUp.as_view(), name="signup"),
    path('verify-email/<str:token>/', VerifyEmail.as_view(), name='verify_email'),
]