import RPi.GPIO as GPIO
import time

class Button():
   def __init__(self, pin_led, pin_button):
      self.PIN_LED = pin_led
      self.PIN_BUTTON = pin_button

      GPIO.setwarnings(False)
      GPIO.setmode(GPIO.BCM)

      GPIO.setup(self.PIN_LED, GPIO.OUT)
      GPIO.setup(self.PIN_BUTTON, GPIO.IN)

   def control(self):
           while True:
               if GPIO.input(self.PIN_BUTTON):
                   GPIO.output(self.PIN_LED, False)
               else:
                   GPIO.output(self.PIN_LED, True)

LED_PIN = 18
BUTTON_PIN = 25
controller = Button(LED_PIN, BUTTON_PIN)
controller.control()
