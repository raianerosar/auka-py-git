print("Calculadora")
escolha = 0
numer1 = 0
numero2 = 0
while escolha != 5:
        print("Escolha uma opção: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Resultado: ")
        escolha = int(input())
        
        if escolha != 5: 
            print("Digite um numero: ")
            numero1 = float(input())


            print("Digite um numero: ")
            numero2 = float(input())
        
        if escolha == 1:
                numeros = numero1 + numero2 
        elif escolha == 2:
                numeros = numero1 - numero2
        elif escolha == 3:
                numeros = numero1 * numero2
        elif escolha == 4: 
                try:
                    numeros = numero1 / numero2
                except ZeroDivisionError:
                    print("Erro: Não é possível dividir por zero.")
                    numeros = None
        else:
            print("Opção inválida")
    
print(f"O resultado é: {numeros}")




