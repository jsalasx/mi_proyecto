from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.UserSerializer import UserSerializer

class LoginView(APIView):
    def post(self, request):
        password = request.data.get('password')
        email = request.data.get('email')
        user = UserSerializer.getByEmail(self, email=email)
        errorMsg = []
        if (user):
            user = authenticate(username=user.username, password=password)  
            if (user):
                return Response({"error": False, "errorMsg": errorMsg, "data": UserSerializer(user).data}, status=status.HTTP_200_OK)
            else:
                errorMsg.append("Contraseña incorrecta")
                return Response({"error": True, "errorMsg": errorMsg, "data": None},status=status.HTTP_400_BAD_REQUEST) 
        else:   
            errorMsg.append("No existe un usuario registrado con el correo: " + email)

            return Response({"error": True, "errorMsg": errorMsg, "data": None},status=status.HTTP_400_BAD_REQUEST) 