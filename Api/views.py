from django.shortcuts import render
from Api.models import *
from rest_framework.response import Response
from rest_framework import  viewsets
from Api.serializers import *
from rest_framework import status


#patients detail api
class PatientAPI(viewsets.ViewSet):
    def list(self,request):
            try:
                patients=Patient.get_all_objects()
                res=Patient_Serializer(patients,many=True)
                return Response(res.data,status=status.HTTP_200_OK)
            except Exception as e:
             err=str(e)
             return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
        
    def create(self,request):
        try:
            patient=Patient_Serializer(data=request.data)
            if(patient.is_valid(raise_exception=True)):
                patient.save()
                return Response({'success':'Data Saved!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self,request,pk=None):
        try:
            patient=Patient.get_object(id=pk)
            res=Patient_Serializer(patient)
            return Response(res.data,status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request,pk=None):
        try:
            patient=Patient.get_object(id=pk)
            res=Patient_Serializer(patient,data=request.data)
            if(res.is_valid(raise_exception=True)):
                res.save()
                return Response({'success':'Data Updated!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk=None):
        try:
            patient=Patient.get_object(id=pk)
            res=Patient_Serializer(patient,data=request.data,partial=True)
        
            if(res.is_valid(raise_exception=True)):
                res.save()
                return Response({'success':'Data Updated!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        try:
            patient=Patient.get_object(id=pk)
            patient.soft_delete()
            return Response({'success':'Data Removed!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)


#appointments api     
class AppointmentListAPI(viewsets.ViewSet):
    def list(self,req):
        try:
            appointments=AppointmentList.get_all_objects()
            Appointments=AppointmentList_Serializer(appointments,many=True)
            return Response(Appointments.data,status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def create(self,req):
        try:
            appointment=AppointmentList_Serializer(data=req.data)
            if(appointment.is_valid(raise_exception=True)):
                appointment.save()
                return Response({'':'Data saved!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'erro':err},status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,req,pk=None):
        try:
            appointment=AppointmentList.get_object(id=pk)
            appointment_data=AppointmentList_Serializer(appointment)
            return Response(appointment_data.data,status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,req,pk=None):
        try:
            appointment=AppointmentList.get_object(id=pk)
            updated_appointment=AppointmentList_Serializer(appointment,data=req.data)
            if(updated_appointment.is_valid(raise_exception=True)):
                updated_appointment.save()
                return Response({'success':'Data Updated!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self,req,pk=None):
        try:
            appointment=AppointmentList.get_object(id=pk)
            updated_appointment=AppointmentList_Serializer(appointment,data=req.data,partial=True)
            if(updated_appointment.is_valid(raise_exception=True)):
                updated_appointment.save()
                return Response({'success':'Data Updated!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,req,pk=None):
        try:
            appointment=AppointmentList.get_object(id=pk)
            appointment.soft_delete()
            return Response({'success':'Data Removed!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
        

#prescription  api        
class PrescriptionAPI(viewsets.ViewSet):
    def list(self,req):
        try:
            prescriptions=Prescription.get_all_objects()
            Prescriptions=Prescription_Serializer(prescriptions,many=True)
            return Response(Prescriptions.data,status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
        
    def create(self,req):
        try:
            prescription=Prescription_Serializer(data=req.data)
            if(prescription.is_valid(raise_exception=True)):
                prescription.save()
                return Response({'success':'Prescription Saved!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self,req,pk=None):
        try:
            prescription=Prescription.get_object(id=pk)
            Prescription=Prescription_Serializer(prescription)
            return Response(Prescription.data,status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def update(self,req,pk=None):
        try:
            prescription=Prescription.get_object(id=pk)
            updated_prescription=Prescription_Serializer(prescription,data=req.data)
            if(updated_prescription.is_valid(raise_exception=True)):
                updated_prescription.save()
                return Response({'success':'prescription updated successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self,req,pk=None):   
        try:
            prescription=Prescription.get_object(id=pk)
            updated_prescription=Prescription_Serializer(prescription,data=req.data,partial=True)
            if(updated_prescription.is_valid(raise_exception=True)):
                updated_prescription.save()
                return Response({'success':'prescription updated successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,req,pk=None):
        try:
            prescrption=Prescription.get_object(id=pk)
            prescrption.soft_delete()
            return Response({'success':'Prescription removed successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
        
#login credentials api
class LoginAPI(viewsets.ViewSet):

    def list(self,req):
        try:
            credentials=Login.get_all_objects()
            Credentials=Login_Serializer(credentials,many=True)
            return Response(Credentials.data,status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def create(self,req):
        try:
            credentials=Login_Serializer(data=req.data)
            if(credentials.is_valid(raise_exception=True)):
                credentials.save()
                return Response({'success':'Login credentials saved successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,req,pk=None):
        try:
            credentials=Login.get_object(id=pk)
            Credentials=Login_Serializer(credentials)
            return Response(Credentials.data,status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def update(self,req,pk=None):
        try:
            credentials=Login.get_object(id=pk)
            Credentials=Login_Serializer(credentials,data=req.data)
            if(Credentials.is_valid(raise_exception=True)):
                Credentials.save()
                return Response({'success':'Login credentials updated successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,req,pk=None):
        try:
            credentials=Login.get_object(id=pk)
            Credentials=Login_Serializer(credentials,data=req.data,partial=True)
            if(Credentials.is_valid(raise_exception=True)):
                Credentials.save()
                return Response({'success':'Login credentials updated successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,req,pk=None):
        try:
            credentials=Login.get_object(id=pk)
            username=str(credentials.Username)
            credentials.soft_delete()
            return Response({'success':f'{username} login credentials removed successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
        


#employee info api
class EmployeeAPI(viewsets.ViewSet):
    def list(self,req):
        try:
            employees=Employee.get_all_objects()
            Employees=Employee_Serializer(employees,many=True)
            return Response(Employees.data,status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def create(self,req):
        try:
            employees=Employee_Serializer(data=req.data)
            if(employees.is_valid(raise_exception=True)):
                employees.save()
                return Response({'success':'Employees data saved successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,req,pk=None):
        try:
            employees=Employee.get_object(id=pk)
            Employees=Employee_Serializer(employees)
            return Response(Employees.data,status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def update(self,req,pk=None):
        try:
            employees=Employee.get_object(id=pk)
            Employees=Employee_Serializer(employees,data=req.data)
            if(Employees.is_valid(raise_exception=True)):
                Employees.save()
                return Response({'success':'Employees data updated successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,req,pk=None):
        try:
            employees=Employee.get_object(id=pk)
            Employees=Employee_Serializer(employees,data=req.data,partial=True)
            if(Employees.is_valid(raise_exception=True)):
                Employees.save()
                return Response({'success':'Employee data updated successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,req,pk=None):
        try:
            employees=Employee.get_object(id=pk)
            username=str(employees.First_name)
            employees.soft_delete()
            return Response({'success':f'{username} Employee removed successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
        
#roles api
class RoleAPI(viewsets.ViewSet):
    
    def list(self,req):
        try:
            roles=Role.get_all_objects()
            Roles=Role_Serializer(roles,many=True)
            return Response(Roles.data,status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def create(self,req):
        try:
            roles=Role_Serializer(data=req.data)
            if(roles.is_valid(raise_exception=True)):
                roles.save()
                return Response({'success':'Roles data saved successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,req,pk=None):
        try:
            roles=Role.get_object(id=pk)
            Roles=Role_Serializer(roles)
            return Response(Roles.data,status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def update(self,req,pk=None):
        try:
            roles=Role.get_object(id=pk)
            Roles=Role_Serializer(roles,data=req.data)
            if(Roles.is_valid(raise_exception=True)):
                Roles.save()
                return Response({'success':'Roles data updated successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,req,pk=None):
        try:
            roles=Role.get_object(id=pk)
            Roles=Role_Serializer(roles,data=req.data,partial=True)
            if(Roles.is_valid(raise_exception=True)):
                Roles.save()
                return Response({'success':'Role data updated successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,req,pk=None):
        try:
            roles=Role.get_object(id=pk)
            role=str(roles.role)
            roles.soft_delete()
            return Response({'success':f'{role} Role removed successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)


#pharmacy stock api
class Pharmacy_stockAPI(viewsets.ViewSet):
    
    def list(self,req):
        try:
            stock=Pharmacy_stock.get_all_objects()
            Stocks=Pharmacy_stock_Serializer(stock,many=True)
            return Response(Stocks.data,status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def create(self,req):
        try:
            stock=Pharmacy_stock_Serializer(data=req.data)
            if(stock.is_valid(raise_exception=True)):
                stock.save()
                return Response({'success':'Stocks data saved successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,req,pk=None):
        try:
            stock=Pharmacy_stock.get_object(id=pk)
            Stocks=Pharmacy_stock_Serializer(stock)
            return Response(Stocks.data,status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def update(self,req,pk=None):
        try:
            stock=Pharmacy_stock.get_object(id=pk)
            Stocks=Pharmacy_stock_Serializer(stock,data=req.data)
            if(Stocks.is_valid(raise_exception=True)):
                Stocks.save()
                return Response({'success':'Stocks data updated successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,req,pk=None):
        try:
            stock=Pharmacy_stock.get_object(id=pk)
            Stocks=Pharmacy_stock_Serializer(stock,data=req.data,partial=True)
            if(Stocks.is_valid(raise_exception=True)):
                Stocks.save()
                return Response({'success':'Pharmacy_stock data updated successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,req,pk=None):
        try:
            stock=Pharmacy_stock.get_object(id=pk)
            medicine=str(stock.Medicine)
            stock.soft_delete()
            return Response({'success':f'{medicine} Pharmacy stock removed successfully!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return Response({'error':err},status=status.HTTP_400_BAD_REQUEST)

















        
        


            

    

