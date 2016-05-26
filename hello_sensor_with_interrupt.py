
import  RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24

print "Distance measurement in progress"
GPIO.setup(TRIG,GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ECHO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


pulse_start = time.time()
pulse_end = time.time()


def send_pulse():
	GPIO.input(TRIG,True)
	time.sleep(0.00001)
	GPIO.output(TRIG,False)
	 
def on_low_echo(channel):
	pulse_start = time.time()	
	print 'got high'

def on_high_echo(channel):
	pulse_end = pulse.time()
	print  'got low'
	print_distance()

def print_distance():
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance,2)
	print 'Distance %d cm',distance
		
try:

	GPIO.output(TRIG,False)
	print "Waiting for Sendor to settle"
	time.sleep(2)
	GPIO.add_event_detect(ECHO,GPIO.RISING, callback=on_high_echo)
	GPIO.add_event_detect(ECHO,GPIO.FALLING,callback=on_low_echo)
	send_pulse()
	
	
finally:
	GPIO.cleanup()

