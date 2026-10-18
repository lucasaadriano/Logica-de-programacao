# Programa 3: desconto na compra
valor_compra = 150
desconto = 0
if valor_compra >= 100:
    desconto = 10
print("Desconto:", desconto, "%")
valor_final = valor_compra - (valor_compra * desconto / 100)
print("Valor final:", valor_final)
