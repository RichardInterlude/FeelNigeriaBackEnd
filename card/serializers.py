from rest_framework import serializers
from .models import CardApplication



class CardApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardApplication
        fields = '__all__'
        read_only_fields = ['status','created_at','updated_at']


class SubmitAccountSerializer(serializers.Serializer):
    account_number = serializers.CharField(max_length=20)
