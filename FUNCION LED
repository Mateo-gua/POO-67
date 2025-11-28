import RPi.GPIO as GPIO
import time

def ledbt():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
def control_led():
  try:
      while True:
          GPIO.output(18,True)
          time.sleep(1)
          GPIO.output(18,False)
          time.sleep(1)
  except KeyboardInterrupt:
      pass
  finally:
       GPIO.cleanup()
if __name__ == '__main__':
   
   ledbt()
   control_led()
