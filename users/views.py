from django.shortcuts import render
from django.http import JsonResponse, FileResponse, HttpResponse, HttpResponseRedirect, HttpRequest
from django.views.generic import DetailView, View

# Create your views here.

class Home(View):
    def get(self, request):
        response = HttpResponse("Site is running") 
        return response
