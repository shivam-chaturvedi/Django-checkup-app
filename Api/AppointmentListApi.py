from Api.models import AppointmentList
from django.http import JsonResponse,FileResponse
from django.views.decorators.csrf import csrf_exempt
from Api.serializers import AppointmentList_Serializer
from rest_framework import status
import io
from reportlab.pdfgen import canvas
from rest_framework.parsers import JSONParser

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
def generate_pdf(request):
    if(request.method=='GET'):
        try:
            buffer = io.BytesIO()
            # Create the PDF content
            p = canvas.Canvas(buffer)
            p.drawString(100, 750, "Hello, World!")

            # Save the PDF
            p.showPage()
            p.save()

            # Retrieve the value from BytesIO
            pdf_data = buffer.getvalue()
            buffer.close()

            # Create the FileResponse object with PDF data
            response = FileResponse(pdf_data, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
            return response
        except Exception as e:
            return JsonResponse()







        
