from rest_framework import serializers
import random
from django.contrib.auth.models import User
from .models import Expert, Patient, Staff

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'password']
        extra_kwargs = {"password": {"write_only": True}}
    
    def create(self, validated_data):
        email = validated_data['email']
        username = email[:3] + str(random.randint(1000, 9999))
        user = User(
            email=email,
            username=username
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     if 'password' in validated_data:
    #         instance.set_password(validated_data['password'])
    #     instance.save()
    #     return instance

class ExpertSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Expert
        fields = ["id", "name", "user","specialty"] #fields we want to serialize when accepting a new user
         # accept password only when creating user but not when returning info about the user

    # def create(self, validated_data):
    #     print(validated_data)
    #     user = Expert.objects.create_user(**validated_data)
    #     return user
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        expert = Expert.objects.create(user=user, **validated_data)
        return expert


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Patient
        fields = ["id", "name", "user"] #fields we want to serialize when accepting a new user

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        patient = Patient.objects.create(user=user, **validated_data)
        return patient
    # def update(self, instance, validated_data):
    #     user_data = validated_data.pop('user')
    #     user = instance.user

    #     instance.medical_record_number = validated_data.get('medical_record_number', instance.medical_record_number)
    #     instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
    #     instance.save()

    #     user.email = user_data.get('email', user.email)
    #     if 'password' in user_data:
    #         user.set_password(user_data['password'])
    #     user.save()

    #     return instance

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'