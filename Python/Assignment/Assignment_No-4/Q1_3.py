import re

def validate_date(date):
    pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(19|20)\d\d$'
    return re.match(pattern, date) is not None

date = "03/10/2024"
if validate_date(date):
    print(f"{date} is a valid date.")
else:
    print(f"{date} is not a valid date.")
