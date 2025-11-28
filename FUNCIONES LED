import RPi.GPIO as GPIO
import time

def ledb():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(25, GPIO.IN)
def controlar_led():
   try:
      while True:
          if GPIO.input (25):
             GPIO. output(18, False)
          else: 
             GPIO.output(18, True)
   except KeyboardInterrupt:
       pass
   finally:
      GPIO.cleanup()
if __name__ == '__ main __' :

    ledb()
    controlar_led()
