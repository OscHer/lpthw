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
data = pd.read_csv(io.StringIO(output), sep=";", header=None)

# Renombrar columnas clave (ajustar según formatod e salida)
data.columns = ['Time', 'hostname', 'interval', 'cpu', 'user',
                'nice', 'system', 'iowait', 'steal', 'idle']

# Convertir la columna Time a datetime
data['Time'] = pd.to_datetime(data['Time'])

# Graficar
plt.figure(figsize=(12, 6))
plt.plot(data['Time'], data['user'], label='User CPU (%)')
plt.plot(data['Time'], data['system'], label='System CPU (%)')
plt.plot(data['Time'], data['idle'], label='Idle CPU (%)')

plt.xlabel('Timestamp')
plt.ylabel('CPU Usage(%)')
plt.title(f'CPU Usage Metrics from {sar_file}')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
