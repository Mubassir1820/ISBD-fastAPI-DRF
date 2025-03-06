from django.shortcuts import render
from rest_framework import generics, status
from .serializers import (
    UserSerializer
)
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.urls import reverse
from rest_framework import generics, status
from . serializers import UserSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

class UserSignUp(generics.CreateAPIView):
    serializer_class = UserSerializer

class VerifyEmail(generics.GenericAPIView):
    def get(self, request, token):
        user = CustomUser.objects.filter(verification_token=token).first()
        if user:
            if user.is_verified:
                return Response({
                    "details" : "Email already verified",
                }, status=status.HTTP_400_BAD_REQUEST)
            user.is_verified = True
            user.veirification_token = None
            user.save()
            return Response({
                "details" : "Invalid token",
            }, status=status.HTTP_400_BAD_REQUEST)
        

class ResebdVerificationEmail(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        given_email = request.data.get('email')
        if given_email:
            user = CustomUser.objects.filter(email=given_email).first()
            if not user:
                return Response({
                    "details": "User with this email doesnt exist",
                }, status=status.HTTP_400_BAD_REQUEST)
            user.veirification_token = get_random_string(length=32)
            user.save()
            # Prepare things for sending mail
            verification_link = request.build_absolute_uri(reverse(
                viewname='verify_email',
                kwargs = {'token' : user.veirification_token}
            ),
            )