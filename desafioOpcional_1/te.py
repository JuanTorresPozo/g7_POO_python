class Te():
    formato = [300,500]
    duracion = "1 año"
    infusion = ""
    recomendacion = ""
    
    @staticmethod
    def especificaciones(num:int):
        if num == 1:
            print("las especificaciones para el te negro son las siguientes: "),
            Te.infusion = "3 minutos",
            print(f"El tiempo de infusion es de {Te.infusion}."),
            Te.recomendacion ="consumir en el desayuno.",
            print(f"se recomienda{Te.recomendacion}."),
            print(f"Recuerde consumir antes de{Te.duracion}.")
        elif num == 2:
            print("las especificaciones para el te verde son las siguientes: "),
            Te.infusion = "5 minutos",
            print(f"El tiempo de infusion es de {Te.infusion}."),
            Te.recomendacion ="consumir al mediodia.",
            print(f"se recomienda{Te.recomendacion}."),
            print(f"Recuerde consumir antes de{Te.duracion}.")
        elif num == 3:
            print("las especificaciones para el agua de hierva son las siguientes: "),
            Te.infusion = "6 minutos",
            print(f"El tiempo de infusion es de {Te.infusion}."),
            Te.recomendacion ="consumir al atardecer.",
            print(f"se recomienda{Te.recomendacion}."),
            print(f"Recuerde consumir antes de{Te.duracion}.")
    

    @staticmethod
    def precio_gramaje(num:int):
        if num == 1:
            precio = 3000
        elif num == 2:
            precio = 5000
        return precio

if __name__ == "__main__":
        (Te.especificaciones(1))
        print (Te.precio_gramaje(2))

