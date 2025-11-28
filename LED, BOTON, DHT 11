import RPi.GPIO as GPIO
import time
import adafruit_dht 
import board # NECESARIO para usar board.D4


class Robot:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo

    def encender(self):
        print(self.nombre, "está encendido.")

    def apagar(self):
        print(self.nombre, "está apagado.")

    def estado(self):
        print("Robot:", self.nombre, "Modelo:", self.modelo)
      

class RobotObrero(Robot):
    PIN_LED = 18 

    def __init__(self, nombre, modelo, tarea):
        super().__init__(nombre, modelo)
        self.tarea = tarea
        GPIO.setup(self.PIN_LED, GPIO.OUT)
        print(f"[{self.nombre}]: GPIO {self.PIN_LED} configurado (LED Obrero).")

    def trabajar(self):
        print(self.nombre, "está realizando la tarea:", self.tarea)

    def controlar_led(self):
        print(f"[{self.nombre}]: Iniciando control de parpadeo. Presiona CTRL+C para detener y pasar al Explorador.")
        while True:
            GPIO.output(self.PIN_LED, True)
            time.sleep(1)
            GPIO.output(self.PIN_LED, False)
            time.sleep(1)


class RobotExplorador(Robot):
    PIN_LED = 18 
    PIN_BUTTON = 25
    _last_state = False 

    def __init__(self, nombre, modelo, zona_exploracion):
        super().__init__(nombre, modelo)
        self.zona_exploracion = zona_exploracion
        
        GPIO.setup(self.PIN_LED, GPIO.OUT) 
        GPIO.setup(self.PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        print(f"[{self.nombre}]: GPIO {self.PIN_LED} (LED) y {self.PIN_BUTTON} (Botón) configurados.")

    def explorar(self):
        print(self.nombre, "está listo para explorar la zona:", self.zona_exploracion)
        print(f"Mantén pulsado el botón en el pin {self.PIN_BUTTON} para EXPLORAR.")
        
        while True:
            current_state = GPIO.input(self.PIN_BUTTON) == GPIO.HIGH
            
            if current_state:
                GPIO.output(self.PIN_LED, False) 
                if current_state != self._last_state:
                    print(self.nombre, "DETENIDO.")
                    time.sleep(0.05)
            
                
            else:
                GPIO.output(self.PIN_LED, True) 
                print(self.nombre, "EXPLORANDO.")
                time.sleep(0.5) 
                
            
            self._last_state = current_state

class RobotMedico(Robot):
    # La inicialización del dispositivo se hace dentro de diagnosticar()
    def __init__(self, nombre, modelo, especialidad):
        super().__init__(nombre, modelo)
        self.especialidad = especialidad
        
    def diagnosticar(self):
        print(self.nombre, "está realizando la especialidad:", self.especialidad)
        
        # Inicialización del dispositivo DHT con board.D4 (GPIO 4)
        try:
            dht_device = adafruit_dht.DHT11(board.D4)
        except Exception as e:
            print(f"[{self.nombre} - ERROR DE INICIALIZACIÓN]: No se pudo crear el objeto DHT. Asegúrate de que 'board' esté configurado. Error: {e}")
            return

        while True:
            try:
                temperature_c = dht_device.temperature
                # Cálculo de Fahrenheit
                temperature_f = temperature_c * (9 / 5) + 32
                humidity = dht_device.humidity

                # Imprime la lectura según el formato solicitado
                print(f"[{self.nombre} - DIAGNÓSTICO]: Temp:{temperature_c:.1f} C / {temperature_f:.1f} F    Humidity: {humidity}%")
            
            except RuntimeError as err:
                # Maneja errores comunes de lectura del sensor (CRC error)
                print(f"[{self.nombre} - ERROR DE LECTURA]: {err.args[0]}")

            time.sleep(2.0) # Espera 2.0 segundos entre lecturas


def simulacion_robots():
    GPIO.setwarnings(False)
    # Se necesita el modo BCM para los pines 18 y 25 del Obrero/Explorador
    GPIO.setmode(GPIO.BCM) 

    obrero = RobotObrero("R-Worker", "MK-3", "Control de iluminación")
    explorador = RobotExplorador("R-Explorer", "XJ-9", "Marte")
    medico = RobotMedico("R-Medic", "M-100", "Monitoreo Ambiental")
    
    try:
        # 1. Robot Obrero (Termina con CTRL+C)
        obrero.encender()
        obrero.trabajar()
        obrero.controlar_led()

    except KeyboardInterrupt:
        print("\n--- ¡Transición al Explorador! ---")
        explorador.encender()
        try:
            # 2. Robot Explorador (Termina con un 2do CTRL+C)
            explorador.explorar()
            
        except KeyboardInterrupt:
            print("\n--- ¡Transición al Médico! ---")
            
            # 3. Robot Médico (Termina con un 3er CTRL+C)
            medico.encender()
            try:
                medico.diagnosticar()
            except KeyboardInterrupt:
                print("\nRobot Médico detenido por CTRL+C.")

    finally:
        # Limpieza final
        print("\n--- Fin de Simulación ---")
        GPIO.cleanup()
        print("Pines GPIO liberados. Programa terminado.")


if __name__ == "__main__":
    simulacion_robots()
