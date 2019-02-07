#!/usr/bin/env python3

import os
import sys
from datetime import datetime

direccion = os.getcwd()
fecha = str(datetime.now())
for i in sys.argv[1:]:
    try:
        os.mkdir(i)
        os.chdir(i)
        with open("base.py", "w") as f:
            f.write("#!/usr/bin/env python3\n\n")
            f.write(f"# Base para el programa {i}\n")
            f.write("# Escrito por: Juan Carlos 1987\n")
            f.write("# Correo: k.juno.1987@gmail.com\n")
            f.write(f"# Fecha: {fecha}\n")
            f.write("# \n")
        os.chdir(direccion)
        print(f"El archivo {i} se creo correctamente")
    except:
        print("Ocurrio alun problema")
        print(f"la carpeta {i} ya existe")
    
