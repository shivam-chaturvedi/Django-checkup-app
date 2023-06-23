# from typing import Optional
from django.contrib import admin
from Api.models import *


class Admin_Actions(admin.ModelAdmin):
    actions=['soft_del','restore']    
    
    @admin.action(description="Soft Delete Selected Elements")
    def soft_del(self,req,queryset):
        for obj in queryset:
            obj.soft_delete()

    @admin.action(description="Restore Selected Elements")
    def restore(self,req,queryset):
        for obj in queryset:
            obj.restore()


@admin.register(Employee)
class Admin_Employee(Admin_Actions):
    ordering=['id']
    list_display=["id",'created_at','updated_at','is_deleted',"First_name","Middle_name","Last_name","Date_of_joining","Department","Phone_number","Email"]


@admin.register(Role)
class Admin_Role(Admin_Actions):
    ordering=['id']
    list_display=["id",'created_at','updated_at','is_deleted',"role"]

@admin.register(Login)
class Admin_Login(Admin_Actions):
    ordering=["id"]
    list_display=[field.name for field in Login._meta.get_fields()]

@admin.register(Patient)
class Admin_Patient(Admin_Actions):
    ordering=["id"]
    list_display=['id','created_at','updated_at','is_deleted','Unique_Id','First_name',"Middle_name","Last_name",'Date_Of_Birth','Gender','Phone','Email','Address','Age']
    #list_display=[field.name for field in Patient._meta.get_fields()]
    

@admin.register(AppointmentList)
class Admin_AppointmentList(Admin_Actions):
    ordering=["id"]
    list_display=['id','created_at','updated_at','is_deleted','Patient','Date','Time','Condition','Shift',"Appointment_type",'Note']   

@admin.register(Prescription)
class Admin_Prescription(Admin_Actions):
    ordering=["id"]
    list_display=[field.name for field in Prescription._meta.get_fields()]

@admin.register(Pharmacy_stock)
class Admin_Pharmacy_stock(Admin_Actions):
    ordering=['id']
    list_display=[field.name for field in Pharmacy_stock._meta.get_fields()]














