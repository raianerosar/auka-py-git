print("Calculadora")
escolha = 0
numero = 0
resultado = 0

while escolha != 6:
        print("Escolha uma opção: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - pontencia  \n 5 - Divisão \n 6 - Resultado: ")
        escolha = int(input())

        if escolha != 6: 
                print("Digite um numero: ")
                numero = float(input())

        if resultado == 0:
         print("Digite um numero: ")
         resultado = float(input())


        if escolha == 1:
                resultado  = numero + resultado
        elif escolha == 2:
                resultado = numero - resultado
        elif escolha == 3:
                resultado = numero * resultado
        elif escolha == 4:
                resultado = numero ** resultado 
        elif escolha == 5: 
                try:
                   resultado = numero / resultado
                except ZeroDivisionError:
                    print("Erro: Não é possível dividir por zero.")
                    numero = None
        elif escolha == 6:
                print("")
        else:

                print("operação invalida")
       
    
print(f"O resultado é: {resultado}")




