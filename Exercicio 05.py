cotação_do_Dolar = 5.25
# valor fixo da cotação do dolar

Valor_Real = float(input("Digite um valor em Reais (R$):"))
# valor digitado pelo usuario em Reais

Valor_em_Dolares = Valor_Real / cotação_do_Dolar
# converte o valor em Reais em Dolar

print(f"O valor de R$: {Valor_Real} equivale a US$: {Valor_em_Dolares:.4f}")
# exibi o valor do resultado