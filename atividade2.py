def quantidade_caracteres():
    palavra = input("Insira uma palavra:")
    return len(palavra)

print("Essa palavra tem " + str(quantidade_caracteres()) + " caractéres.")