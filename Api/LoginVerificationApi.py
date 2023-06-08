from django.http import JsonResponse
from rest_framework import status
from Api.models import Login
from Api.serializers import Login_Serializer
from django.views.decorators.csrf import csrf_exempt
import io
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser
from datetime import datetime,timedelta
from django.conf import settings
import jwt

ACCESS_TOKEN_EXPIRY_MINUTES=2
REFRESH_TOKEN_EXPIRY_DAYS=2
EMAIL=''

def generate_access_token(login):
    # Set the expiration time for the access token
    access_token_expiry = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)

    # Create the payload for the access token
    access_token_payload = {
        'id': login.id,
        'username':login.Username,
        'exp': access_token_expiry,
    }

    # Generate and return the access token
    access_token = jwt.encode(access_token_payload,settings.SECRET_KEY, algorithm='HS256')
    return access_token

def generate_refresh_token(login):
    # Set the expiration time for the refresh token
    refresh_token_expiry = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRY_DAYS)#days=REFRESH_TOKEN_EXPIRY_DAYS)

    # Create the payload for the refresh token
    refresh_token_payload = {
        'id': login.id,
        'username':login.Username,
        'exp': refresh_token_expiry,
    }

    # Generate and return the refresh token
    refresh_token = jwt.encode(refresh_token_payload, settings.SECRET_KEY, algorithm='HS256')
    return refresh_token



def validate_access_token(access_token, refresh_token):
    try:
        decoded_payload = jwt.decode(
            access_token,
            settings.SECRET_KEY,
            algorithms=['HS256']
        )
        return {
                'username': decoded_payload['username'],
                'access_token': access_token
            }
    except (jwt.ExpiredSignatureError):
        try:
            decoded_refresh_token = jwt.decode(
                refresh_token,
                settings.SECRET_KEY,
                algorithms=['HS256']
            )
            # Refresh the access token and return it
            login=Login.get_object(id=decoded_refresh_token['id'])
            new_access_token = generate_access_token(login)
            return {
                'username': decoded_refresh_token['username'],
                'access_token': new_access_token
            }
        
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return None 


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
            if(str(Password)==password):
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



        
@csrf_exempt
def VerifyToken(request):
    if(request.method=='POST'):
        # print(request.body)
        try:
            stream=io.BytesIO(request.body)
            data=JSONParser().parse(stream)
            access_token=data['access_token']
            refresh_token=data['refresh_token']
            res=validate_access_token(access_token=access_token,refresh_token=refresh_token)
            if res is not None:
                username=res['username']
                new_access_token=res['access_token']
                return JsonResponse({'message':'Token is valid','username':username,'access_token':new_access_token},status=status.HTTP_200_OK)
            else:
                return JsonResponse({'error':'Token invalid or expired'},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return JsonResponse({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'error':'Please use POST method for this!'},status=status.HTTP_400_BAD_REQUEST)
    




        

