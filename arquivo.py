def cumprimento():
    texto = input("Digite o seu nome: ")
    return f"Olá, {texto}"

print(cumprimento())

import random

def media_numeros_aleatorios():
    numeros = [random.randint(1, 100) for _ in range(3)]
    media = sum(numeros) / len(numeros)
    return numeros, media

numeros_sorteados, media = media_numeros_aleatorios()
print(f"Números sorteados: {numeros_sorteados}")
print(f"Média: {media}")
