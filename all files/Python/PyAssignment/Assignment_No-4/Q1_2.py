import re

def validate_ip_address(ip_address):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
    return re.match(pattern, ip_address) is not None

# Example usage:
ip_address = "192.168.1.1"
if validate_ip_address(ip_address):
    print(f"{ip_address} is a valid IP address.")
else:
    print(f"{ip_address} is not a valid IP address.")
