import subprocess
import pandas as pd
import matploblib.pyplot as plt

# Configuracion del archivo SAR
sar_file = "data/sa01"

# Extraer datos de CPU en CSV
command = f"sadf -d {sar_file} -- -u"

try:
    # Ejecutar el comando y capturar salida
    output = subprocess.check_output(command, shell=True).decode("utf-8")
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar: {e}")  # TODO-oscar: cambiar outputs a logger
    exit()

# Convertir la salida a un DataFrame
data = pd.read_csv(pd.compat.StringIO(output, sep=",", header=None))

# Renombrar columnas clave (ajustar según formatod e salida)
data.columns = ['Time', 'hostname', 'interval']
