nome = str(input('Digite o seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
nome = nome.split()
print(len(nome[0]))