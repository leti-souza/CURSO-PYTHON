# Jogo de Adivinhação
# Crie um "jogo de adivinhação". Defina um número secreto no código (por exemplo, 42).
# Peça para o usuário adivinhar o número. O laço deve continuar
# até que o usuário acerte. A cada tentativa errada, dê uma dica se o palpite foi
# "muito alto" ou "muito baixo".

numero_secreto = 42  # numero definindo para o usuario adivinhar

while True:
    adivinha = int(input("Digite seu palpite: "))
    print(adivinha)

    if adivinha < numero_secreto:
        print("Muito baixo! Tente novamente")
    elif adivinha > numero_secreto:
        print("Muito alto! Tente novamente")
    else:
        print("Parabéns! Você acertou!")
        break
