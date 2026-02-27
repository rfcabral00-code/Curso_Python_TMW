#Faça um programa que vende uma garrada de água:
# Se o cliente escolher água natural, será cobrado r$1,50
# Se o cliente escolher água com gas, será cobrado r$2,50

texto = """
Escolha a sua água para comprar
(1) Água mineral natural - R$ 1.5
(2) Água mineral com gás - R$ 2.5
"""

opcao = input(texto)


valor_item = 0
if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item = 2.5

if valor_item == 0:
    print("Entre com a opção correta, por favor.")
else:
    qtde = input("Quantas garrafas?")
    qtde = int(qtde)
    valor_total = valor_item * qtde
    print("Sua conta deu: R$", valor_total)