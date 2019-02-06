#!/usr/bin/env python3

import os
import sys

direccion = os.getcwd()
for i in sys.argv[1:]:
    try:
        os.mkdir(i)
        os.chdir(i)
        with open("base.py", "w") as f:
            f.write("#!/usr/bin/env python3\n\n")
            f.write("# Escrito por: Juan Carlos 1987\n")
            f.write("# Correo: k.juno.1987@gmail.com\n")
            f.write("# \n")
        os.chdir(direccion)
        print(f"El archivo {i} se creo correctamente")
    except:
        print("Ocurrio alun problema")
    
