from .models import *
from rest_framework import serializers

class Employee_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"

class Role_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields="__all__"

class Login_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields="__all__"

class Patient_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields="__all__"

class AppointmentList_Serializer(serializers.ModelSerializer):
    class Meta:
        model=AppointmentList
        fields="__all__"

class Prescription_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Prescription
        fields="__all__"


class Pharmacy_stock_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Pharmacy_stock
        fields="__all__"


