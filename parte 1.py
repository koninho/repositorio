def operacao (a, b, c):
    if b == "+":
        resu = a + c
    elif b == "-":
        resu = a - c
    elif b == "/":
        resu = a / c
    elif b == "*":
        resu = a * c
    return resu

num1 = int(input("digite o primeiro número: "))
valor = input("digite a operação: ")
num2 = int(input("digite o segundo múmero: "))
print("o resultado é igual a", operacao(num1, valor, num2))