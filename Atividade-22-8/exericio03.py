import random

opcoes_do_jogo = ["pedra", "papel", "tesoura"]

jogador = input("Escolha uma opção (pedra, papel ou tesoura): ")

if jogador not in opcoes_do_jogo:
    resultado = ("Opção inválida. Tente novamente")
    
outro_jogador = random.choice(opcoes_do_jogo)

if jogador == outro_jogador:
        resultado = ("Empate")
elif (
    (jogador == "pedra" and outro_jogador == "tesoura") or \
    (jogador == "tesoura" and outro_jogador == "papel") or \
    (jogador == "papel" and outro_jogador == "pedra")
):
       resultado = ("Você ganhou!")
else:
    resultado = (outro_jogador, "Venceu!")
    
    
    print(f"Você escolheu: {jogador}")
    print(f"O computador escolheu: {outro_jogador}")
    print(f"Resultado: {resultado}")
