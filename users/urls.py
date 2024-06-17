from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from .views import *
app_name = 'api'

# router = DefaultRouter()
# router.register(r'/', Home)
# router.register(r'staff-profile/', StaffViewSet)
# router.register(r'patient-profile/', PatientViewSet)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path("", include(router.urls)),
]