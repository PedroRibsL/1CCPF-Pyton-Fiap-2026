# Escreva um programa que dadas duas notas de 0 a 10 calcula a média aritmética entre elas.

# n1 = float(input("Digite a 1 nota: "))
# while n1 < 0 or n1 > 10:
#     print("nota invalida, digite valor de 0 a 10!")
#     n1 = float(input("Digite a 1 nota: "))


# n2 = float(input("Digite a 2 nota: "))
# while n2 < 0 or n2 > 10:
#     print("nota invalida, digite valor de 0 a 10!")
#     n1 = float(input("Digite a 2 nota: "))

# media = (n1 + n2) / 2

# print(f"a media é : {media:.2f}")

# Faça um programa que receba a quantidade de produtos que o usuário deseja
# ▪ A seguir, seu programa deve exibir a mensagem “Produto” a quantidade de vezes que o usuário
# solicitou.
# ▪ Utilize o laço for.

# produtos = int(input("informe a quantidade de produtos: "))

# for i in range(produtos):
#     print("Produto")

# ▪ Faça um programa que exiba a mensagem “Olá, Mundo”.
# ▪ Essa mensagem deverá ser exibida repetidamente.
# ▪ Ao final de toda iteração da repetição, você deve perguntar ao usuário se ele deseja exibir a mensagem
# novamente.
# ▪ Se sim, exiba novamente. Senão, saia do loop e exiba a mensagem “Fim”.

# continuar = "sim"

# while continuar == "sim":
#     print("Olá, Mundo")
#     continuar = (input("deseja exibir novamente?  ")).lower()
    
# print("fim")

#  Contagem de 0 a 100 pulando de 10 em 10.
# ▪ O terminal deve ficar assim:
# 13
# 0
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# 100

# for i in range(0, 101, 10):
#     count = 0
#     print(i)

# ▪ Faça um programa que receba um número n
# ▪ Exiba a tabuada deste número do 0 ao 25.
# ▪ Utilize laços de repetição.

# n = int(input("digite n: "))

# for i in range(26):
#     count = 1
#     print(f"{n} x {i} = {n * 1}")

# ▪ Faça um programa que receba 5 valores digitados pelo usuário e, ao final, informe qual é a soma deles.

# soma = 0
# for i in range(5):
#     n = int(input("Digite o valor: "))
    
#     soma += n
    
# print(f"a soma é: {soma}")

# Faça um programa que receba 5 valores digitados pelo usuário e, ao final, informe qual é o maior deles

maior = None

for i in range(5):
    n = int(input("Digite o valor: "))
    
    if maior is None or n > maior:
        maior = n
        
print(f"o maior valor é: {maior}")
