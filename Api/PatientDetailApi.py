from Api.models import Patient
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Api.serializers import Patient_Serializer
from rest_framework import status
from Api.models import AppointmentList
from datetime import datetime
import faker,random
from faker import Faker
import uuid


def generate_random_address():
    faker = Faker()

    # Generate a random street address
    street_address = faker.street_address()

    # Generate a random city name
    city = faker.city()

    # Generate a random state
    state = faker.state()

    # Generate a random ZIP code
    zip_code = faker.zipcode()

    # Generate a random country
    country = faker.country()

    # Combine address components into a single string separated by commas
    address = f"{street_address}, {city}, {state}, {zip_code}, {country}"

    return address


def generate_fake_data():
    f=faker.Faker()
    for i in range(10):
        p=Patient.get_object(id=random.randint(1,20))
        a=AppointmentList.objects.create(Patient=p,Date=str(datetime.now()).split(" ")[0],Time=f.date_time_between(start_date='-1d', end_date='now').strftime("%H:%M"),Condition="Fever",Shift="morning",Appointment_type="offline")
        a.save()


def generate_fake_data2():
    f=faker.Faker()
    for i in range(10):
        p=random.randrange(10**10,10**12)
        a=Patient.objects.create(Unique_Id=f.uuid4()[:6],First_name=f.name(),Date_Of_Birth=str(datetime.now()).split(" ")[0],Gender="Male",Phone=p,Email=f.email(),Address=generate_random_address(),Age=random.randint(10,50))
        a.save()

@csrf_exempt
def get_patient(req,pk=None):
    if(req.method=="GET"):
        try:
            patient=Patient.get_object(id=pk)
            serialize=Patient_Serializer(patient)
            return JsonResponse({'success':serialize.data},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error':'please ,use GET method'},status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def get_all_patients(req):
    if(req.method=='GET'):
        try:
            patients=Patient.get_all_objects()
            serialize=Patient_Serializer(patients,many=True)
            return JsonResponse({'success':serialize.data},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error':'please,use GET method'},status=status.HTTP_400_BAD_REQUEST)

def get_unique_id(req):
    if(req.method=='GET'):
        try:
            while(True):
                unique_id=str(uuid.uuid4())[:6]
                unique_id=unique_id.upper()
                queryset=Patient.objects.filter(is_deleted=False,Unique_Id=unique_id)
                if(queryset.exists()):
                    continue
                else:
                    break
            return JsonResponse({'success':unique_id},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error':'please,use GET method'},status=status.HTTP_400_BAD_REQUEST)




