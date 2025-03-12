# This is an python program to genarate an strong password
# By using Capital letters, Small letters, digits and Special Charecters
#                                                       - Mr_MNJ

import string 
import secrets
def GeneratePassword(length = 12):
    charecters = string.ascii_letters + string.digits + "!@#$%^&*()" 
    return ''.join(secrets.choice(charecters) for i in range(length))

print("Password :", GeneratePassword())