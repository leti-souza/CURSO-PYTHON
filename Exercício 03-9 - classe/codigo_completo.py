print("Bem-vindos ao Cinema UTEC!")

from datetime import datetime # Módulo para trabalhar com datas
hoje = datetime.today().weekday() # Verifica se hoje é quarta-feira (0 = segunda, 1 = terça, 2 = quarta)
quarta_promocao = hoje == 2

# Define os preços dos ingressos
preco_normal, preco_meia = (10.00, 10.00) if quarta_promocao else (30.00, 15.00)

# Se o programa RODAR em uma quarta-feira, os preços serão automaticamente ajustados para R$10,00.

# Atualiza os totais gerais
total_ingressos_vendidos = 0
valor_total_vendas = 0.0

while True:
    # Pergunta a quantidade de ingressos
    qtd = int(input("\nQuantos ingressos deseja comprar? "))

    total = 0.0  # total apenas dessa venda

    if qtd > 1:
        # Para mais de um ingresso, pergunta quantos são crianças e estudantes
        qtd_criancas = int(input("Quantos desses ingressos são para crianças (até 12 anos)? "))
        while qtd_criancas > qtd or qtd_criancas < 0:
            print("Quantidade inválida. Tente novamente.")
            qtd_criancas = int(input("Quantos desses ingressos são para crianças (até 12 anos)? "))

        qtd_restante = qtd - qtd_criancas

        qtd_estudantes = int(input("Quantos dos restantes são para estudantes com carteira válida? "))
        while qtd_estudantes > qtd_restante or qtd_estudantes < 0:
            print("Quantidade inválida. Tente novamente.")
            qtd_estudantes = int(input("Quantos dos restantes são para estudantes com carteira válida? "))

        qtd_adultos = qtd - qtd_criancas - qtd_estudantes

        # Calcula os valores
        total += qtd_criancas * preco_meia
        total += qtd_estudantes * preco_meia
        total += qtd_adultos * preco_normal

        # Mostra o resumo parcial
        print(f"\nIngressos infantis (R${preco_meia:.2f}): {qtd_criancas}")
        print(f"Ingressos de estudantes (R${preco_meia:.2f}): {qtd_estudantes}")
        print(f"Ingressos normais (R${preco_normal:.2f}): {qtd_adultos}")

    else:
        # Venda unitária: faz as perguntas individualmente
        idade = int(input("Por favor, digite a idade do cliente: "))

        if idade <= 12:
            preco = preco_meia
            print(f"Preço infantil, valor: R$ {preco:.2f}")
        else:
            estudante = input("Você é estudante com carteira válida? (S/N): ").strip().lower()
            if estudante == "s":
                preco = preco_meia
                print(f"Preço estudante, valor: R$ {preco:.2f}")
            else:
                preco = preco_normal
                print(f"Preço normal / Adulto, valor: R$ {preco:.2f}")

        total += preco

    # Atualiza os totais gerais
    total_ingressos_vendidos += qtd
    valor_total_vendas += total

    # Resumo da compra
    print("\n=== Resumo da Compra ===")
    print(f"Quantidade de ingressos: {qtd}")
    print(f"Total a pagar: R$ {total:.2f}")

    # Pergunta se deseja nova venda
    nova_venda = input("\nDeseja registrar uma nova venda? (S/N): ").strip().lower()
    if nova_venda != "s":
        break

# Encerramento
print("\n=== Fim de expediente ===")
print(f"Total de ingressos vendidos: {total_ingressos_vendidos}")
print(f"Valor total das vendas: R$ {valor_total_vendas:.2f}")