import io
import matplotlib.pyplot as plt
import pandas as pd
import subprocess


# TODO-oscar: escalar script para que lea todos los archivos SAR en un
# directorio y agrupe los datos en un solo DataFrame y/o haga un plot
# combinado con todos los datos agrupado por tipología


def load_metrics(command, columns_to_check):
    """Ejecuta un comando y devuelve un DataFrame con métricas relevantes."""
    try:
        output = subprocess.check_output(command, shell=True).decode("utf-8")
        data = pd.read_csv(io.StringIO(output), sep=";")
        return data
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")
        return pd.DataFrame(columns=columns_to_check)


# Configuracion del archivo SAR
sar_file = "data/sa01.new"

# Extraer datos de CPU en CSV
cpu_command = f"sadf -d {sar_file} -- -u"
memory_command = f"sadf -d {sar_file} -- -r"
network_command = f"sadf -d {sar_file} -- -n DEV"
# TODO: añadir más comandos para extraer más métricas de SAR
# * -b: I/O y bloqueo
# * -d: Actividad de dispositivos
# * -q: Carga de procesos
# * -y: TTY
# * -v: Inodos y semáforos
# * -w: Cambios de contexto
# * -W: Cambios de contexto de E/S
# * -I: Interrupciones
# * -H: Interrupciones de hardware
# * -P: Interrupciones de software
# * -R: Memoria de páginas
# * -S: Memoria de swap
# * -U: Utilización de CPU
# * -V: Memoria virtual
# * -Y: TTY
# * -Z: Memoria de caché


# Inspecionar columnas disponibles
# TODO-oscar: añadir bloque a parámetro de lanzamiento en modo info o similar
# print("Columnas disponibles en los datos:")
# print(data.columns)


# TODO-oscar: abstraer las subrutinas de ploteo en funciones para reutilizarlas
# Cargar métricas de CPU
cpu_data = load_metrics(cpu_command, ['timestamp', 'CPU', '%user'])
if not cpu_data.empty:
    print("Datos de CPU cargados correctamente")  # TODO-oscar: añadir logging
    cpu_data['timestamp'] = pd.to_datetime(cpu_data['timestamp'],
                                           errors='coerce')

    # Graficar métricas de CPU
    plt.figure(figsize=(12, 6))
    for cpu_id in cpu_data['CPU'].unique():
        cpu_subset = cpu_data[cpu_data['CPU'] == cpu_id]
        plt.plot(cpu_subset['timestamp'], cpu_subset['%user'],
                 label=f'CPU {cpu_id} User (%)')
        plt.xlabel('Timestamp')
        plt.ylabel('CPU Usage (%)')
        plt.title(f'CPU Usage Metrics over time from {sar_file}')
        plt.legend()
        plt.grid()
        plt.tight_layout()
else:
    print("No se encontraron datos de CPU en el archivo SAR")


# Cargar memoria si está disponible en el dataset
memory_data = load_metrics(memory_command, ['timestamp', 'kbmemused',
                                            'kbmemfree', '%memused'])
if not memory_data.empty:
    # TODO-oscar: añadir logging:
    print("Datos de memoria cargados correctamente")
    memory_data['timestamp'] = pd.to_datetime(memory_data['timestamp'],
                                              errors='coerce')

    # Graficar métricas de memoria
    plt.figure(figsize=(12, 6))
    plt.plot(memory_data['timestamp'], memory_data['%memused'],
             label='Memory Used (%)')
    plt.plot(memory_data['timestamp'], memory_data['kbmemfree'] / 1024,
             label='Free memory (MB)')
    plt.plot(memory_data['timestamp'], memory_data['kbmemused'] / 1024,
             label='Used memory (MB)')
    plt.xlabel('Timestamp')
    plt.ylabel('Memory Usage')
    plt.title(f'Memory Usage Metrics from {sar_file}')
    plt.legend()
    plt.grid()
    plt.tight_layout()
else:
    print("No se encontraron datos de memoria en el archivo SAR")


# Cargar red si está disponible en el dataset
network_data = load_metrics(network_command, ['timestamp', 'rxpck/s',
                                              'txpck/s', 'rxkB/s', 'txkB/s'])
if not network_data.empty:
    # TODO-oscar: añadir logging:
    print("Datos de red cargados correctamente")
    network_data['timestamp'] = pd.to_datetime(network_data['timestamp'],
                                               errors='coerce')

    # Graficar métricas de red
    plt.figure(figsize=(12, 6))
    plt.plot(network_data['timestamp'], network_data['rxpck/s'],
             label='Received per second')
    plt.plot(network_data['timestamp'], network_data['txpck/s'],
             label='Transmitted per second')
    plt.plot(network_data['timestamp'], network_data['rxkB/s'],
             label='Received KB per second')
    plt.plot(network_data['timestamp'], network_data['txkB/s'],
             label='Transmitted KB per second')
    plt.xlabel('Timestamp')
    plt.xlabel('Timestamp')
    plt.ylabel('Network Usage')
    plt.title(f'Network Usage Metrics from {sar_file}')
    plt.legend()
    plt.grid()
    plt.tight_layout()
else:
    print("No se encontraron datos de memoria en el archivo SAR")


plt.show()
