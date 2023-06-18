from Api.models import AppointmentList
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Api.serializers import AppointmentList_Serializer
from rest_framework import status

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





        
