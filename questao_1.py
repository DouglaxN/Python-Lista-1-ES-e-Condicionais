#Faça um programa que leia o valor de uma compra e a opção de pagamento 
#(V – para pagamento à vista ou P – para pagamento parcelado). 
#Caso o cliente pague à vista, terá um desconto de 5%, caso pague em 3 vezes 
#terá um acréscimo de 8%. O programa deve mostrar o valor da compra e o valor 
#à vista ou valor a prazo (valor total e o valor de cada parcela).

valor_compra = float(input("Digite o valor da compra: R$ "))

opcao_pagamento = input("Digite a opção de pagamento (V para à vista, P para parcelado): ").strip().upper()

if opcao_pagamento == 'V':
    valor_final = valor_compra - (valor_compra * 0.05)
    print(f"Valor com desconto à vista: R$ {valor_final:.2f}")

elif opcao_pagamento == 'P':
    valor_final = valor_compra + (valor_compra * 0.08)
    valor_parcela_1 = valor_final/3
    valor_parcela_2 = valor_final/3
    valor_parcela_3 = valor_final/3
    
    print(f"Valor total a prazo: R$ {valor_final:.2f}")
    print(f"Valor parcela 1: R$ {valor_parcela_1:.2f}")
    print(f"Valor parcela 2: R$ {valor_parcela_2:.2f}")
    print(f"Valor parcela 3: R$ {valor_parcela_3:.2f}")

else:
    print(f"Opção de pagamento inválida. Por favor, digite 'V' para à vista ou 'P' para parcelado.")

