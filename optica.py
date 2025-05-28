import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as ss
import time  # Para medir el tiempo

# Decorador para medir el tiempo de ejecución
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"\n⏱️ Tiempo de ejecución de '{func.__name__}': {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def cargar_csv():
    ruta = input("Ingrese la ruta completa del archivo CSV: ").strip()
    if not os.path.isfile(ruta):
        print("La ruta proporcionada no es válida o el archivo no existe.")
        return None
    try:
        df = pd.read_csv(ruta, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(ruta, encoding='latin-1')
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return None
    print(f"\nArchivo '{os.path.basename(ruta)}' cargado exitosamente.\n")
    return df

@medir_tiempo
def limpiar_datos(df):
    print("Resumen de valores faltantes por columna:")
    print(df.isnull().sum())
    columnas_numericas = df.select_dtypes(include=[np.number]).columns
    df[columnas_numericas] = df[columnas_numericas].fillna(df[columnas_numericas].mean())
    print("\nValores faltantes en columnas numéricas han sido reemplazados por la media.")
    return df

@medir_tiempo
def estadisticas_descriptivas(df):
    columnas_numericas = df.select_dtypes(include=[np.number]).columns
    if columnas_numericas.empty:
        print("No hay columnas numéricas para analizar.")
        return
    print("\nEstadísticas descriptivas:")
    for col in columnas_numericas:
        serie = df[col].dropna()
        media = serie.mean()
        mediana = serie.median()
        moda = serie.mode().values
        std = serie.std(ddof=0)
        varianza = serie.var(ddof=0)
        rango = serie.max() - serie.min()
        iqr = serie.quantile(0.75) - serie.quantile(0.25)
        cv = std / media if media != 0 else np.nan
        cv_scipy = ss.variation(serie)
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

@medir_tiempo
def visualizar_relaciones(df):
    columnas_numericas = df.select_dtypes(include=[np.number]).columns
    if len(columnas_numericas) < 2:
        print("No hay suficientes columnas numéricas para visualizar relaciones.")
        return
    print("\nColumnas numéricas disponibles:")
    for i, col in enumerate(columnas_numericas, 1):
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