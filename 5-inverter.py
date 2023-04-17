# Exercício 5

# basta percorrer a string normal começando pelo final e adicionar cada caractere à nova string vazia invertida.

normal = str(input("Digite a palavra que quiser: "))

invertida = ''

for i in range(len(normal)-1, -1, -1):
    invertida += normal[i]

print('String original:', normal)
print('String invertida:', invertida)