# Grupo 3: Jocelyn Centero - Lolett Llanquinao - Juan Torres - Leonardo Llaupe - Claudio Méndez

"""
1. Crear un archivo script.py que permita leer línea a línea el archivo usuarios.txt, y crear
una instancia de Usuario a partir de los datos de cada línea leída.
2. En el mismo archivo, manejar las posibles excepciones al leer cada línea y/o generar
cada instancia, y agregar la excepción en un archivo error.log.
    """
    
import json
from usuario import Usuario
from datetime import datetime
lista_usuarios = []
log_error = open('error.log', 'a+')
now = datetime.now()
# Leer línea a línea el archivo usuarios.txt, y crear
# una instancia de Usuario a partir de los datos de cada línea leída
with open("desafios/desafio_5/usuarios.txt") as usuarios:
    linea = usuarios.readline()
    while linea:
        try:
            usuario = json.loads(linea)
            lista_usuarios.append(Usuario(usuario.get("nombre"), usuario.get("apellido"), usuario.get("email"), usuario.get("genero")))
        except json.decoder.JSONDecodeError as e:
            log_error.write(f"[{now.strftime('%d-%m-%Y %H:%M:%S')}] ERROR: {e}\n")
        finally:
            linea = usuarios.readline()
usuarios.close()        
for usuario in lista_usuarios:
    print(f'{usuario.nombre}  {usuario.apellido}  {usuario.email}  {usuario.genero}')
    
    #with open(os.path.abspath("dia12/usuarios.txt")) as usuarios: