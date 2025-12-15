from collector import collecter_tout

donnees = collecter_tout()

def afficher_tout():
    donnees = collecter_tout()
    print("=== SysWatch v2.0 ===")
    print(f"Timestamp : {donnees['timestamp']}\n")
    print("Système :", donnees["systeme"])
    print("CPU :", donnees["cpu"])
    print("Mémoire :", donnees["memoire"])
    print("Disques :", donnees["disques"])

afficher_tout()