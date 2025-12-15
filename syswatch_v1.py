import platform
import psutil

print("=== SysWatch v1.0 ===")

def systeme():
    print("=== Système ===")
    print(f"Système d'exploitation : {platform.system()}")
    print(f"Version du système     : {platform.version()}")
    print(f"Architecture           : {platform.architecture()[0]}")
    print(f"nom de la machine      : {platform.node()}")
    print(f"version de python      : {platform.python_version()}")
def cpu():
      cpu_percent = psutil.cpu_percent(interval=1)
      print("=== CPU ===")
      print(f"Cœurs physiques : {psutil.cpu_count(logical=False)}")
      print(f"Cœurs logiques : {psutil.cpu_count(logical=True)}")
      print(f"Utilisation du CPU : {cpu_percent}%")

def memoire():
    mem = psutil.virtual_memory()
    print("=== Mémoire ===")
    print(f"Mémoire totale : {mem.total / (1024 ** 3):.2f} Go")
    print(f"Mémoire disponible : {mem.available / (1024 ** 3):.2f} Go")
    print(f"Pourcentage utilisé : {mem.percent}%")

def disque():
    disque = psutil.disk_partitions(all=True)
    print("=== Disques ===")
    for partition in disque:
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"{partition.mountpoint} : {usage.percent} %")


systeme()
cpu()
memoire()
disque()