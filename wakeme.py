import time
import os

name = raw_input('What is your name?')

print ("Hello, " + name)

alarm_HH = raw_input('Enter the hour that you would like to wake up.')
alarm_MM = raw_input('Enter the minutes of the hour')

print ("Ok I'll wake you up at " + alarm_HH + ":" + alarm_MM)

alarm = "on"
while alarm == "on":
	now = time.localtime()
	if now.tm_hour == int(alarm_HH) and now.tm_min == int(alarm_MM):
		print "WAKE UP"
		for i in range(5):
			os.system('say "Wake up Motherfucker"')