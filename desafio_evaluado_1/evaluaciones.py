from pizza import Pizza

print(f"El valor de la pizza es ${Pizza.precio} y su tamaño es {Pizza.tamaño}")
print(Pizza.validacion("salsa de tomate",["salsa de tomate", "salsa bbq"]))

pizza = Pizza()
pizza.tomar_pedido()

if pizza.es_pizza_valida:
    print(f"ingrediente proteico: {pizza.proteico}")
    print(f"Ingrediante vegetales: {pizza.vegetales[0]} - {pizza.vegetal2}")
    print(f"La masa seleccionada es {pizza.masa}")
else:
    print("La pizza no es valida")
 