import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas y funciones matemáticas
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib para crear gráficos
from scipy.integrate import solve_ivp  # Importa el método solve_ivp para resolver ecuaciones diferenciales

# Parámetros del sistema
m = 1.0       # masa del objeto en kilogramos (kg)
k = 4.0       # constante del resorte en newtons por metro (N/m)
omega = np.sqrt(k / m)  # Calcula la frecuencia angular del oscilador (rad/s)

# Ecuación diferencial de segundo orden convertida a un sistema de ecuaciones de primer orden
def oscilador_armonico(t, y):  # Define la función que representa el sistema dinámico
    x, v = y  # Asigna x = y[0] (posición), v = y[1] (velocidad)
    dxdt = v  # Derivada de la posición es la velocidad
    dvdt = -omega**2 * x  # Derivada de la velocidad es la aceleración (ley de Hooke: -k/m * x)
    return [dxdt, dvdt]  # Retorna el sistema como un vector de derivadas

# Condiciones iniciales
x0 = 1.0  # Posición inicial en metros
v0 = 0.0  # Velocidad inicial en metros por segundo

# Intervalo de tiempo
t_span = (0, 10)  # Intervalo de tiempo de 0 a 10 segundos
t_eval = np.linspace(*t_span, 300)  # Crea 300 puntos uniformemente distribuidos entre 0 y 10 para evaluar la solución

# Resolución de la ecuación diferencial
sol = solve_ivp(oscilador_armonico, t_span, [x0, v0], t_eval=t_eval)  # Resuelve el sistema usando el método de integración de scipy

# Graficar resultados
plt.plot(sol.t, sol.y[0])  # Grafica la posición (sol.y[0]) en función del tiempo (sol.t)
plt.title('Oscilador Armónico Simple')  # Título del gráfico
plt.xlabel('Tiempo (s)')  # Etiqueta del eje x
plt.ylabel('Posición (m)')  # Etiqueta del eje y
plt.grid(True)  # Muestra una cuadrícula en el gráfico
plt.show()  # Muestra el gráfico en pantalla