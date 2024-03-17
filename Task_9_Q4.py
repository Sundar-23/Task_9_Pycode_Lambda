#Question-4
#Validate the regular expressions

import re
# validate email address
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# validate angladesh mobile number
def is_valid_bangladesh_mobile_number(number):
    pattern = r"^(?:\+88|01)[0-9]{9}$"
    return re.match(pattern, number) is not None

# validate USA telephone number
def is_valid_usa_telephone_number(number):
    pattern = r"^(?:\+1|1)?[-. (]*[2-9]\d{2}[-). ]*\d{3}[-. ]*\d{4}$"
    return re.match(pattern, number) is not None

# validate password
def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{16}$"
    return re.match(pattern, password) is not None

# Examples

email1 = "sample@testing.com"
if is_valid_email(email1):
    print("Valid email address")
else:
    print("Invalid email address")

mobile_number = "01658974123"
if is_valid_bangladesh_mobile_number(mobile_number):
    print("Valid Bangladesh mobile number")
else:
    print("Invalid Bangladesh mobile number")

telephone_number = "1212456789"
if is_valid_usa_telephone_number(telephone_number):
    print("Valid USA telephone number")
else:
    print("Invalid USA telephone number")

password = "Abc5@pass8710"
if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")