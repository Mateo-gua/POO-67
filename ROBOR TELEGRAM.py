import time 
import requests
import RPi.GPIO as GPIO

class LedController:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def status(self):
        return GPIO.input(self.pin)

class TelegramBot:
    def __init__(self, token, led_controller):
        self.token = token
        self.led = led_controller
        self.base_url = f"https://api.telegram.org/bot{self.token}/"
        self.last_update_id = None

    def send_message(self, chat_id, text):
        url = self.base_url + "sendMessage"
        payload = {"chat_id": chat_id, "text": text}
        try:
            requests.post(url, data=payload, timeout=5)
        except Exception as e:
            print("Error enviando mensaje:", e)

    def get_updates(self, timeout=30):
        url = self.base_url + "getUpdates"
        params = {"timeout": timeout}

        if self.last_update_id:
            params["offset"] = self.last_update_id + 1

        try:
            r = requests.get(url, params=params, timeout=timeout + 5)
            return r.json()
        except Exception as e:
            print("Error getUpdates:", e)
            return None

    def handle_message(self, item):
        if "message" not in item:
            return

        m = item["message"]
        chat_id = m["chat"]["id"]
        text = m.get("text", "").strip().lower()

        print(f"Mensaje de {chat_id}: {text}")

        if text == "/on":
            self.led.on()
            self.send_message(chat_id, " LED encendido")

        elif text == "/off":
            self.led.off()
            self.send_message(chat_id, " LED apagado")

        elif text == "/status":				
            est = self.led.status()
            self.send_message(chat_id, f" Estado del LED: {'ON' if est else 'OFF'}")

        elif text == "/id":
            self.send_message(chat_id, f" Tu chat ID es: {chat_id}")

        else:
            self.send_message(chat_id,
                              "Comandos disponibles:\n"
                              "/on\n/off\n/status\n/id")

    def run(self):
        while True:
            updates = self.get_updates()

            if not updates or not updates.get("ok"):
                time.sleep(1)
                continue

            for item in updates.get("result", []):
                self.last_update_id = item["update_id"]

                try:
                    self.handle_message(item)
                except Exception as e:
                    print("Error procesando mensaje:", e)

if __name__ == "__main__":
    TOKEN = "8513640504:AAGJAzWpp5K6Ec8uw_4K8Nvyw9EjgEK5E1g" 
LED_PIN=18

    led = LedController(LED_PIN)
    bot = TelegramBot(TOKEN, led)

    try:
        bot.run()
    except KeyboardInterrupt:
    finally:
        GPIO.cleanup()
