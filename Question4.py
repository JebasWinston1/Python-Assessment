''' Login to the machine 192.168.10.32 using python inbuilt ssh module, 
and execute the command "route -n" and get the output of the command. '''

from pexpect import pxssh

try:
    conn = pxssh.pxssh()
    hostname = '192.168.10.32'
    username = 'root'
    password = 'rootroot'
    conn.login(hostname,username,password)
    conn.sendline('route -n > RouterTable.txt')
    conn.prompt()
    print(conn.before)
except:
    print("Cannot Login")