def nome_composto():
    nome = input("Insira seu primeiro nome: ")
    sobrenome = input("Insira seu segundo nome: ")
    return nome.upper(), sobrenome.lower()

print(nome_composto())