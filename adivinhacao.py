import random
numero_secreto = 7
chute = int(input("Escolha um número de 1 a 10: "))
print(f"Você escolhou o número: {chute}")

if chute == numero_secreto:
    print("Você acertou!")
elif chute > numero_secreto:
    print("Você errou! Tente um número menor")
else:
    print("Você errou! Tente um número maior")