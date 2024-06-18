from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from .views import *
app_name = 'api'

# router = DefaultRouter()
# router.register(r'experts/', ExpertViewSet)
# router.register(r'staff-profile/', StaffViewSet)
# router.register(r'patient-profile/', PatientViewSet)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path("patient/register/", CreatePatientView.as_view(), name="register_patient"),
    path("expert/register/", CreateExpertView.as_view(), name="register_expert"),
    path("experts/", ExpertViewSet.as_view(), name="experts"),
    path('expert/<int:pk>/', ExpertDetail.as_view(), name='expert_detail'),
    # path('api/', include(router.urls)),
]