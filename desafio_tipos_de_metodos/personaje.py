class Personaje ():
    # Metodo Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    # Getter
    @property
    def nombre(self):
       return self.__nombre
    
    @property
    def nivel(self):
        return self.__nivel
    
    @property
    def experiencia(self):
        return self.__experiencia
    
     #Setter
    @nombre.setter
    def nombre(self,nuevo_nombre: str):
        self.__nombre = nuevo_nombre
    
    @nivel.setter
    def nivel(self,nuevo_nivel: int):
        self.__nivel = nuevo_nivel
    
    @experiencia.setter
    def experiencia(self,nueva_experiencia: int):
        self.__experiencia = nueva_experiencia
    
    #Getter de estado
    @property
    def estado(self):
        return f'NOMBRE: {self.nombre}   NIVEL: {self.nivel}    EXPERIENCIA: {self.experiencia}'
    #Setter de estado
    @estado.setter
    def estado(self, nueva_experiencia: int):
        self.experiencia += nueva_experiencia
        #Se incorpora la logica de calculo del estado de los personajes por refactorizacion del codigo
        if self.experiencia < 0 and self.nivel <= 1:
            self.experiencia = 0
        elif self.experiencia < 0 and self.nivel > 1:
            self.nivel -= 1
            self.experiencia += 100
        elif self.experiencia >= 100:
            self.nivel +=1
            self.experiencia -= 100
            
    #Sobrecarga metodo operador 'menor que'
    def __it__(self, other):
        return self.nivel < other.nivel
    #Sobrecarga metodo operador 'mayor que'
    def __gt__(self, other):
        return self.nivel > other.nivel
    #Sobrecarga metodo operador 'menor que'
    def __eq__(self, other):
        return self.nivel == other.nivel
    
    #Metodo no estatico que retorna la probabilidad de ganar
    def probabilidad(self, enemigo):
        if Personaje.__gt__(self, enemigo):
            return 0.66
        elif Personaje.__eq__(self, enemigo):
            return 0.50
        elif Personaje.__it__(self, enemigo):
            return 0.33
        
    # Metodo que muestar dialogo de enfrentamiento al orco. Retorna opcion de juego
    @staticmethod
    def dialogo(probabilidad):
        print(f'Con tu nivel actual, tienes {probabilidad*100}% de probabilidad de ganarle al orco.')
        print("")
        print(f'Si ganas, ganaras 50 puntos de experiencia y el orco perdera 30.')
        print('')
        print(f'Si pierdes, perderas 30 puntos de experiencia y el orco ganara 50.')
        opcion = int(input("¿Que deseas hacer?, 1. Atacar 2. Huir"))
        return opcion
        
      