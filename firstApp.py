import sys
import datetime
import time

print ("This is my Second App using Dockerfile")
print("Python version = ",sys.version)
while(1) :
	now = datetime.datetime.now()
	print "Current date and time : ", now.strftime("%Y-%m-%d %H:%M:%S")
	time.sleep(1)
