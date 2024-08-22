#Imagine que você está planejando uma viagem para o Vale do Silício no final de setembro. 
#Você quer saber como as temperaturas locais podem variar em diferentes escalas de temperatura 
#para se preparar adequadamente. A previsão do tempo local indica a temperatura em graus Fahrenheit, 
#mas você também gostaria de saber como essa temperatura seria em Celsius, já que é a sua habitual. 
#Como também é curioso com relação à diferentes escalas, por que não saber como ficaria o valor em Kelvin?

#Ao pensar sobre o assunto, você pensou que seu problema deve ser o mesmo passado por 
#várias outras pessoas e decidiu que vai ajudar. Para isso, você precisa escrever um algoritmo que 
#permita ao usuário informar a temperatura (em números reais) e a escala utilizada (Celsius, Fahrenheit 
#ou Kelvin). A saída do programa será a temperatura nas três escalas, com duas casas decimais de precisão. A entrada é composta pelo valor da temperatura, seguida de uma letra que vai indicar a escala em que ela está.


valor_temperatura = float(input("Digite o valor da temperatura: "))
escala = input("Digite a escala da temperatura (C, F, K): ").upper()

if escala == 'C':
    celsius = valor_temperatura
    fahrenheit = (valor_temperatura * 9/5) + 32
    kelvin = valor_temperatura + 273.15
elif escala == 'F':
    celsius = (valor_temperatura - 32) * 5/9
    fahrenheit = valor_temperatura
    kelvin = (valor_temperatura - 32) * 5/9 + 273.15
elif escala == 'K':
    celsius = valor_temperatura - 273.15
    fahrenheit = (valor_temperatura - 273.15) * 9/5 + 32
    kelvin = valor_temperatura
else:
    print("Escala desconhecida. Use 'C' para Celsius, 'F' para Fahrenheit ou 'K' para Kelvin.")
    exit()

print(f"{celsius:.2f} °C, {fahrenheit:.2f} °F, {kelvin:.2f} K")
