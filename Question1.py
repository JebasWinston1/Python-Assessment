''' Validate a IP address using python Regex '''
import re
def validate(ip_address):
    # regex = "(\d[0-2])?\d?(\d[0-5])\.(\d[0-2])?\d?(\d[0-5])\.(\d[0-2])?\d?(\d[0-5])\.(\d[0-2])?\d?(\d[0-5])"
    regex = r"[^0][0-255]{1,3}\.[^0][0-255]{1,3}\.[^0][0-255]{1,3}\.[^0][0-255]{1,3}"
    if re.search(regex,ip_address) != None:
        print("Your IP Address is correct!")
        print(re.findall(regex,ip_address))
    else:
        print("Your IP Address is incorrect!")

validate("255.255.255.1")