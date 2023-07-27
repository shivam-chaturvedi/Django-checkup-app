"""checkup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from Api import views,LoginVerificationApi,TokenVerification
from Api import AppointmentListApi,PatientDetailApi

router=routers.DefaultRouter()
router.register('api/Patient/details',views.PatientAPI,basename='patient_details')
# router.register('api/appointment',AppointmentListApi,basename='appointments')
router.register('api/Prescription',views.PrescriptionAPI,basename='prescription')
router.register('api/Employee',views.EmployeeAPI,basename='employee')
router.register('api/Role',views.RoleAPI,basename='roles')
# router.register('api/Login',views.LoginAPI,basename='login')#not use this
router.register('api/Pharmacy_stock',views.Pharmacy_stockAPI,basename='pharmacy_stocks')

urlpatterns = [
    path('api/appointments',AppointmentListApi.list),
    path('api/appointment/pdf/<int:pk>',AppointmentListApi.generate_pdf),
    path('api/save/prescription/<int:pk>',AppointmentListApi.save_prescription),
    path('api/appointment/note/save/<int:pk>',AppointmentListApi.save_note),
    path('api/appointment/note/get/<int:pk>',AppointmentListApi.get_note),
    path('api/patient/<int:pk>',PatientDetailApi.get_patient),
    path('api/patients',PatientDetailApi.get_all_patients),
    path('api/patient/get_unique_id',PatientDetailApi.get_unique_id),
    path('api/token',TokenVerification.authenticate_token,name='token_verification'),
    path('api/login',LoginVerificationApi.Verify,name='login'),
    path('api/appointment/cancel',AppointmentListApi.cancel),
    path('api/login/forgotpassword',LoginVerificationApi.ForgotPassword,name='forgotpassword'),
    path('api/login/changepassword',LoginVerificationApi.ChangePassword,name='changepassword'),
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
