def operacao(a, b, c):
    resu = a / 1.609
    resu2 = b * 100
    resu3 = c * 1000
    return resu, resu2, resu3

quilometro = int(input("Digite a sua quilometragem para converter em milhas:"))
metros = int(input("Digite em metros para converter em centímentros:"))
litros = int(input("Digite em litros para converter em mililitros:"))

print(operacao(quilometro, metros, litros))