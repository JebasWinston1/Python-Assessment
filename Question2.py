''' Using python modules, login to the machine 192.168.10.32 and do file transfer. '''

from pexpect import pxssh

try:
    conn = pxssh.pxssh()
    hostname = '192.168.10.32'
    username = 'root'
    password = 'rootroot'
    conn.login(hostname,username,password)
    conn.sendline('touch helloworld.txt')
    conn.prompt()
    print(conn.before)
except:
    print("Cannot Login")