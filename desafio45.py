from random import randint # Importando sorteador na biblioteca random
print("Olá, perdedor! Vamos jogar jokenpô?")
print("-=" * 30)

jogadas = ("Pedra", "Papel", "Tesoura") # Opções de jogadas do computador
computador = randint(0, 2) # Sorteando número que será sua jogada

print("Vamos começar então.") 
print("Qual será sua primeira jogada?")
print("[ 1 ] Pedra") 
print("[ 2 ] Papel")
print("[ 3 ] Tesoura")
escolha = int(input("Qual é a sua jogada? ")) # Receber jogada do usuário

while escolha != 1 and escolha != 2 and escolha != 3: # Aceitar apenas uma opção válida
    print("Deixa de ser frouxo! Escolha uma das 3 opções logo!!!")
    escolha = int(input("Escolha sua jogada: "))

if escolha == 1:
    escolha = "Pedra"
elif escolha == 2:
    escolha = "Papel"
elif escolha == 3:
    escolha = "Tesoura"

print("-=" * 30)

print(f"Computador jogou {jogadas[computador]}")
print(f"Jogador jogou {escolha}")

if escolha == jogadas[computador]:
    print("Que sorte, o jogo empatou!")

if jogadas[computador] == "Pedra":
    if escolha == "Papel":
        print(f"Parabéns vencedor! {escolha} ganha da {jogadas[computador]}")
    elif escolha == "Tesoura":
        print(f"KAKAKAKAKAKA Otário! {escolha} perde para {jogadas[computador]}")

if jogadas[computador] == "Papel":
    if escolha == "Pedra":
        print(f"KAKAKAKAKAKA Otário! {escolha} perde para {jogadas[computador]}")
    elif escolha == "Tesoura":
        print(f"Parabéns vencedor! {escolha} ganha do {jogadas[computador]}")

if jogadas[computador] == "Tesoura":
    if escolha == "Pedra":
        print(f"Parabéns vencedor! {escolha} ganha da {jogadas[computador]}")
    elif escolha == "Papel":
        print(f"KAKAKAKAKAKA Otário! {escolha} perde para {jogadas[computador]}")

print("-=" * 30)