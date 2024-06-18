from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework import viewsets, generics
from django.http import JsonResponse, FileResponse, HttpResponse, HttpResponseRedirect, HttpRequest
from django.views.generic import DetailView, View
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import *

# Create your views here.

class Home(View):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer # kind of data you need to accept to make a new user
    permission_classes = [AllowAny]
    
    def get(self, request):
        welcome_message = "Welcome to our homepage!"
        experts = Expert.objects.all().order_by('-date_joined')[:5]
        items = [{"name": e.user, "specialty": e.specialty} for e in experts]
        
        return JsonResponse({
            "message": welcome_message,
            "recent_experts": items
        })
        # response = HttpResponse("Site is running") 
        
        # return Response(response)

class ExpertViewSet(generics.ListAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
    permission_classes = [AllowAny]
    # def get(self, request):
    #     response = HttpResponse("Site is running") 
    #     serializer_class = ExpertSerializer

class ExpertDetail(generics.RetrieveAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
    permission_classes = [AllowAny]


class PatientViewSet(generics.CreateAPIView):
    queryset = Patient.objects.all()
    def get(self, request):
        response = HttpResponse("Site is running") 
        serializer_class = PatientSerializer

class PatientDetail(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    def get(self, request):
        response = HttpResponse("Site is running") 
        serializer_class = StaffSerializer

class CreateExpertView(generics.CreateAPIView):
    queryset = Expert.objects.all()
    # serializer_class = User
    serializer_class = ExpertSerializer # kind of data you need to accept to make a new user
    permission_classes = [AllowAny]
    


class CreatePatientView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    # serializer_class = User
    serializer_class = PatientSerializer # kind of data you need to accept to make a new user
    permission_classes = [AllowAny]
    


class ExpertProfileView(generics.ListCreateAPIView):
    serializer_class = ExpertSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Expert.objects.filter(user=user)

    # def perform_create(self, serializer):
    #     if serializer.is_valid():
    #         serializer.save(author=self.request.user)
    #     else:
    #         print(serializer.errors)

@api_view(['POST'])
@permission_classes([AllowAny])
def sign_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'message': 'Login successful'})
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_profile(request):
    user = request.user
    return JsonResponse({
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name
    })