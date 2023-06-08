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

from datetime import datetime,timedelta
import pytz,tzlocal
local_tz=tzlocal.get_localzone()
print(local_tz)
print(pytz.timezone(str(local_tz)))
t=datetime.now().timestamp()
print(datetime.now())
print(datetime.fromtimestamp(t))



# print(timedelta(days=2)+datetime.utcnow())
