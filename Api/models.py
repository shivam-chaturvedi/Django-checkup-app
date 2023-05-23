from typing import Any
from django.db import models
from django.db.models.query import QuerySet


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
        Phone_number=models.PositiveBigIntegerField()
        Email=models.EmailField()

        def __str__(self) -> str:
            return self.First_name+" "+self.Middle_name+" "+self.Last_name

class Role(Base):
     role=models.CharField(max_length=100)
     def __str__(self) -> str:
          return self.role
    

class Login(Base):
    Username=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    isActive=models.BooleanField()
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    def __str__(self) -> str:
         return self.Username
        

class Patient(Base):
    Unique_Id=models.CharField(max_length=15,unique=True)
    First_name=models.CharField(max_length=100)
    Middle_name=models.CharField(max_length=100,blank=True)
    Last_name=models.CharField(max_length=100,blank=True)
    Date_Of_Birth=models.DateField()
    Gender=models.CharField(max_length=20)
    Phone=models.PositiveBigIntegerField()
    Email=models.EmailField(max_length=200)

    def __str__(self) -> str:
         return self.First_name+" "+self.Middle_name+" "+self.Last_name


class AppointmentList(Base):
    Patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Date=models.DateField()
    Time=models.TimeField()
    Condition=models.CharField(max_length=200,default='No Condition Specified')
    Shift=models.CharField(max_length=50)
    Appointment_type=models.CharField(max_length=20)
    def __str__(self) -> str:
         return self.Patient.First_name


class Prescription(Base):
    Patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Prescribed_medicine=models.CharField(max_length=500)
    def __str__(self) -> str:
         return self.Prescribed_medicine

class Pharmacy_stock(Base):
     Medicine=models.CharField(max_length=200)
     Quantity=models.PositiveIntegerField()
     Expiry_date=models.DateField()
     def __str__(self) -> str:
          return self.Medicine





