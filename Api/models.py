from collections.abc import Iterable
from typing import Iterable, Optional
from django.db import models
import sys,os
from django.contrib.auth.hashers import make_password

def hash_password(password):
    sys.path.append(os.path.abspath(os.path.dirname( os.path.join(__file__,'..'))))#this is for environment variable checkup.setting DJANGO_SETTINGS_MODULE error resolve
    return make_password(password)



class Base(models.Model):
    readonly_fields=['created_at','updated_at']
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_deleted=models.BooleanField(default=False,editable=False)

    def soft_delete(self):
         self.is_deleted=True
         self.save()

    def restore(self):
         self.is_deleted=False
         self.save()

    @classmethod
    def get_all_objects(cls,*args,**kwargs):
         return cls.objects.filter(*args,**kwargs,is_deleted=False)
    
    @classmethod
    def get_object(cls,*args,**kwargs):
         return cls.objects.get(*args,**kwargs,is_deleted=False)
         
    class Meta:
         abstract=True

class Employee(Base):
        First_name=models.CharField(max_length=100)
        Middle_name=models.CharField(max_length=100,blank=True)
        Last_name=models.CharField(max_length=100,blank=True)
        Date_of_joining=models.DateField()
        Department=models.CharField(max_length=100)
        Phone_number=models.PositiveBigIntegerField(unique=True)
        Email=models.EmailField(unique=True)

        def __str__(self) -> str:
            return self.First_name+" "+self.Middle_name+" "+self.Last_name

class Role(Base):
     role=models.CharField(max_length=100)
     def __str__(self) -> str:
          return self.role
    

class Login(Base):
    Username=models.CharField(max_length=200,unique=True)
    Password=models.CharField(max_length=200)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    isActive=models.BooleanField()
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    def __str__(self) -> str:
         return self.Username
    
    def save(self, *args,**kwargs):
         self.Password=hash_password(self.Password)
         return super().save(*args,**kwargs)
        

class Patient(Base):
    GENDER_CHOICES=[('male','Male'),('female','Female'),('other','Other')]
    Unique_Id=models.CharField(max_length=15,unique=True)
    First_name=models.CharField(max_length=100)
    Middle_name=models.CharField(max_length=100,blank=True)
    Last_name=models.CharField(max_length=100,blank=True)
    Date_Of_Birth=models.DateField()
    Gender=models.CharField(max_length=20,choices=GENDER_CHOICES)
    Phone=models.PositiveBigIntegerField(unique=True)
    Email=models.EmailField(max_length=200,unique=True)
    Address=models.CharField(max_length=500)
    Age=models.PositiveIntegerField()

    def __str__(self) -> str:
         return self.First_name+" "+self.Middle_name+" "+self.Last_name
    
    def soft_delete(self):
         self.is_deleted=True
         self.appointments.update(is_deleted=True)
         self.save()

    def restore(self):
         self.is_deleted=False
         self.appointments.update(is_deleted=False)
         self.save()


class AppointmentList(Base):
     TYPE_CHOICES=[('offline','Offline'),('online','Online')]
     SHIFT_CHOICES=[('morning','Morning'),('evening','Evening')]
     Patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="appointments")
     Date=models.DateField()
     Time=models.TimeField()
     Condition=models.CharField(max_length=200,default='No Condition Specified')
     Shift=models.CharField(max_length=20,choices=SHIFT_CHOICES)
     Appointment_type=models.CharField(max_length=20,choices=TYPE_CHOICES)
     Note=models.TextField(blank=True)

     def __str__(self) -> str:
         return self.Patient.First_name
    
     def soft_delete(self):
         self.is_deleted=True
         self.prescription_set.update(is_deleted=True)
         self.save()

     def restore(self):
          self.prescription_set.update(is_deleted=False)
          return super().restore()
     


class Prescription(Base):
    Appointment=models.ForeignKey(AppointmentList,on_delete=models.CASCADE)
    Prescribed_medicines=models.TextField(default="No Medicine Prescribed")

    def __str__(self) -> str:
         return self.Prescribed_medicines

class Pharmacy_stock(Base):
     Medicine=models.CharField(max_length=200)
     Quantity=models.PositiveIntegerField()
     Expiry_date=models.DateField()
     def __str__(self) -> str:
          return self.Medicine





