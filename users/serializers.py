from rest_framework import serializers
from .models import Expert, Patient, Staff

class HealthExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'