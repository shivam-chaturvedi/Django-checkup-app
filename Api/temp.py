# import jwt
# import datetime

# # Set the access token to decode and verify
# access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInVzZXJuYW1lIjoiZXhhbXBsZV91c2VyIiwiZXhwIjoxNjg2MTYxOTg2fQ.L9nyPy36ee2CeMfmUNPwKu2q67TGLDQE5Sg1U6H-kVk'  # Replace with the actual access token

# # Set the secret key used for encoding the token
# secret_key = 'your-secret-key'  # Replace with your own secret key

# try:
#     # Decode and verify the access token
#     decoded_token = jwt.decode(access_token, secret_key, algorithms=['HS256'])

#     # Access the decoded token data
#     user_id = decoded_token['user_id']
#     username = decoded_token['username']
    
#     exp = decoded_token['exp']
#     exp=datetime.datetime.fromtimestamp(exp)

#     # Print or use the decoded token data
#     print(f"User ID: {user_id}")
#     print(f"Username: {username}")
    
#     print(f"exp: {exp}")
# except jwt.ExpiredSignatureError:
#     # Handle the case where the access token has expired
#     print("Access token has expired.")
# except jwt.InvalidTokenError:
#     # Handle the case where the access token is invalid or tampered with
#     print("Invalid access token.")


# import jwt
# from datetime import datetime, timedelta

# # Set the payload data
# payload = {
#     'user_id': 123,
#     'username': 'example_user',
#     'exp': datetime.utcnow() + timedelta(minutes=3)  # Set the expiration time for the token
# }

# # Set the secret key
# secret_key = 'your-secret-key'  # Replace with your own secret key

# # Generate the access token
# access_token = jwt.encode(payload, secret_key, algorithm='HS256')

# # Print or use the generated access token
# print(access_token)

# from datetime import datetime,timedelta
# import pytz,tzlocal
# local_tz=tzlocal.get_localzone()
# print(local_tz)
# print(pytz.timezone(str(local_tz)))
# t=datetime.now().timestamp()
# print(datetime.now())
# print(datetime.fromtimestamp(t))



# print(timedelta(days=2)+datetime.utcnow())

# from django.contrib.auth.hashers import make_password,check_password
# # from django.conf import setting
# import os
# # import checkup.settings as s

# import sys
# import os

# # Add the path to the project directory
# project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# print(project_path)
# # sys.path.append(project_path)
# import sys
# print(sys.path)


# # Now you can import your project module

# # import checkup
# # print(s.ALLOWED_HOSTS)

# print(os.environ.get('DJANGO_SETTINGS_MODULE'))

# print(os.path.dirname(__file__))
# data="shiavm"
# # print(s.ALLOWED_HOSTS)


# from checkup import settings
# from django.contrib.auth.hashers import make_password,check_password
# data="shivam"
# # print(make_password(data))
# # print(check_password('shivam',"pbkdf2_sha256$600000$aeRMiYCdea4EMbHHfatNvU$l70dppxPjV0+xfAbACsJW2Z23kGN5IyvZS0l99hqfQ4="))
