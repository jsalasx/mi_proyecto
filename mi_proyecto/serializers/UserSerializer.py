from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    def getById(self, id):
        try:
            user = User.objects.filter(pk=id).first()   
        except User.DoesNotExist:
            return None
        return user
    def getByEmail(self, email):
        try:
            user = User.objects.filter(email=email).first()
        except User.DoesNotExist:
            return None
        return user
    def getByUsername(self, username):
        try:
           user = User.objects.filter(username=username).first()
        except User.DoesNotExist:
            return None
        return user
        
    class Meta:
        model = User
        fields = ['id', 'username','email','password']