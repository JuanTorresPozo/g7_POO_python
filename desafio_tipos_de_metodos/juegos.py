# Importacion de modulos necesarios para el desarrollo del juago
import os, sys, random
from personaje import Personaje

clear = 'cls' if sys.platform == 'win32' else 'clear'
os.system(clear)

print('Bienvenido a Gran Fantasia')
#Creacion del personajes
name =input("Por favor indique nombre del personaje:\n")
person = Personaje(name)
orco = Personaje('Orco')
#visualisacion de consola del estado de los personajes
print(person.estado)
print("¡Ha aparecido un Orco!")
# Se llama al metodo dialogo para visualizar dialogos e ingresar al juego
opt = person.dialogo(person.probabilidad(orco))
#Mecanica del juego segun opciones ingresadas por el jugador
while opt == 1:
    aleatorio = random.uniform(0, 1)
    if aleatorio <= person.probabilidad(orco):
        print('Le ha ganado al Orco, felicidades')
        print('Recibiras 50 puntos de experiencia ')
        person.estado = 50
        orco.estado = -30
    else:
        print('El Orco ha ganado')
        print('Has perdido 30 puntos de experiencia' )
        person.estado = -30
        orco.estado = 50
        
    print(person.estado)
    print(orco.estado)
    opt = person.dialogo(person.probabilidad(orco))
    os.system(clear)
    


