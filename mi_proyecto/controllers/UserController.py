from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.UserSerializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        error= []
        if (username != "" and username != None ):
            if (password != "" and password != None):
                if (email != "" and email != None):
                    user = serializer.getByEmail(email=email)
                    if (user):
                        error.append("Ya existe un usuario con ese email")     
                        return Response({"error": True, "errorMsg": error, "data": None},status=status.HTTP_400_BAD_REQUEST)
                    user = serializer.getByUsername(username=username)
                    if (user):
                        error.append("Ya existe un usuario con ese Nombre de Usuario")     
                        return Response({"error": True, "errorMsg": error, "data": None},status=status.HTTP_400_BAD_REQUEST)
                    
                    if (len(password) < 8):
                        error.append("La contraseña debe tener al menos 8 caracteres")     
                        return Response({"error": False, "errorMsg": error, "data": None},status=status.HTTP_400_BAD_REQUEST)
                    serializer.is_valid()
                    serializer.save()  
                    return Response({"error": True, "errorMsg": error, "data": serializer.data}, status=status.HTTP_201_CREATED)
                else:
                    error.append("El email no debe estar vacio")        
                    return Response({"error": True, "errorMsg": error, "data": None},status=status.HTTP_400_BAD_REQUEST)
            else:
                error.append("La contraseña no debe estar vacía")
                return Response({"error": True, "errorMsg": error, "data": None},status=status.HTTP_400_BAD_REQUEST)
        else:
            error.append["El usuario no debe estar vacio"]
            return Response({"error": True, "errorMsg": error, "data": None},status=status.HTTP_400_BAD_REQUEST)
class GetUser(APIView):
    def get(self,request):
        permission_classes = [IsAuthenticated]
        user = UserSerializer(request.user).data
        return Response({"error": False, "errorMsg": [], "data": user}, status=status.HTTP_200_OK)