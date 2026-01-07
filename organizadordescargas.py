import os
import shutil
import csv
from datetime import datetime
from pathlib import Path

# DINÁMICO: Detecta la carpeta donde está guardado este archivo .py
ruta_actual = Path(__file__).parent.resolve()
log_archivo = ruta_actual / "log_productividad.csv"

# Extensiones por categoría
CATEGORIAS = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Instaladores": [".exe", ".msi"],
    "Diseño_y_Varios": [".psd", ".ai", ".zip", ".rar"]
}

def organizar():
    conteo_movimientos = {cat: 0 for cat in CATEGORIAS}
    conteo_movimientos["Otros"] = 0
    
    # Listar archivos
    archivos = [f for f in ruta_actual.iterdir() if f.is_file()]
    
    for archivo in archivos:
        # SUGERENCIA 1: No moverse a sí mismo ni al log ni a otros .py
        if archivo.suffix == ".py" or archivo.name == "log_productividad.csv":
            continue
            
        movido = False
        for categoria, extensiones in CATEGORIAS.items():
            if archivo.suffix.lower() in extensiones:
                destino = ruta_actual / categoria
                destino.mkdir(exist_ok=True)
                shutil.move(str(archivo), str(destino / archivo.name))
                conteo_movimientos[categoria] += 1
                movido = True
                break
        
        if not movido:
            destino = ruta_actual / "Otros"
            destino.mkdir(exist_ok=True)
            shutil.move(str(archivo), str(destino / archivo.name))
            conteo_movimientos["Otros"] += 1

    # SUGERENCIA 2: Registro de KPIs
    es_nuevo = not log_archivo.exists()
    with open(log_archivo, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if es_nuevo:
            writer.writerow(["Fecha", "Categoria", "Archivos_Movidos"])
        for cat, total in conteo_movimientos.items():
            if total > 0:
                writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cat, total])

if __name__ == "__main__":
    organizar()
    print(f"Éxito: Se organizó la carpeta {ruta_actual}")