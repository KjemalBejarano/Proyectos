import matplotlib.pyplot as plt

class caida():
    """Clase para modelar el movimiento de caída libre de un objeto."""
    def __init__(self, g:float, altura:float, tiempo:float, velocidad_0:float, velocidad_f ):
        self.g = 9.81
        self.h=altura
        self.t=tiempo
        self.v0=velocidad_0
        self.vf=velocidad_f
    #velocidad final y altura
    def _vf_(self):
        """Calcula velocidad final del objeto"""
        resultadovf=self.v0+self.g*self.t
        return(resultadovf)
    def _h_(self):
        """Calcula altura del objeto en funcion del tiempo"""
        resultadoh=self.v0*self.t+(1/2)*self.g*self.t**2
        return(resultadoh)

class tiro():
    def __init__(self, altura:float, tiempo:float, velocidad_0:float, velocidad_f:float ):
        self.h=altura
        self.t=tiempo
        self.v0=velocidad_0
        self.vf=velocidad_f 
    def _vft_(self):
      resultadot=v0-self.g*t
      return(resultadot)
    
#metodo numerico de Euler
def euler_caida_libre(n, tiempo_total, velocidad_inicial, altura_inicial):
    """Implementa el metodo numerico de Euler para la simulacion de un objeto en caida libre"""
    g = 9.81
    t, v, h = 0.0, velocidad_inicial, altura_inicial 
    resultadose = [(t, h, v)]  

    while t < tiempo_total:
        v -= g * n  # Actualización de velocidad
        h += v * n  # Actualización de posición
        t += n      # Avance de tiempo
        resultadose.append((t, h, v))  # Guarda resultados

    return resultadose
 
# Solicita elección del método
opcion = input("¿Desea usar el método numérico (Euler) o su propio método? (numerico/propio): ").lower()

# Procesar la elección
if opcion == "numerico":
    paso_tiempo = float(input("Ingrese el tamaño del paso de tiempo (en segundos): "))
    tiempo_total = float(input("Ingrese el tiempo total de simulación (en segundos): "))
    v0 = float(input("Ingrese la velocidad inicial (en metros por segundo): "))
    h = float(input("Ingrese la altura inicial (en metros): "))
    
    resultadose = euler_caida_libre(paso_tiempo, tiempo_total, v0, h)

    for t, h, v0 in resultadose:
        print(f"Tiempo: {t:.2f} s, Altura: {h:.2f} m, Velocidad: {v0:.2f} m/s")
        

    # Extraer resultados para graficar
    tiempos = [resultado[0] for resultado in resultadose]
    alturas = [resultado[1] for resultado in resultadose]
    velocidades = [resultado[2] for resultado in resultadose]

    # Graficar altura vs. tiempo
    plt.figure(figsize=(10, 5))
    plt.plot(tiempos, alturas, label='Altura')
    plt.title('Caida de un objeto')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Altura (m)')
    plt.grid(True)
    plt.legend()
    plt.ylim(bottom=0)  # Establecer el límite inferior del eje y en 0
    plt.show()

elif opcion == "propio":
    g = 9.81
    v0 = float(input("Ingrese la velocidad inicial (en metros por segundo): "))
    t = float(input("Ingrese el tiempo total de simulación (en segundos): "))
    if t > 0:
        print("Perfecto")
    elif t < 0:
        print("Error")
    h = float(input("Ingrese la altura inicial (en metros): "))
    if h > 0:
        print("Continuemos")
    elif h < 0:
        print("Error")

    # Crear una instancia de la clase caida
    objeto_caida = caida(g, h, t, v0, 0)  # La velocidad final es desconocida en este punto

    # Crear listas vacías para almacenar los datos del movimiento del objeto
    tiempos = []
    alturas = []

    # Calcular y almacenar los datos del movimiento del objeto en intervalos de tiempo regulares
    for tiempo in range(int(t) + 1):
    # Calcular altura en función del tiempo utilizando el método de la clase
        altura = objeto_caida._h_()  
        tiempos.append(tiempo)
        alturas.append(altura)
    
    # Actualizar la posición del objeto para el próximo paso de tiempo
        objeto_caida.t = tiempo
        objeto_caida.h = altura

    # Graficar altura vs. tiempo
    plt.figure(figsize=(10, 5))
    plt.plot(tiempos, alturas, label='Altura')
    plt.title('Altura del objeto en función del tiempo')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Altura (m)')
    plt.grid(True)
    plt.legend()
    plt.show()

else:
    print("Opción no válida.")
