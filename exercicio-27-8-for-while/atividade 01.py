# Contagem Regressiva de Ímpares 
# Peça ao usuário para digitar um número inteiro positivo. Em seguida, use um 
# laço for para fazer uma contagem regressiva a partir desse número até 1. O 
# programa deve imprimir apenas os números ímpares encontrados nesse intervalo. 

seu_numero = int(input("Digite um número inteiro positivo: ")) # Solicitar ao usuário para digitar um número
print( seu_numero)

#Faz a contagem regressiva do numero digitado pelo usuário até 1 (não inclui 0), decrementando/eliminando de 1 em 1
for i in range(seu_numero, 0, -1): 
    if i % 2 != 0: #Verifica se o número é ímpar
        print(i)
        
#O operador módulo (%) em Python calcula o resto da divisão de dois números.
#Ex: 5 % 2 = 1 (porque o resto da divisão de 5 por 2 é 1)

#O que significa n % 2 != 0?

# A expressão n % 2 != 0.
# n % 2: calcula o resto da divisão de n por 2.
# != 0: significa "diferente de 0", ou seja, verifica se o resto da divisão é diferente de 0.