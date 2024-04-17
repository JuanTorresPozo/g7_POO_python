from te import Te

te_negro = Te()
te_verde = Te()
agua_de_hierba = Te()
"""
te_negro.infusion = "3 minutos"
te_verde.infusion = "5 minutos"
agua_de_hierba.infusion = "6 minutos"

te_negro.recomendacion = "consumir en el desayuno"
te_verde.recomendacion = "consumir al mediodia"
agua_de_hierba.recomendacion = "Consumir en la tarde"
"""
sabor = int(input(""" Ingrese el tipo de te que desea pedir: [1, 2 o 3]
                  1) Té negro
                  2) Té Verde
                  3) Agua de hierbas
                  """))
gramaje = int(input("""¿Cuantos gramos desea pedir?: [1 o 2]
                    1) 300 gramos
                    2) 500 gramos
                    """))

print(Te.especificaciones(sabor))
print(f"el precio para esta cantidad de gramos es de {Te.precio_gramaje(gramaje)} pesos")