escolha_usuario = 23324
#0 -> sair do programa
#1 -> entrar no programa
# >>> erra!!

match escolha_usuario:
    case 0:
        print("sair do programa")
    case 1:
        print("entrar no programa")
    case _:
        print("erro!!")