
import  RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24

print "Distance measurement in progress"
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


pulse_start = time.time()
pulse_end = time.time()
waiting_for_high = True
waiting_for_low = False

def send_trigger():
	time.sleep(1)
	GPIO.output(TRIG,True)
	time.sleep(0.00001)
	GPIO.output(TRIG,False)
	 
def on_echo_pulse(channel):
	global pulse_end, pulse_start, got_high, waiting_for_high, waiting_for_low
	if GPIO.input(ECHO) == GPIO.LOW and waiting_for_low:
		#print 'echo pulse low'
		pulse_end = time.time()
		print_distance(pulse_end,pulse_start)
		waiting_for_low = False
		waiting_for_high = True
	elif waiting_for_high:
		#print 'echo pulse high'
		pulse_start = time.time()
		waiting_for_high = False
		waiting_for_low = True

def print_distance(pend,pstart):
	pulse_duration = pend - pstart
	distance = pulse_duration * 17150
	distance = round(distance,2)
	print 'Distance %s cm' % distance
	send_trigger()
		
try:
	GPIO.add_event_detect(ECHO,GPIO.BOTH, callback=on_echo_pulse)
	GPIO.output(TRIG,False)
	print "Waiting for Sendor to settle"
	time.sleep(2)
	send_trigger()
	print 'press any  key to terminate'
	raw_input()
	
finally:
	GPIO.cleanup()
