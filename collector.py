import platform
import psutil
from datetime import datetime

def collecter_info_systeme():
    return {
        "os": platform.system(),
        "version": platform.version(),
        "architecture": platform.architecture()[0],
        "hostname": platform.node()
    }

def collecter_cpu():
    return {
        "coeurs_physiques": psutil.cpu_count(logical=False),
        "coeurs_logiques": psutil.cpu_count(logical=True),
        "utilisation": psutil.cpu_percent(interval=1)
    }

def collecter_memoire():
    mem = psutil.virtual_memory()
    return {
        "total": mem.total,
        "disponible": mem.available,
        "pourcentage": mem.percent
    }

def collecter_disques():
    partitions = psutil.disk_partitions(all=True)
    liste_disques = []

    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disque_info = {
            "point_montage": partition.mountpoint,
            "total": usage.total,
            "utilise": usage.used,
            "pourcentage": usage.percent
        }
        liste_disques.append(disque_info)
    return liste_disques

from datetime import datetime

def collecter_tout():
    return {
        "timestamp": datetime.now().isoformat(),
        "systeme": collecter_info_systeme(),
        "cpu": collecter_cpu(),
        "memoire": collecter_memoire(),
        "disques": collecter_disques()
    }


collecter_info_systeme()
collecter_cpu()
collecter_memoire()
collecter_disques()
collecter_tout()