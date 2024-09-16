import calculadora

def menu():
    texto ="0-Sair\n1-Somar\n2-Subtrair\n3-Multiplicar\n4-Dividir\n Escolha uma das opções anteriores "
    op = int(input(texto))
    while op != 0:
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        if op == 1:
           print("O resultado é: ", calculadora.somar(a, b))
           print("")

        op = int(input(texto))
    else:
        print('Até mais')

def main():
    menu()

main()