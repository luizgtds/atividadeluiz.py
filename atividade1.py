def substituir_vogal():    
    texto = input("Insira uma frase:")
    return texto.lower().replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')
    
print(substituir_vogal())