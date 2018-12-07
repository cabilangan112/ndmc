from django.contrib.auth import login
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from django.views.generic.base import TemplateView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from .serializers import (
        UserSerializer, 
        UserAuthSerializer, 
        UserDetailSerializer,
        UserEditSerializer,
        ConfirmationSerializer,
        ChangepassSerializer
)

from .models import User, Confirmation
from django.conf import settings


class Home(TemplateView):
    template_name = 'home.html'

class GuestAPI(ViewSet):
    """Guest API"""
 
    def list(self, *args, **kwargs):
        """lists all users
        """
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=200)

    def create(self, *args, **kwargs):
        """creates a user"""
        serializer = UserSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)

    def login(self, *args, **kwargs):
        serializer = UserAuthSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        login(self.request, user)
        token, created = Token.objects.get_or_create(user=user)
        context = {
            'token':token.key,
            'log':user.last_login,
        }
        return Response(context,status=200)

    def get_hash(self, *args, **kwargs):
        """submits a user email to generate confirmation
        """
        serializer = ConfirmationSerializer(data=self.request.data)
        if serializer.is_valid():
            subject = settings.DEFAULT_SUBJECT_EMAIL
            from_email = settings.EMAIL_HOST_USER
            to_email = serializer.validated_data['email']
            url = serializer.save()
            # text_content = f"{self.request.get_host()}{url}"
            send_mail(subject, text_content, from_email, [to_email])
            return Response(status=200)
        return Response(status=400)


class UserAPI(ViewSet):
    """User API"""
    permission_classes = (IsAuthenticated,)
        
    def check_valid(self, *args, **kwargs):
        """returns status=200 if hashed link is valid
        """
        confirmation = Confirmation.objects.get(pk=self.kwargs['hash'])
        if confirmation and confirmation.user == self.request.user:
            return Response(status=200)
        return Response(status=404)

    def details(self, last_name, *args, **kwargs):
        """view details of a user
        """ 
        instance = User.objects.get(last_name=last_name)
        serializer = UserDetailSerializer(instance)
        return Response(serializer.data, status=200)

    def edit(self, *args, **kwargs):
        """Edit details of a user"""
        handle = self.request.user.lastname
        instance = User.objects.get(lastname=lastname)

        serializer = UserEditSerializer(
            data=self.request.data, 
            context={'request':self.request}
        )

        serializer.is_valid(raise_exception=True)
        serializer.save(handle=handle)

        return Response(serializer.data, status=200)

    def changepass(self, *args, **kwargs):
        """changes a user's password
        """
        confirmation = Confirmation.objects.get(pk=self.kwargs['hash'])
        if confirmation and confirmation.user == self.request.user:
            serializer = ChangepassSerializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save(self.request.user.id)
                return Response(status=200)
        return Response(status=400)