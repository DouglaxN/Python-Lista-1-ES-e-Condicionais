#Muitas vezes na computação, precisamos de algoritmos para resolver problemas 
#envolvendo representações geométricas, seja nos jogos, mapas ou outras aplicações que
#utilizam essas formas. Um dos problemas mais comuns é saber se um ponto ou não está dentro 
#ou fora de um polígono. Dependendo do cenário, isso pode ficar mais complexo.

#Nesse problema, vocês vão apenas verificar se um ponto está dentro de um retângulo ou não. 
#Seu programa lerá dois pares de valores inteiros representando a coordenada de dois pontos em um 
#retângulo: o valor do canto esquerdo seperior e o valor do canto direito inferior. Em seguida ele 
#lerá dois inteiros representando a coordenada de um ponto qualquer. 
#Seu programa deve imprimir se esse ponto está dentro ou fora da área delimitada pelo retângulo.
 
print("Valores do canto esquerdo superior")
x1 = int(input())
y1 = int(input())

print("Valores do canto direito inferior: ")
x2 = int(input())
y2 = int(input())

print("Coordenada do ponto: ")
x = int(input())
y = int(input())

if x1<= x <= x2 and y1<= y <= y2:
    print("Dentro!")

else:
    print("Fora!")
