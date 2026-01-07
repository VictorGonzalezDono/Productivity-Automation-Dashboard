import pandas as pd
import matplotlib.pyplot as plt

def generar_dashboard():
    try:
        # 1. Cargar los datos
        df = pd.read_csv('log_productividad.csv')
        
        # Convertir fecha a objeto datetime para que Python la entienda
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        
        print("--- Resumen General de Archivos ---")
        resumen = df.groupby('Categoria')['Archivos_Movidos'].sum()
        print(resumen)

        # 2. Crear la gráfica
        plt.figure(figsize=(10, 6))
        colores = ['#4CAF50', '#2196F3', '#FF9800', '#E91E63', '#9C27B0']
        
        resumen.plot(kind='bar', color=colores, edgecolor='black')
        
        plt.title('KPIs de Organización Digital: Archivos por Categoría', fontsize=14)
        plt.xlabel('Categoría de Archivo', fontsize=12)
        plt.ylabel('Cantidad Total', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'log_productividad.csv'.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    generar_dashboard()