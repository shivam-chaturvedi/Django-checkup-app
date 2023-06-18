from django.http import JsonResponse
from rest_framework import status
from Api.models import Login
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import check_password
from Api.TokenVerification import generate_access_token,generate_refresh_token    





@csrf_exempt
def Verify(request):
    if(request.method=='POST'):
        # print(request.body)
        # print(request.data)
        try:
            stream=io.BytesIO(request.body)
            data=JSONParser().parse(stream=stream)
            email=data['email']
            password=data['password']

            login=Login.get_object(employee_id__Email=email)
            Password=login.Password
            if(check_password(str(password),str(Password))):
                access_token = generate_access_token(login)
                refresh_token = generate_refresh_token(login)
                return JsonResponse(
                    {
                        'access_token': access_token,
                        'refresh_token': refresh_token,
                        'message': 'Login Successful!',
                    },
                    status=status.HTTP_200_OK
                )
                
            else:
                return JsonResponse({'error':'Wrong Password!'},status=status.HTTP_401_UNAUTHORIZED)
        except Login.DoesNotExist:
            return JsonResponse({'error':'Email not exist!'},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return JsonResponse({'error': str(e)},status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'error':'Please use POST method for login verification!'},status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def ForgotPassword(request):
    if(request.method=='POST'):
        # print(request.body)
        try:
            email=JSONParser().parse(io.BytesIO(request.body))['email']
            global EMAIL
            EMAIL=email
        
            login=Login.get_object(employee_id__Email=email)
            return JsonResponse({'message':'Email Exist!'},status=status.HTTP_200_OK)
        except Login.DoesNotExist:
            return JsonResponse({'error':'Email Not Exist!'},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return JsonResponse({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'error':'Please use POST method for this!'},status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def ChangePassword(request):
    if(request.method=='PATCH'):
        try:
            stream=io.BytesIO(request.body)
            data=JSONParser().parse(stream)
            if(len(data)==1):
                if 'email' not in data:
                    email=EMAIL
            else:
                email=JSONParser().parse(io.BytesIO(request.body))['email']
            new_password=JSONParser().parse(io.BytesIO(request.body))['password']
            # data={'Password':new_password}
        
            login=Login.get_object(employee_id__Email=email)
            login.Password=new_password
            login.save()
            return JsonResponse({'message':'Password Updated!'},status=status.HTTP_200_OK)
        except Exception as e:
            err=str(e)
            return JsonResponse({'error':err},status=status.HTTP_401_UNAUTHORIZED)
    else:
        return JsonResponse({'error':'Please use PATCH method for Password updation!'},status=status.HTTP_400_BAD_REQUEST)



    




        

