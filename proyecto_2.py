# ==== Importación de módulos ====

import os  # Permite interactuar con el sistema operativo (verificar rutas, archivos, etc.)
import pandas as pd  # Librería para manipulación y análisis de datos en forma de tablas (DataFrames)
import numpy as np  # Librería para cálculos numéricos y arrays
import matplotlib.pyplot as plt  # Módulo de visualización de gráficos de matplotlib
import seaborn as sns  # Librería para visualización estadística avanzada
import scipy.stats as ss  # Submódulo de scipy para estadísticas y distribuciones
import time  # Módulo para medir el tiempo (usado en el decorador)

# ==== Decorador para medir el tiempo de ejecución de funciones ====
def medir_tiempo(func):  # Recibe como parámetro la función original
    """

    se utiliza para calcular e imprimir el tiempo de ejecución de cualquier función a la que se aplique. Internamente, define una función envolvente (wrapper) que registra el tiempo justo antes y después de ejecutar la función original, calcula la diferencia y muestra el resultado en segundos, sin alterar el comportamiento ni los valores de retorno de la función decorada. Gracias a su uso de *args y **kwargs, puede aplicarse a funciones con cualquier tipo y número de argumentos,
     lo que lo hace altamente reutilizable y útil para evaluar el rendimiento de distintas partes del código.

    """
    def wrapper(*args, **kwargs):  # Define una función interna (envoltura)
        inicio = time.time()  # Registra el tiempo antes de ejecutar la función
        resultado = func(*args, **kwargs)  # Llama a la función original con sus argumentos
        fin = time.time()  # Registra el tiempo después de ejecutarla
        print(f"\n Tiempo de ejecución de '{func.__name__}': {fin - inicio:.4f} segundos")  # Imprime duración
        return resultado  # Devuelve el resultado de la función original
    return wrapper  # Devuelve la función decorada

# ==== Función para cargar un archivo CSV ====
@medir_tiempo  # Aplica el decorador para medir su tiempo


def cargar_csv():
    """solicita al usuario una ruta de archivo CSV, valida su existencia y luego intenta cargarlo en un DataFrame de pandas. Primero, elimina espacios innecesarios en la ruta ingresada y verifica si corresponde a un archivo real en el sistema. Si el archivo no existe, muestra un mensaje de error y retorna None. Si el archivo existe, intenta abrirlo usando codificación UTF-8; si esto falla por un error de codificación, intenta nuevamente con latin-1. Si ambos intentos fallan, captura la excepción y muestra un mensaje con el error específico. 
    Si la lectura tiene éxito, informa al usuario que el archivo fue cargado correctamente y devuelve el DataFrame resultante para su posterior análisis."""
    ruta = input("Ingrese la ruta completa del archivo CSV: ").strip()  # Pide al usuario la ruta del archivo
    if not os.path.isfile(ruta):  # Verifica si el archivo existe en esa ruta
        print("La ruta proporcionada no es válida o el archivo no existe.")  # Mensaje de error
        return None  # Sale de la función devolviendo None

    try:
        df = pd.read_csv(ruta, encoding='utf-8')  # Intenta leer el archivo usando codificación UTF-8
    except UnicodeDecodeError:  # Si falla por codificación
        try:
            df = pd.read_csv(ruta, encoding='latin-1')  # Intenta leer usando codificación alternativa
        except Exception as e:  # Si ocurre otro tipo de error
            print(f"Error al leer el archivo: {e}")  # Muestra el error
            return None  # Sale devolviendo None

    print(f"\nArchivo '{os.path.basename(ruta)}' cargado exitosamente.\n")  # Confirmación con el nombre del archivo
    return df  # Retorna el DataFrame leído

# ==== Función para limpiar datos faltantes ====
@medir_tiempo
def limpiar_datos(df):

    """Toma un DataFrame como entrada y realiza una limpieza básica enfocada en los valores faltantes. Primero, muestra al usuario 
    un resumen del número de valores nulos en cada columna del DataFrame. Luego, identifica todas las columnas que contienen datos numéricos 
    y reemplaza sus valores nulos por la media de cada columna correspondiente, lo cual es una práctica común para mantener la coherencia estadística de los datos. 
    Finalmente, informa que se ha realizado esta imputación y retorna el DataFrame modificado, listo para ser analizado sin problemas por 
    valores ausentes en sus variables numéricas."""

    print("Resumen de valores faltantes por columna:")
    print(df.isnull().sum())  # Imprime cuántos valores nulos hay en cada columna

    columnas_numericas = df.select_dtypes(include=[np.number]).columns  # Selecciona solo columnas numéricas
    df[columnas_numericas] = df[columnas_numericas].fillna(df[columnas_numericas].mean())  # Rellena valores nulos con la media de cada columna
    print("\nValores faltantes en columnas numéricas han sido reemplazados por la media.")
    return df  # Retorna el DataFrame modificado

