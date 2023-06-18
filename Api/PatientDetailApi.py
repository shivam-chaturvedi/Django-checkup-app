from Api.models import Patient
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Api.serializers import Patient_Serializer
from rest_framework import status

@csrf_exempt
def detail(req):
    if(req.method=="GET"):
        try:
            id=req.GET.get("id")
            patient=Patient.get_object(id=id)
            serialize=Patient_Serializer(patient)
            return JsonResponse({'success':serialize.data},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error':'please used GET method'},status=status.HTTP_400_BAD_REQUEST)

