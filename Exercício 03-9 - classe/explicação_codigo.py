# Cabeçalho: Exibe uma mensagem de boas-vindas.
  # *print("Bem-vindos ao Cinema UTEC!")*
  
 # Módulo para trabalhar com datas:
   # from datetime import datetime
   # hoje = datetime.today().weekday() -> Verifica se hoje é quarta-feira (0 = segunda, 1 = terça, 2 = quarta)
   # quarta_promocao = hoje == 2

 # Define os preços dos ingressos:
   # preco_normal, preco_meia = (10.00, 10.00) if quarta_promocao else (30.00, 15.00)

# Se o programa RODAR em uma quarta-feira, os preços serão automaticamente ajustados para R$10,00.
  
# Variáveis de controle: Inicializa as variáveis para rastrear o total de ingressos vendidos 
# e o valor total das vendas.
  # *total_ingressos_vendidos = 0*
  # *valor_total_vendas = 0.0*

# Loop principal: Inicia um loop infinito permitindo várias vendas, até o usuário decidir encerrar.
    # *while True:*

# Entrada de dados: quantidade de ingressos e o total da venda atual
# Solicita ao usuário a quantidade de ingressos que ele deseja comprar.
    # *qtd = int(input("\nQuantos ingressos deseja comprar? "))*

# Inicializa o total da venda atual
    # *total = 0.0* 
    
# Venda múltipla: Se a quantidade de ingressos for maior que um (1):
# solicita quantidade de ingressos para crianças e estudantes, calcula o total com base nessas categorias abaixo: 
    # *if qtd > 1:*
        # *qtd_criancas = int(input("Quantos desses ingressos são para crianças (até 12 anos)? "))*
        # *qtd_restante = qtd - qtd_criancas*
        
        # *qtd_estudantes = int(input("Quantos dos restantes são para estudantes com carteira válida? "))*
        # *qtd_adultos = qtd - qtd_criancas - qtd_estudantes*
        
        # Calcula o "Total" da venda atual com base nas categorias usadas:
          # *total += qtd_criancas * preco_meia*  -> total = total + (qtd_criancas * preco_meia)
          # *total += qtd_estudantes * preco_meia*  -> total = total + (qtd_estudantes * preco_meia)
          # *total += qtd_adultos * preco_normal*  -> total = total + (qtd_adultos * preco_normal)

        # Exibe um resumo parcial da venda.
        # *print(f"\nIngressos infantis (R${preco_meia:.2f}): {qtd_criancas}")*
        # *print(f"Ingressos de estudantes (R${preco_meia:.2f}): {qtd_estudantes}")*
        # *print(f"Ingressos normais (R${preco_normal:.2f}): {qtd_adultos}")*

# Venda unitária: Se for apenas 1 ingresso:
   # else:
        # *idade = int(input("Por favor, digite a idade do cliente: "))*
    # Se a idade for menor ou igual a 12 anos, aplica o preço infantil.
          # *if idade <= 12:*
              # *preco = preco_meia*
              # *print(f"Preço infantil, valor: R$ {preco:.2f}")*
              
     # Se a idade for maior que 12 anos, pergunta se é estudante.
          # *else:*
              # *estudante = input("Você é estudante com carteira válida? (S/N): ").strip().lower()*
               # *if estudante == "s":*
                    # *preco = preco_meia*
                    # *print(f"Preço estudante, valor: R$ {preco:.2f}")*
                # *else:*
                    # *preco = preco_normal*
                    # *print(f"Preço normal / Adulto, valor: R$ {preco:.2f}")*
                # *total += preco*  -> total = total + preco
                
# Atualiza os totais gerais com os valores da venda atual.
  # *total_ingressos_vendidos += qtd*  -> total_ingressos_vendidos = total_ingressos_vendidos + qtd*
  # *valor_total_vendas += total*  -> valor_total_vendas = valor_total_vendas + total*
  
# Resumo da compra: Exibe um resumo da compra atual, incluindo a quantidade de ingressos e o total a pagar.
    # *print("\n=== Resumo da Compra ===")*
    # *print(f"Quantidade de ingressos: {qtd}")*
    # *print(f"Total a pagar: R$ {total:.2f}")*
    
# Nova venda: Pergunta ao usuário se o mesmo deseja registrar uma nova venda.
    # *nova_venda = input("\nDeseja registrar uma nova venda? (S/N): ").strip().lower()*
    # *if nova_venda == "s":*
        # *continue*  -> reinicia o loop principal (while True)
        
    # OUTRA FORMA DE FAZER:
        # if nova_venda != "s": -> != significa "diferente de:" neste caso:"s"
         #   break - encerra o loop e finaliza o programa.
    # *else:*
        # *print("\n=== Resumo das Vendas ===")*
        # *print(f"Total de ingressos vendidos: {total_ingressos_vendidos}")*
        # *print(f"Valor total das vendas: R$ {valor_total_vendas:.2f}")*
        # *break*