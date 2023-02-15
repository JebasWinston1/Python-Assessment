''' Extract mac address and Interface information from the below output 
and store in it a dict. '''

import re
table = ''' 
VLAN  Mac Address        Interface  IfIndex     Status
----  -----------------  ---------  -------  ------------
   1  00:0D:88:68:8C:3F   1/1       1        Learned
   1  00:0D:88:68:8D:A1   1/10      10       Learned
   1  00:0D:88:68:8D:A3   1/2       2        Learned
   1  00:80:63:CB:A7:00   4/1       57       Management '''

regex_mac = r"[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}"
regex_interface = r"\d+/\d+"

mac_addresses = re.findall(regex_mac,table)
interfaces = re.findall(regex_interface, table)

print(mac_addresses)
print(interfaces)
print(dict(zip(mac_addresses,interfaces)))