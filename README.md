# CSV Data Analyzer y Ecuación diferencial
## 📊 CSV Data Analyzer

Una herramienta interactiva en Python para cargar, limpiar, analizar y visualizar archivos CSV con datos numéricos. Ideal para trabajar con datos tabulares, obtener estadísticas descriptivas rápidas, y visualizar relaciones entre variables sin necesidad de usar librerías complejas manualmente.


## 🚀 ¿Qué hace este script?

Este script es una herramienta interactiva para análisis básico de datos en formato CSV. Comienza solicitando al usuario la ruta de un archivo .csv y verifica si el archivo existe. Intenta abrirlo utilizando primero la codificación utf-8, y en caso de fallar, recurre a latin-1. Esto permite manejar archivos con diferentes orígenes de forma flexible. Una vez cargado el archivo, se informa al usuario con un mensaje claro en consola.

Después de la carga, el script procede a limpiar el conjunto de datos, enfocándose en las columnas numéricas. Muestra un resumen con la cantidad de valores faltantes por columna y, en aquellas columnas numéricas donde se encuentran datos nulos, los reemplaza automáticamente por la media de cada columna. Esto garantiza un análisis posterior mejor y sin interrupciones debido a datos incompletos.

Con los datos ya limpios, el script realiza un análisis estadístico descriptivo detallado. Para cada columna numérica se calculan medidas como la media, mediana, moda, desviación estándar, varianza, rango, rango intercuartílico (IQR) y el coeficiente de variación (calculado tanto manualmente como con la función scipy.stats.variation). Toda esta información se presenta directamente en la consola, lo que permite tener una visión rápida y clara del comportamiento de cada variable numérica.

Finalmente, el script ofrece una funcionalidad para visualizar relaciones entre variables. Muestra una lista numerada de todas las columnas numéricas disponibles y solicita al usuario seleccionar dos de ellas: una para el eje X y otra para el eje Y. Con esa información genera automáticamente un gráfico de dispersión utilizando seaborn, lo que permite al usuario explorar posibles correlaciones o patrones visuales entre las variables seleccionadas.

## 📁 Archivos generados: Análisis de Datos CSV
Este script no genera archivos automáticamente, pero *trabaja con archivos .csv que tú mismo debes proporcionar*. Una vez cargado el archivo, realiza análisis estadísticos y visualizaciones directamente en consola y en gráficos, sin guardar salidas en disco. Las visualizaciones se muestran en tiempo real y no se exportan por defecto (aunque puedes modificar el script para guardar las gráficas como imágenes .png si lo deseas).

*Entrada esperada:*  
- datos.csv (o cualquier archivo CSV que el usuario especifique)

*Salida generada:*  
- Visualización de relaciones entre variables numéricas (gráfico interactivo en ventana emergente)
- Estadísticas descriptivas impresas en consola



## 🧰 Librerías utilizadas para el Data analyzer

- pandas → Manipulación de datos tabulares.
- numpy → Cálculos numéricos.
- matplotlib & seaborn → Visualización de datos.
- scipy.stats → Estadísticas avanzadas.
- os → Interacción con el sistema de archivos.

## 🎢 Simulación de Oscilador Armónico Simple

Este proyecto simula numéricamente un oscilador armónico simple utilizando Python. Es ideal para cualquier persona interesada en física y ecuaciones diferenciales ordinarias (EDO), pues combina teoría con visualización clara y directa.


## 🚀 ¿Qué hace este script?

Este script modela y visualiza el comportamiento de un *oscilador armónico simple* mediante la resolución numérica de una ecuación diferencial de segundo orden. Utiliza la biblioteca scipy para resolver la ecuación del movimiento y matplotlib para visualizar los resultados, permitiendo así observar cómo evoluciona la posición de una masa que oscila en un resorte ideal sin fricción.

El sistema físico se define con una masa m y una constante de resorte k, y a partir de ellos se calcula la *frecuencia angular* (ω) del oscilador. La ecuación diferencial de segundo orden que describe este tipo de movimiento se transforma en un sistema de ecuaciones de primer orden para poder ser resuelta por el método solve_ivp, que es adecuado para integrar ecuaciones diferenciales ordinarias.

A partir de condiciones iniciales definidas para la posición y la velocidad, el script calcula la solución del sistema dinámico en un intervalo de tiempo dado (de 0 a 10 segundos). Los valores de posición a lo largo del tiempo se obtienen con alta resolución, usando 300 puntos evaluados uniformemente. Esto permite una representación visual fluida y precisa del comportamiento oscilatorio.

Finalmente, el script genera un gráfico que muestra la evolución de la *posición en función del tiempo*, característico del movimiento armónico simple. Esta visualización permite entender intuitivamente las propiedades del sistema, como la periodicidad, amplitud y comportamiento oscilante.


## 📁 Archivos generados: Oscilador Armónico Simple
Este script tampoco genera archivos persistentes por defecto, pero *produce una visualización dinámica de la posición en función del tiempo*, útil para analizar el comportamiento oscilatorio del sistema modelado.

*Entrada esperada:*  
- Ninguna (todos los parámetros están definidos dentro del código)

*Salida generada:*  
- Gráfico interactivo de la posición vs. tiempo (matplotlib.pyplot.show())



## 🧰 Librerías utilizadas para la EDO

- numpy → Operaciones numéricas y manejo de arrays.
- matplotlib → Visualización de datos mediante gráficos.
- scipy.integrate → Solución de ecuaciones diferenciales ordinarias (ODEs).

## Autores
Laura Boada, Valentina Vega, Leidy Piñeros
