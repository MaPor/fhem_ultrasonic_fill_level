#Libraries
import RPi.GPIO as GPIO
import time

#Variablen

einbauhoehe= 205.5 #cm
fuellhoehe=0


#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
        # Dem Sensor nach Programmstart Zeit geben "bereit zu sein"
        time.sleep(0.05)

	# set Trigger to HIGH
	GPIO.output(GPIO_TRIGGER, True)

	# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)

	StartTime = time.time()
	StopTime = time.time()

	# save StartTime
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()

	# save time of arrival
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()

	# time difference between start and arrival
	TimeElapsed = StopTime - StartTime
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	distance = (TimeElapsed * 34300) / 2

	return distance

dist0 = distance() #Messwert Sensor zur Wasseroberflaeche in cm
dist1 = distance() #Messwert Sensor zur Wasseroberflaeche in cm
dist2 = distance() #Messwert Sensor zur Wasseroberflaeche in cm
dist3 = distance() #Messwert Sensor zur Wasseroberflaeche in cm
dist4 = distance() #Messwert Sensor zur Wasseroberflaeche in cm

mittel = (dist0+dist1+dist2+dist3+dist4)/5
thres = 5

if (dist0-mittel)>thres:
	dist0=mittel
if (dist1-mittel)>thres:
        dist1=mittel
if (dist2-mittel)>thres:
        dist2=mittel
if (dist3-mittel)>thres:
        dist3=mittel
if (dist4-mittel)>thres:
        dist4=mittel
 
result = (dist0+dist1+dist2+dist3+dist4)/5

print (einbauhoehe-result) #Ausgabe Fuellhoehe fuer FHEM
GPIO.cleanup()