# ==== Función para mostrar estadísticas descriptivas ====
@medir_tiempo
def estadisticas_descriptivas(df):
    """enera un análisis estadístico detallado de las columnas numéricas de un DataFrame.
      Primero, identifica todas las columnas que contienen datos numéricos. 
      Si no hay ninguna, informa al usuario y termina la ejecución. 
      Para cada columna numérica, elimina los valores nulos y calcula diversas medidas estadísticas:
    media, mediana, moda, desviación estándar y varianza , rango, rango intercuartílico (IQR) y coeficiente de variación. 
    Todos estos resultados se imprimen en consola, proporcionando un panorama completo de la distribución de cada variable numérica."""
    columnas_numericas = df.select_dtypes(include=[np.number]).columns  # Filtra columnas numéricas
    if columnas_numericas.empty:  # Verifica si hay columnas numéricas
        print("No hay columnas numéricas para analizar.")  # Mensaje si no hay
        return  # Sale de la función

    print("\nEstadísticas descriptivas:")
    for col in columnas_numericas:  # Recorre cada columna numérica
        serie = df[col].dropna()  # Elimina valores nulos para análisis
        media = serie.mean()  # Calcula la media
        mediana = serie.median()  # Calcula la mediana
        moda = serie.mode().values  # Calcula la moda (puede tener varias)
        std = serie.std(ddof=0)  # Desviación estándar (poblacional)
        varianza = serie.var(ddof=0)  # Varianza (poblacional)
        rango = serie.max() - serie.min()  # Rango = máximo - mínimo
        iqr = serie.quantile(0.75) - serie.quantile(0.25)  # IQR = Q3 - Q1
        cv = std / media if media != 0 else np.nan  # Coeficiente de variación manual
        cv_scipy = ss.variation(serie)  # Coeficiente de variación con scipy

        # Imprime todos los resultados
        print(f"\nColumna: {col}")
        print(f"  Media: {media}")
        print(f"  Mediana: {mediana}")
        print(f"  Moda: {moda}")
        print(f"  Desviación estándar: {std}")
        print(f"  Varianza: {varianza}")
        print(f"  Rango: {rango}")
        print(f"  IQR: {iqr}")
        print(f"  Coef. de variación (manual): {cv}")
        print(f"  Coef. de variación (scipy): {cv_scipy}")

# ==== Función para graficar relaciones entre variables ====
@medir_tiempo
def visualizar_relaciones(df):
    """permite al usuario generar un gráfico de dispersión entre dos columnas numéricas de un DataFrame. 
    Verifica que existan al menos dos columnas numéricas, muestra sus nombres numerados y solicita al usuario que seleccione dos para graficar. 
    Si la selección es válida, crea y muestra el gráfico con seaborn, facilitando el análisis visual de la relación entre ambas variables."""
    columnas_numericas = df.select_dtypes(include=[np.number]).columns  # Selecciona columnas numéricas
    if len(columnas_numericas) < 2:  # Verifica que haya al menos 2 columnas
        print("No hay suficientes columnas numéricas para visualizar relaciones.")
        return  # Sale si no hay suficientes

    print("\nColumnas numéricas disponibles:")
    for i, col in enumerate(columnas_numericas, 1):  # Lista las columnas numeradas
        print(f"{i}. {col}")

    try:
        idx_x = int(input("Seleccione el número de la columna para el eje X: ")) - 1
        idx_y = int(input("Seleccione el número de la columna para el eje Y: ")) - 1
        if idx_x not in range(len(columnas_numericas)) or idx_y not in range(len(columnas_numericas)):
            print("Selección inválida.")
            return
        x = columnas_numericas[idx_x]
        y = columnas_numericas[idx_y]
        sns.scatterplot(data=df, x=x, y=y)
        plt.title(f"Relación entre '{x}' y '{y}'")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.tight_layout()
        plt.show()
    except ValueError:
        print("Entrada inválida.")

def main():
    df = cargar_csv()
    if df is None:
        return
    df = limpiar_datos(df)
    estadisticas_descriptivas(df)
    visualizar_relaciones(df)

if __name__ == "__main__":
    main()