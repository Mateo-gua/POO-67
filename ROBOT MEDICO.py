class Robot:
    PIN_LED = 18

    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo
        self.led_encendido = False 

    def encender(self):
        print(self.nombre, "está encendido.")
        self.led_encendido = True
        print(f"**LED: Encendido** (Simulando GPIO.output({self.PIN_LED}, GPIO.HIGH))")

    def apagar(self):
        print(self.nombre, "está apagado.")
        self.led_encendido = False
        print(f"**LED: Apagado** (Simulando GPIO.output({self.PIN_LED}, GPIO.LOW))")

    def estado(self):
        print("Robot:", self.nombre, "Modelo:", self.modelo)
        print("Estado del LED (Pin 18):", "Encendido" if self.led_encendido else "Apagado")


class RobotExplorador(Robot):
    def __init__(self, nombre, modelo, zona_exploracion):
        super().__init__(nombre, modelo)
        self.zona_exploracion = zona_exploracion

    def presionar_boton_explorar(self):
        print(self.nombre, "ha **PRESIONADO EL BOTÓN** e iniciará la exploración.")
        self.explorar()

    def soltar_boton_explorar(self):
        print(self.nombre, "ha **SOLTADO EL BOTÓN** y se detendrá.")
        self.detener_exploracion()
    
    def explorar(self):
        print(self.nombre, "está explorando la zona:", self.zona_exploracion)

    def detener_exploracion(self):
        print(self.nombre, "se ha **detenido** en la zona:", self.zona_exploracion)


class RobotMedico(Robot):
    def __init__(self, nombre, modelo, especialidad):
        super().__init__(nombre, modelo)
        self.especialidad = especialidad
        self.temperatura_detectada = 36.5 
        
    def diagnosticar(self):
        print(self.nombre, "está realizando la especialidad:", self.especialidad)
    
    def detectar_temperatura(self, temperatura):
        self.temperatura_detectada = temperatura
        print(f"**Sensor de Temperatura:** Detectado {self.temperatura_detectada}°C.")
        if self.temperatura_detectada > 37.0:
            print(self.nombre, "recomienda atención médica por posible fiebre.")
        else:
            print(self.nombre, "indica una temperatura corporal normal.")


def simulacion_robots():
    explorador = RobotExplorador("R-Explorer", "XJ-9", "Zona Ártica")
    
    print("--- Simulación Robot Explorador ---")
    explorador.encender()
    explorador.presionar_boton_explorar()
    explorador.estado()
    explorador.soltar_boton_explorar()
    explorador.apagar()
    
def sim_robot_med():    
    medico = RobotMedico("RMED", "R-MG", "Medicina General")

    print("\n--- Simulación Robot Médico ---")

    medico.encender()
    medico.diagnosticar()
    medico.detectar_temperatura(38.2)
    medico.estado()
    medico.apagar()

simulacion_robots()
sim_robot_med()
