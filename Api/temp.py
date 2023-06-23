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
# import hashlib
# import random
# import string
# import time

# def generate_code(phone_number):
#     # Concatenate the phone number and timestamp to create a unique identifier
#     identifier = phone_number + str(time.time())

#     # Generate a hash using the identifier
#     hash_value = hashlib.md5(identifier.encode()).hexdigest()
#     print(hash_value)

#     # Take the first 6 characters from the hash
#     code = hash_value[:6]

#     # Convert the code to uppercase to ensure alphanumeric characters
#     code = code.upper()

#     return code

# # Example usage
# phone_number = "1234567890"
# code = generate_code(phone_number)
# print("Generated Code:", code)


# from faker import Faker

# fake = Faker()

# # Generate fake ID
# fake_id = fake.uuid4()[:6]

# # Generate fake name
# fake_name = fake.name()

# # Generate fake phone number
# fake_phone_number = fake.phone_number()

# # Generate fake date of birth
# fake_dob = fake.date_of_birth(minimum_age=18, maximum_age=90)

# # Generate fake email address
# fake_email = fake.email()

# # Print the generated information
# print("ID:", fake_id)
# print("Name:", fake_name)
# print("Phone Number:", fake_phone_number)
# print("Date of Birth:", fake_dob)
# print("Email:", fake_email)

import datetime
import sys,os
sys.path.append(os.path.abspath(os.path.dirname( os.path.join(__file__,''))))
from Api.models import AppointmentList
print(str(datetime.datetime.now()).split(" ")[0])
# import faker
# def generate_fake_data2():
#     f=faker.Faker()
#     for i in range(10):
#         appointment=Patient.objects.create(Unique_Id=f.uuid4()[:6],First_name=f.name(),Date_Of_Birth=datetime.now().split(" ")[0],Gender="Male",Phone=f.fake_number(),Email=f.email())
#         appointment.save()

