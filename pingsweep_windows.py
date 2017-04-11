import os
import sys
# create a function pingsweep	
def pingsweep(x,y,z):
	a = 0
	for i in range(y,z):
		addr = x + str(i)
		lines = os.popen("ping -n 1 192.168.0." + str(i))
		
		for line in lines.readlines():
			if "TTL" in line:
				a = a+1
				print "Host :%s is up"%addr
		
	print "%d hosts found online"%a
				

#call the pingsweep function
#Give it three arguements 
#For eg :  pingsweep_windows.py "192.168.0." 1 255 
#to scan the whole subnet :192.168.0.1 to 192.168.0.255
	
pingsweep(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))