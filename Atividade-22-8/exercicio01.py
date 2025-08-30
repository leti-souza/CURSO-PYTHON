cardapio_python = {
    1: ("Hambúrguer", 25.00),
    2: ("Batata Frita", 15.00),
    3: ("Refrigerante", 8.00)
}
print("Bem-vindo ao Restaurante LSPython!","=== Cardápio ===")
for codigo, (item, preco) in cardapio_python.items():
    print(f"{codigo} - {item} - R${preco:.2f}")

faca_sua_escolha = int(input("Digite o número do item desejado: "))

if faca_sua_escolha in cardapio_python:
    nome_item, preco_item = cardapio_python[faca_sua_escolha]
    print(f"Você escolheu: {nome_item} que custa R$ {preco_item:.2f}")
    #print(f"Você escolheu: {cardapio_python[faca_sua_escolha]}")
else:
    print("Opção inválida.")