# Média de Notas em uma Lista 
# Você recebeu uma lista de notas: notas = [8.5, 9.0, 6.5, 10.0, 7.5]. Use um laço for 
# para calcular a soma total das notas. Após o laço, calcule e imprima a média da turma. 

notas_turma = [8.5, 9.0, 6.5, 10.0, 7.5]
soma = 0

for nota_na_lista in notas_turma:
    soma += nota_na_lista  #Soma cada nota da lista à variável "soma"
    print(soma) # opcional
    
media = soma / len(notas_turma)  #Calcula a média dividindo a soma pelo número de notas na lista
print(f"A media total da turma é: {media}")