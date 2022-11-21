from rest_framework import generics, status
from account.models import CustomUser
from .serializers import RegistrationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


class UserRegister(APIView):
    # queryset = CustomUser.objects.all()
    # serializer_class = RegistrationSerializer
    
     def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data = serializer.data
            token = Token.objects.get(user=account).key
            data['token'] = token
            # print(data);
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





