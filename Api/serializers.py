from .models import *
from rest_framework import serializers

class Employee_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"

    def validate(self,data):
        phone=data.get('Phone_number')
        if(len(str(phone))<10):
            raise serializers.ValidationError("Phone number must be 10 digits")
        return data


class Role_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields="__all__"

class Login_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields="__all__"


class Patient_Name_id_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=["id","First_name","Middle_name","Last_name","Unique_Id"]

class AppointmentList_Serializer(serializers.ModelSerializer):
    Patient=Patient_Name_id_Serializer()
    Time=serializers.TimeField(format="%I:%M %p")
    class Meta:
        model=AppointmentList
        fields=["id","Patient","Date","Time","Condition",'Note']

class AppointmentHistory_Serializer(serializers.ModelSerializer):
    Time=serializers.TimeField(format="%I:%M %p")
    class Meta:
        model=AppointmentList
        fields=["Date","Time",'id','Note']

class Patient_Serializer(serializers.ModelSerializer):
    appointments=AppointmentHistory_Serializer(many=True)
    class Meta:
        model=Patient
        exclude=["created_at","updated_at","is_deleted"]
    
class Prescription_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Prescription
        fields="__all__"


class Pharmacy_stock_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Pharmacy_stock
        fields="__all__"


