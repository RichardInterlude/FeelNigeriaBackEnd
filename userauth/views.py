from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from django.conf.global_settings import SECRET_KEY
from django.contrib.auth import login,logout,authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404
from django.urls import reverse
import  jwt

from . models import *
from . serializers import *
from .serializers import RegistrationSerializer
from .utils import sendMail



class RegistrationView(APIView):
    def post(self, request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                # Save the user
                user = serializer.save()

                # Generate token for email verification
                token = RefreshToken.for_user(user).access_token

                # Build activation URL
                current_site = get_current_site(request).domain
                relative_link = reverse('verify')  # <- make sure you have a urlpattern named 'verify'
                abs_url = f"http://{current_site}{relative_link}?token={str(token)}"

                # Send activation email
                sendMail(
                    to_email=user.email,
                    username=user.username,
                    activation_link=abs_url
                )

                return Response(
                    {"message": "Registration successful. Please check your email to verify your account."},
                    status=status.HTTP_201_CREATED
                )

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

class VerifyRegistrationView(generics.GenericAPIView):
    def get(self,request):
        token = request.GET.get('token')
        try:
            access_token = AccessToken(token)
            user_id = access_token['user_id']

            user = get_object_or_404(User,id=user_id)

            profile = get_object_or_404(Profile,user=user)

            if not profile.is_verified:
                profile.is_verified = True
                profile.save()
            return Response({"Message":"Email Verification successful"}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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


