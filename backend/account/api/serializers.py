from rest_framework import serializers
from account.models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'phone_number', 'first_name', 'last_name', 'password', 'password2')
        extra_kwargs = { 'password': {'write_only': True}}
        
    def save(self):
        user = CustomUser(
            email = self.validated_data['email'],
            phone_number = self.validated_data['phone_number'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match!'})
        user.set_password(password)
        user.save()
        
        return user
        