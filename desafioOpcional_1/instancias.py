from te import Te

te_negro = Te()
te_verde = Te()

if type(te_negro) == type(te_verde):
    print(type(te_negro))
    print("Ambos tipos son iguales")
else:
    print("Ambos no son iguales") 
  