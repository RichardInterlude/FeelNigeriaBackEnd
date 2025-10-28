from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from django.shortcuts import get_object_or_404

from .models import Application
from .serializers import *
from rest_framework.permissions import IsAuthenticated



class Step1View(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = Step1Serializer(data=request.data)  
        try:
            if serializer.is_valid():
                application = serializer.save(user=request.user)  # create new application
                return Response({"id": application.id}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Step2View(APIView):
    def put(self, request, id):
        app = get_object_or_404(Application, id=id, user=request.user)
        serializer = Step2Serializer(app, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Step 2 saved"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Step3View(APIView):
    def put(self, request, id):
        app = get_object_or_404(Application, id=id, user=request.user)
        serializer = Step3Serializer(app, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Step 3 saved"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Step4View(APIView):
    def put(self, request, id):
        app = get_object_or_404(Application, id=id, user=request.user)
        serializer = Step4Serializer(app, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Step 4 saved"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BVNView(APIView):
    def put(self, request, id):
        try:
            # Get the user's application
            app = Application.objects.filter(id=id, user=request.user).first()
            if not app:
                return Response({'error': 'Application not found'}, status=status.HTTP_404_NOT_FOUND)

            # Check if user already has BVN
            if app.has_bvn:
                return Response({'message': 'You already have a BVN linked to your account'}, status=status.HTTP_400_BAD_REQUEST)

            # If user doesn’t have BVN, validate and save new BVN
            serializer = BVNSerializers(app, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                app.has_bvn = True
                app.save()
                return Response({'message': 'BVN added successfully'}, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReviewView(APIView):
    def get(self, request, id):
        app = get_object_or_404(Application, id=id, user=request.user)
        serializer = ReviewSerializer(app)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubmissionView(APIView):
    def put(self, request, id):
        app = get_object_or_404(Application, id=id, user=request.user)
        serializer = SubmissionSerializer(app, data={"is_submitted": True}, partial=True)
        if serializer.is_valid():
            serializer.save(submitted_at=now())
            return Response({"message": "Application submitted successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)