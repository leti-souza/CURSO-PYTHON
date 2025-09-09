print("Bem-vindos ao Cinema UTEC!")

# Pergunta a quantidade de ingressos
quantd = int(input("Quantos ingressos deseja comprar? "))

# Pergunta se é estudante
estudante = input("Você é estudante com carteira válida? (S/N): ").strip().lower()

#idade = int(input("Por favor, digite sua idade: "))

total = 0.0

for i in range(1, quantd + 1):
    print(f"\nIngresso {i}:")
    idade = int(input("Por favor, digite sua idade: "))

    if idade <= 12:
        preco = 15.00
        print(f"Preço infantil, valor: R$ {preco:.2f}")
    elif estudante == "s":
        preco = 15.00
        print(f"Preço estudante, valor: R$ {preco:.2f}")
    else:
        preco = 30.00
        print(f"Preço normal / Adulto, valor: R$ {preco:.2f}")

    total += preco

print("\n=== Resumo da Compra ===")
print(f"Quantidade de ingressos: {quantd}")
print(f"Total a pagar: R$ {total:.2f}")