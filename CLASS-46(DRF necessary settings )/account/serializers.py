from account.models import CustomUser
from rest_framework import serializers
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.urls import reverse

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'password',
            'bio',
            'image'
        ]
        extra_kwargs = {"password" : {"write_only" : True}}


    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.verification_token = get_random_string(length=32)
        user.save()
        self.send_email(user=user)
        return user
    
    def send_email(self, user):
        verification_link = self.context['request'].build_absolute_uri(
            reverse(
                viewname='verify_email',
                kwargs= {'token' : user.verification_token}
            )
        )

        subject = 'Verify your email'
        html_content = render_to_string('emails/verification_email.html', {
            "user": user.username,
            "verification_link": verification_link
        })
        # create an email message
        email = EmailMultiAlternatives(
            subject,
            "This is a plain text version of the email",
            "from@example.com",
            [user.email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)

        return True