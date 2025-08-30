# Cadastro e Análise de Idades 
# Crie um programa que peça ao usuário para digitar idades continuamente. Cada idade
# digitada deve ser armazenada em uma lista. O laço deve parar quando o usuário digitar -1. 
# No final, percorra a lista e diga quantas pessoas são maiores de idade (idade >= 18). 

lista = [] #Criar uma lista vazia para armazenar as idades

while True: #Usar um laço para pedir ao usuário as idades continuamente até ele digitar -1
    idade = int(input("Digite a sua idade (ou -1 para sair): "))
    if idade == -1:
        break  #Se o usuário digitar -1, ele encerra o laço

    lista.append(idade)  #Se a idade digitada não for -1, será adicionada à lista.
    print(lista) # opcional

    maior_de_idade = 0 #variável para contar maiores de idade

    for idade in lista:
        if idade >= 18:
            print(f"{idade} é maior de idade")
            maior_de_idade = maior_de_idade + 1 # toda vez que uma idade igual/maior de 18 for encontrada na lista
            #(dentro do laço for) o contador é incrementado em 1. ou seja, ele vai contar quantas 
            # pessoas são maiores de idade.

print(f"Total de pessoas maiores de idade: {maior_de_idade}") #Exibir o resultado
