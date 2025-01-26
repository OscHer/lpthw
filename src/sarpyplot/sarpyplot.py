import io
import matplotlib.pyplot as plt
import pandas as pd
import subprocess


# Configuracion del archivo SAR
sar_file = "data/sa01.new"

# Extraer datos de CPU en CSV
command = f"sadf -d {sar_file} -- -u"

try:
    # Ejecutar el comando y capturar salida
    output = subprocess.check_output(command, shell=True).decode("utf-8")
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar: {e}")  # TODO-oscar: cambiar outputs a logger
    exit()

# Convertir la salida a un DataFrame
data = pd.read_csv(io.StringIO(output), sep=";")


# Inspecionar columnas disponibles
# TODO-oscar: añadir bloque a parámetro de lanzamiento en modo info o similar
print("Columnas disponibles en los datos:")
print(data.columns)

# Convertir la columna Timestamp a datetime
data['timestamp'] = pd.to_datetime(data['timestamp'], errors='coerce')

# Filtrar los datos para el análisis de CPU
cpu_data = data[data['CPU'] != "-1"]  # Excluye filas con cpu global = -1

# Graficar
plt.figure(figsize=(12, 6))
for cpu_id in cpu_data['CPU'].unique():
    cpu_subset = cpu_data[cpu_data['CPU'] == cpu_id]
    plt.plot(cpu_subset['timestamp'],
             cpu_subset['%user'], label=f'CPU {cpu_id}')

plt.xlabel('Timestamp')
plt.ylabel('CPU Usage(%)')
plt.title(f'CPU Usage Metrics from {sar_file}')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
