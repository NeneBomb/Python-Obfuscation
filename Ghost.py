import hashlib
import random
import string
import os
import subprocess

def analizar_entorno():
    puntos = 0
    
    try:
        with open("/proc/meminfo", "r") as f:
            for linea in f:
                if "MemTotal" in linea:
                    if int(linea.split()[1]) < 4000000:
                        puntos += 1
                    break
    except:
        pass

    try:
        cores = os.cpu_count()
        if cores and cores < 2:
            puntos += 1
    except:
        pass

    drivers_vm = [
        "/usr/bin/vbox-control",
        "/usr/sbin/VBoxService",
        "/proc/scsi/vbox",
        "/sys/module/vmwgfx"
    ]
    for driver in drivers_vm:
        if os.path.exists(driver):
            puntos += 1
            break

    return puntos >= 2

def calcular_hash():
    sha256 = hashlib.sha256()
    with open(__file__, "rb") as f:
        sha256.update(f.read())
    return sha256.hexdigest()

def mutar():
    junk = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    with open(__file__, "r") as f:
        lineas = f.readlines()
    
    if lineas and lineas[-1].startswith("# JUNK:"):
        lineas[-1] = f"# JUNK: {junk}"
    else:
        lineas.append(f"\n# JUNK: {junk}")
    
    with open(__file__, "w") as f:
        f.writelines(lineas)
    print(f"[+] Mutacion completada.")

if __name__ == "__main__":
    is_sandbox = analizar_entorno()
    
    if is_sandbox:
        print("[!] Alerta: Se ha detectado un entorno de sandbox.")
    else:
        print("[*] Entorno verificado: Usuario real.")

    print(f"[*] Hash actual: {calcular_hash()}")
    if input("[?] Mutar? (s/n): ").lower() == 's':
        mutar()
        print(f"[*] Nuevo Hash: {calcular_hash()}")

# JUNK: Gf7C6Yn9Xo2Pq4Wz
