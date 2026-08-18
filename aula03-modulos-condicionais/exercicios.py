#  Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

# import pygame
#
# pygame.init()
# pygame.mixer.init()
#
# pygame.mixer.music.load('musica.mp3')
# pygame.mixer.music.play(start=175.0)  # só uma vez aqui
#
# clock = pygame.time.Clock()
#
# while pygame.mixer.music.get_busy():
#     clock.tick(30)

#Faça um programa que leia um número, e informe se ele é par ou impar.

# numero = int(input("digite o numero: "))
#
# if numero % 2 == 0:
#     print("Número par")
# else:
#     print("É impar")

#Faça um programa que peça dois números e imprima o maior deles, e informe caso eles sejam iguais.

# num1 = int(input("Digite o primeiro valor: "))
# num2 = int(input("Digite o segundo valor: "))
#
# if num1 > num2:
#     print(num1)
# elif num2 > num1:
#     print(num2)
# elif num1 == num2:
#     print("são iguais!")

# Faça um programa para a leitura de quatro notas parciais de um aluno. O programa deve calcular a
# média alcançada pelo aluno e apresentar:
# ▪ A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# ▪ A mensagem "Em recuperação", se a média for entre cinco, incluindo o cinco, e sete;
# ▪ A mensagem "Reprovado", se a média for menor que cinco.


nota_1 = float(input("digite sua primeira nota: "))
nota_2 = float(input("digite sua segunda nota: "))
nota_3 = float(input("digite sua terceira nota: "))
nota_4 = float(input("digite sua quarta nota: "))

media = (nota_1 + nota_2 + nota_3 + nota_4)/4
print(f"sua media foi de {media}")

if media >= 7:
    print("aprovado")
elif media >= 5:
    print("em recuperação")
else:
    print("reprovado")