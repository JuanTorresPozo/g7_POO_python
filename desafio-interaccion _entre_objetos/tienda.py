from abc import ABC, abstractmethod # para poder trabajar con clase y metodo abstactos

#clase abstarcta-> planilla para crear subclases(clases hijas)
#a lo menos debe tener un metodo abstracto

class Tienda(ABC):
    #metodo abstacto->es SOLO la definicion del metodo(no hace NADA)
    @abstractmethod
    def imprimir(self):
        pass

class Restaurant(Tienda):#herencia
    
    #obligado de implementar en la clase hija
    def imprimir(self):
        pass
    
    #metodo de instancia llamado constructor
    def __init__(self, parametro_nombre = "", parametro_costo = 0, parametro_productos = []):
        #definir variables de instancia
        self.__nombre = parametro_nombre
        self.__costo = parametro_costo
        self.__productos = parametro_productos
        
    #getter(acceder al valor)   
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def costo(self):
        return self.__costo
    
    @property
    def productos(self):
        return self.__productos
    
    #setter  (modifica el valor)
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor    
    
    
        
if __name__ == "__main__":
    #instancia de clase u objeto
    objeto_restobar = Restaurant('Pink',10000)
    print(objeto_restobar.costo)
    print(objeto_restobar.nombre)
  
    objeto_restolunch = Restaurant()
    print(objeto_restolunch.costo)
    objeto_restolunch.nombre= 'Cerebro'
    print(objeto_restolunch.nombre)
   