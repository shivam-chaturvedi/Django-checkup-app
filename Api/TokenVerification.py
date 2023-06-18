from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime,timedelta
from .models import Login
import jwt
import sys,os
sys.path.append(os.path.abspath(os.path.dirname( os.path.join(__file__,'..'))))
from checkup import settings




ACCESS_TOKEN_EXPIRY_MINUTES=1
REFRESH_TOKEN_EXPIRY_DAYS=2
EMAIL=''

#use this decorator to apply another decorator to all class methods
# use @jwt_authentication directly for function api or views
# syntax: @apply_authentication(jwt_authentication)
def apply_authentication(decorator):
    def wrapper(cls,*args,**kwargs):
        for name,value in vars(cls).items():
            if(callable(value) and name!='__init__'):
                setattr(cls,name,decorator(value))
        return cls
    return wrapper

#takes a login model object as an arguement and on the basis of id and username encode it
# and generate a jwt access token
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
    refresh_token_expiry = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRY_DAYS)#days=REFRESH_TOKEN_EXPIRY_DAYS)

    # Create the payload for the refresh token
    refresh_token_payload = {
        'id': login.id,
        'username':login.Username,
        'exp': refresh_token_expiry,
    }

    # Generate and return the refresh token
    refresh_token = jwt.encode(refresh_token_payload, settings.SECRET_KEY, algorithm='HS256')
    return refresh_token

# validates the expiry or valid ,invalid jwt 
def validate_access_token(access_token):
    try:
        decoded_payload = jwt.decode(
            access_token,
            settings.SECRET_KEY,
            algorithms=['HS256']
        )
        return {'success':f"Access Token is valid for {decoded_payload['username']}"}
    except (jwt.ExpiredSignatureError):
            return {'error':'Access Token Expired!'}
    except Exception as e:
        return{'error':('Invalid Token -> '+str(e))}
    
def validate_refresh_token(refresh_token):
    try:
        decoded_payload=jwt.decode(
            refresh_token,
            settings.SECRET_KEY,
            algorithms=['HS256']
        )
        
        login=Login.get_object(id=decoded_payload['id'])
        refreshed_access_token=generate_access_token(login)
        return{'success':refreshed_access_token}
    except jwt.ExpiredSignatureError:
        return {'error':'refresh token is expired!'}
    except Exception as e:
        return {'error':('Invalid Token -> '+str(e))}

# decorator func to apply jwt authentication to anothe functions and classes
# checks header of the request and check for access_token(AUTHORIZATION) 
# and if acces_token is expired so check refresh token
def jwt_authentication(func,*args,**kwargs):
    def wrapper (request,*args,**kwargs):
        try:
            access_token=request.headers.get('Authorization',None)
            refresh_token=request.headers.get('X-Refresh-Token',None)
            if access_token is not None:
                if(str(access_token).startswith('Bearer')):
                    access_token=str(access_token.split(' ')[1])
                res=validate_access_token(str(access_token))
                if(list(res.keys())[0] == 'error'):
                    raise Exception(str(list(res.values())[0]))
                else:
                    return func(request,message=str(list(res.values())[0]),*args,**kwargs)
                
            elif refresh_token is not None:
                res=validate_refresh_token(refresh_token)
                if(list(res.keys())[0]=='error'):
                    raise Exception(str(list(res.values())[0]))
                else:
                    access_token=str(list(res.values())[0])
                    return func(request,access_token=access_token,*args,**kwargs)
                
            else:
                raise Exception("Authentication Tokens Not Found!")
        except Exception as e:
            return JsonResponse({'error':str(e)},status=status.HTTP_401_UNAUTHORIZED)
    return wrapper
        
@csrf_exempt 
@jwt_authentication 
def authenticate_token(request,*args,**kwargs):
    if('access_token' in kwargs):
        #refresh token request
        return JsonResponse({'success':'token is valid!','access_token':kwargs['access_token']})
    else:
        # access token request
        return JsonResponse({'success':kwargs['message']})
    
        
    


        

    