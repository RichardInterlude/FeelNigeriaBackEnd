from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . models import *
from . serializers import *
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import get_object_or_404


class RegistrationView(APIView):
    def post(self,request):
        try:
            serializers = RegistrationSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_200_OK)
            return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)})
    def put(self,request,id):
        try:
            profile = get_object_or_404(Profile, id=id)
            serializers = RegistrationSerializer(profile,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.dat,status=status.HTTP_202_ACCEPTED)
            return Response(serializers.error,status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginView(APIView):
    def post(self,request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)            
            if user is not None:
                login(request,user)
                return Response({'message':'user logged in successfully'}, status=status.HTTP_200_OK)
            return Response({'message':'username/password seems to be incorrect'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)     
        
class LogoutView(APIView):
    def post(self,request):
        try:
            logout(request)
            return Response({'message':"Logout was successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    



