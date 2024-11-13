# from datetime import datetime
# from ipaddress import ip_address
# import re

# def validation(email, ip_address, date, mobile_number):
#     pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
#     pattern1 = r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
#     pattern2 = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(19|20)\d\d$'
#     pattern3 = r'^[1-9]\d{9}$'
#     return re.match(pattern, pattern1, pattern2, pattern3,  email,ip_address,date, mobile_number) is not None


# email = "user@example.com"
# ip_address = "192.168.1.1"
# date = "03/10/2024"
# mobile_number = "1234567890"
# if validation(email):
#     print(f"{email} is a valid email address.")
# elif validation(ip_address):
#     print(f"{ip_address} is a valid IP address.")
# elif validation(date):
#     print(f"{date} is a valid date.")
# elif validation(mobile_number):
#     print(f"{mobile_number} is a valid mobile number.")

# else:
#     print(f"{email} is not a valid email address.")


# Email validatin
# email = "user@example.com"
# if validation(email, ip_address, datetime, mobile_number):
#     print(f"{email} is a valid email address.")
# else:
#     print(f"{email} is not a valid email address.")

# Ip Address Validation
# ip_address = "192.168.1.1"
# if validation(ip_address):
#     print(f"{ip_address} is a valid IP address.")
# else:
#     print(f"{ip_address} is not a valid IP address.")

# Date Validation 
# date = "03/10/2024"
# if validation(date):
#     print(f"{date} is a valid date.")
# else:
#     print(f"{date} is not a valid date.")

# Mobile Number Validation

# mobile_number = "1234567890"
# if validation(mobile_number):
#     print(f"{mobile_number} is a valid mobile number.")
# else:
#     print(f"{mobile_number} is not a valid mobile number.")