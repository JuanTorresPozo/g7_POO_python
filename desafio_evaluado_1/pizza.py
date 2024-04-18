from ingredientes import lista_masa, lista_proteicos, lista_vegetales
class Pizza():
    tamaño = "familiar"
    precio = 10000
    
    @staticmethod
    def validacion(elemento,valores_posibles):
        elemento in valores_posibles
        #for valor in valores_posible:
            #if valor == elemento:
                #return True
        #return False
        return elemento in valores_posibles
        
    
    def tomar_pedido(self):
        self.proteico = input("Ingrese un ingrediente proteico:\n Vacuno\n Pollo\n Carne Vegetal\n").lower()
        ()
        self.vegetales = []
        self.vegetales.append(input("Ingrese primer ingrediente vegetal:\n Tomate\n Aceitunas\n Champiñon\n").lower())
        ()
        self.vegetal2 = input("Ingrese segundo ingrediente vegetal:\n Tomate\n Aceitunas\n Champiñon\n").lower()
        ()
        self.masa = input("Ingrese tipo de masa:\n Tradiciona\n Delgada\n").lower()
        ()
        self.es_pizza_valida = self.validacion(self.proteico, lista_proteicos) and \
        self.validacion(self.vegetales[0], lista_vegetales) and \
        self.validacion(self.vegetal2, lista_vegetales) and \
        self.validacion(self.masa, lista_masa)
