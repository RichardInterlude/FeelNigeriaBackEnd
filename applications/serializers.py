from rest_framework import serializers
from . models import *


class Step1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['nationality','country_of_residence','date_of_birth','gender','phone','passport_photo']

class Step2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['passport_number','passport_expiration','visa_history','travel_history']

class Step3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['motivation','profession','hobbies']

class Step4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['instagram','tiktok','youtube','intro_video']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['is_submitted','submitted_at']