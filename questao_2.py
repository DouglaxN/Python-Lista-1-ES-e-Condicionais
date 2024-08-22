#Francisco ingressou na universidade e em uma disciplina do primeiro 
#semestre obteve nota N1 na primeira unidade, nota N2 na segunda unidade e 
#nota N3 na terceira unidade. Ele não conhece bem as regras de pontuação e, 
#portanto, precisa de ajuda para saber se está aprovado, reprovado ou em prova 
#final nesta disciplina. A nota final de Francisco é calculada utilizando uma média 
#ponderada na qual o peso da nota N1 é 2, o peso da nota N2 é 3 e o peso da nota N3 é 4. 
#Caso a média final seja maior ou igual a 7, Francisco está aprovado. 
#Caso a média seja menor que 3, Francisco está reprovado. Em caso contrário, terá que fazer a prova final. 
#Para isso, faça um programa para imprimir qual é a situação de Francisco a partir de três notas 
#informadas.

nota_1 = float(input("Digite a nota da primeira unidade (N1): "))
nota_2 = float(input("Digite a nota da segunda unidade (N2): "))
nota_3 = float(input("Digite a nota da terceira unidade (N3): "))

media_final = (nota_1 * 2 + nota_2 * 3 + nota_3 * 4)/9

if media_final >= 7:
    situacao = "Aprovado"

elif media_final <= 3:
    situacao = "Reprovado"

else:
    situacao = "em prova final"

print(f"Francisco está {situacao}, ")