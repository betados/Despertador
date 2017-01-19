import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
p.start(0)
p.ChangeDutyCycle(50)
try:
    while 1:
        for freq in range(20000):
            p.ChangeFrequency(freq+1) 
            time.sleep(0.005)
        
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()