from rest_framework import generics, status
from account.models import CustomUser
from .serializers import RegistrationSerializer


class UserRegister(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer


# class User(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = SnippetSerializer



