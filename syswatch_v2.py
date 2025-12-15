from collector import collecter_tout

def affichage(data_systeme):
    print("=== SYSTÈME ===")
    print(f"Système d'exploitation : {data_systeme['os']}")
    print(f"Version               : {data_systeme['version']}")
    print(f"Architecture           : {data_systeme['architecture']}")
    print(f"Nom de la machine      : {data_systeme['hostname']}")

def afficher_cpu(data_cpu):
    print("=== CPU ===")
    print(f"Cœurs physiques : {data_cpu['coeurs_physiques']}")
    print(f"Cœurs logiques  : {data_cpu['coeurs_logiques']}")
    print(f"Utilisation CPU : {data_cpu['utilisation']} %")

def afficher_memoire(data_memoire):
    print("=== MÉMOIRE ===")
    print(f"Mémoire totale      : {octets_vers_go(data_memoire['total'])}")
    print(f"Mémoire disponible  : {octets_vers_go(data_memoire['disponible'])}")
    print(f"Utilisation mémoire : {data_memoire['pourcentage']} %")

def afficher_disques(data_disques):
    print("=== DISQUES ===")
    for disque in data_disques:
        print(f"Point de montage : {disque['point_montage']}")
        print(f"  Total     : {octets_vers_go(disque['total'])}")
        print(f"  Utilisé   : {octets_vers_go(disque['utilise'])}")
        print(f"  Utilisation : {disque['pourcentage']} %")

def octets_vers_go(octets):
    return f"{octets / (1024 ** 3):.2f} GB"


def main():
    donnees = collecter_tout()

    print("=== SysWatch v2.0 ===\n")

    affichage(donnees["systeme"])
    afficher_cpu(donnees["cpu"])
    afficher_memoire(donnees["memoire"])
    afficher_disques(donnees["disques"])

main()