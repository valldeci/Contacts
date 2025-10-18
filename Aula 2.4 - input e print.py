#Q1
comprimento = int(input("Digite o comprimento: "))
largura = int(input("Digite a largura: "))
preco_m2 = float(input("Valor do m2: "))

area = comprimento * largura  # m2
preco_total = area * preco_m2

print(f"O terreno possui {area}m2 e custa R${preco_total:,.2f}")

#Q2
# Leitura de dados (entrada)
fahrenheit = int(input("Digite a temperatura em F: "))

# Processamento
celsius = (fahrenheit - 32) * 5 / 9

# Impressão de dados (saída)
print(f"{fahrenheit} graus Fahrenheit são {int(celsius)} graus Celsius.")

#3
# Leitura de dados (entrada)
valor = int(input("Digite o valor: "))

# Processamento
# Começar da maior nota (quantas notas?)
notas_100 = valor // 100  # 576 // 100 = 5
valor = valor % 100      # 576 - 5*100 = 76

notas_50 = valor // 50   # 76 // 50 = 1
valor = valor % 50       # 76 - 1*50 = 26

notas_20 = valor // 20   # 26 // 20 = 1
valor = valor % 20       # 26 - 1*20 = 6

notas_10 = valor // 10   # 6 // 10 = 0
valor = valor % 10       # 6 - 0*10 = 6

notas_5 = valor // 5     # 6 // 5 = 1
valor = valor % 5        # 6 - 1*5 = 1

notas_2 = valor // 2     # 1 // 2 = 0
valor = valor % 2        # 1 - 0*2 = 1

# Impressão de resultados
print(f"{notas_100} nota(s) de 100")
print(f"{notas_50} nota(s) de 50")
print(f"{notas_20} nota(s) de 20")
print(f"{notas_10} nota(s) de 10")
print(f"{notas_5} nota(s) de 5")
print(f"{notas_2} nota(s) de 2")

#Q4
valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
resto = valor

for nota in notas:
    quantidade = resto // nota
    resto = resto % nota
    print(f"{quantidade} nota(s) de R${nota},00")