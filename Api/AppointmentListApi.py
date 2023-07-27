from Api.models import AppointmentList,Prescription
from django.http import JsonResponse,FileResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Api.serializers import AppointmentList_Serializer
from rest_framework import status
import io
from reportlab.pdfgen import canvas
from rest_framework.parsers import JSONParser
from Api import pdfgen

@csrf_exempt
def list(req):
    if(req.method=='GET'):
        try:
            date=req.GET.get('date')
            appointments=AppointmentList.get_all_objects(Date=date)
            serailize=AppointmentList_Serializer(appointments,many=True)
            return JsonResponse({'success':serailize.data},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error':'please used GET method'},status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def cancel(req):
    if(req.method=='DELETE'):
        try:
            appointment_id=req.GET.get("id")
            appointment=AppointmentList.get_object(id=appointment_id)
            appointment.soft_delete()
            return JsonResponse({'success':'Appointment Cancelled'},status=status.HTTP_200_OK)
        except AppointmentList.DoesNotExist:
            return JsonResponse({'error':'Appointment not exist!'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error':'Please Use DELETE request!'},status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def save_note(req,pk=None):
    if(req.method=='PATCH'):
        try:
            body=req.body
            stream=io.BytesIO(body)
            data=JSONParser().parse(stream)
            note=data.get('note')
            appointment=AppointmentList.get_object(id=pk)
            appointment.Note=note
            appointment.save()
            return JsonResponse({'success':'Note Saved'},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error':'please,use PATCH method!'},status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def get_note(req,pk=None):
    if(req.method=='GET'):
        try:
            appointment=AppointmentList.objects.get(id=pk)
            note=appointment.Note
            return JsonResponse({'success':note},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error':'please,use GET method'},status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def save_prescription(req,pk):
    if(req.method=="POST"):
        try:
            data=JSONParser().parse(io.BytesIO(req.body))
            
            #to ensure updation of prescriptions
            try:
                prescription=Prescription.objects.get(Appointment__id=pk)
                prescription.Prescribed_medicines=data["prescription"]
                prescription.save()
            except Prescription.DoesNotExist:
                prescription=Prescription()
                prescription.Appointment=AppointmentList.objects.get(id=pk)
                prescription.Prescribed_medicines=data["prescription"]
                prescription.save()

            return JsonResponse({"success":"prescription saved!"},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"error":"please,use post method"},status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def generate_pdf(request,pk):
    if(request.method=='GET'):
        try:   
            appointment=AppointmentList.objects.get(id=pk)
            name=appointment.Patient.First_name
            date=str(appointment.Date)
            address=str(appointment.Patient.Address)
            dob=str(appointment.Patient.Date_Of_Birth)
            phone=str(appointment.Patient.Phone)
            doctor_name="Doctor's name"
            clinic_name="Supersize Health Clinic"
            clinic_addr="123 Main Street, Big City, Upstate 110101"
            clinic_phone="+91 4536453643"
            try:
                prescription=Prescription.objects.get(Appointment=appointment)
                prescription=str(prescription.Prescribed_medicines)
            except Prescription.DoesNotExist as e:
                prescription="[]"
            pdf=pdfgen.generate_pdf(name,date,address,dob,phone,doctor_name,clinic_name,clinic_addr,clinic_phone,prescription)
            # Retrieve the value from BytesIO
            pdf_data = pdf.getvalue()#to get the bytesio buffer data
            pdfgen.clean()#to close the buffer
            
            #to make a name of pdf with appointment date and time
            filename=f"application_{appointment.Date}_{appointment.Time}.pdf"

            # Create the FileResponse object with PDF data
            response = HttpResponse(pdf_data, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
        except Exception as e:
            return JsonResponse({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)







        
