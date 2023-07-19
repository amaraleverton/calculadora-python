def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

print("Calculadora de Adição e Subtração")
print("-------------------------------")

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite '+' para adição ou '-' para subtração (ou 'sair' para encerrar): ")

        if operacao == '+':
            resultado = adicao(num1, num2)
            print(f"{num1} + {num2} = {resultado}")
        elif operacao == '-':
            resultado = subtracao(num1, num2)
            print(f"{num1} - {num2} = {resultado}")
        elif operacao.lower() == 'sair':
            print("Encerrando a calculadora.")
            break
        else:
            print("Operação inválida. Tente novamente.")
    except ValueError:
        print("Erro: Certifique-se de digitar apenas números válidos.")