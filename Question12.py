''' Use Reg expression
     a) do ifconfig eth0 (or any interface) in linux and get its mac address
     b) Do ping to an IP 
	    (Ex output: ping 1.1.1.1 -c 2
	     PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
	     64 bytes from 1.1.1.1: icmp_seq=1 ttl=53 time=8.03 ms
	     64 bytes from 1.1.1.1: icmp_seq=2 ttl=53 time=7.93 ms
             --- 1.1.1.1 ping statistics ---
	     2 packets transmitted, 2 received, 0% packet loss, time 1006ms
	     rtt min/avg/max/mdev = 7.930/7.984/8.039/0.104 ms)
 	    Get the min max and average rtt values
     c) http://192.168.12.217:8080/viewvc/Documents
     From the URL, get the protocol, IP address, port number and path. '''

''' Part C '''
import re

url = "http://192.168.12.217:8080/viewvc/Documents" 
regex = r"([a-z]+)://([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}):(\d{4})((/[a-zA-Z]+)*)"
matches = re.search(regex, url)
print(f"URL = {url}")
print(f"Protocol: {matches.group(1)}")
print(f"IP Address: {matches.group(2)}")
print(f"Port: {matches.group(3)}")
print(f"Path: {matches.group(4)}")