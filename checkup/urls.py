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

router=routers.DefaultRouter()
router.register('api/Patient/details',views.PatientAPI,basename='patient_details')
router.register('api/Appointment',views.AppointmentListAPI,basename='appointments')
router.register('api/Prescription',views.PrescriptionAPI,basename='prescription')
router.register('api/Employee',views.EmployeeAPI,basename='employee')
router.register('api/Role',views.RoleAPI,basename='roles')
# router.register('api/Login',views.LoginAPI,basename='login')#not use this
router.register('api/Pharmacy_stock',views.Pharmacy_stockAPI,basename='pharmacy_stocks')

urlpatterns = [
    path('api/token',TokenVerification.authenticate_token,name='token_verification'),
    path('api/login',LoginVerificationApi.Verify,name='login'),
    path('api/login/forgotpassword',LoginVerificationApi.ForgotPassword,name='forgotpassword'),
    path('api/login/changepassword',LoginVerificationApi.ChangePassword,name='changepassword'),
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
