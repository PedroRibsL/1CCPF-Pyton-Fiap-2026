# DESAFIO: ANALISADOR DE E-MAILS DA FIAP
# ▪ Você foi contratado para criar um pequeno sistema que analisa uma lista de endereços de e-mail de
# alunos da FIAP e gera um relatório.
# ▪ O programa deve:
# ▪ Receber uma lista de e-mails digitada pelo usuário (separados por vírgula).
# ▪ Exemplo: joao.silva@fiap.com.br, maria.souza@fiap.com.br, ana.paula@fiap.com.br
# ▪ Separar cada e-mail em:
# ▪ Nome de usuário (parte antes do @)
# ▪ Domínio (parte depois do @)
# ▪ Contar quantos e-mails pertencem a cada domínio usando um dicionário.

# Você foi contratado para criar um pequeno sistema que analisa uma lista de endereços de e-mail de
# alunos da FIAP e gera um relatório.
# ▪ O programa deve:
# ▪ Criar uma tupla com todos os nomes de usuário e exibir o primeiro e o último.
# ▪ Trocar a ordem do primeiro e último nome de usuário usando atribuição de tupla (sem variável temporária).
# ▪ Exibir o relatório final, por exemplo:
# ▪ Relatório:
# ▪ Quantidade de e-mails por domínio:
# ▪ fiap.com.br: 3
# ▪ Lista de usuários: ('ana.paula', 'joao.silva', 'maria.souza')
# ▪ Após troca de posições: ('maria.souza', 'joao.silva', 'ana.paula')

# Dicas:
# ▪ Use split('@') para separar nome de usuário e domínio.
# ▪ Use um dicionário para contar os domínios.
# ▪ Use tuple(lista) para converter uma lista em tupla.
# ▪ Use a, b = b, a para trocar valores.

entrada = input("Digite os e-mails separados por vírgula: ")
lista_emails = entrada.split(",")
print(lista_emails)

dominios = {}
usuarios = []

for email in lista_emails:
    email = email.strip()                  # 1. tira espaços em branco
    usuario, dominio = email.split("@")    # 2. separa usuário e domínio
    usuarios.append(usuario)               # guarda o usuário numa lista

    if dominio not in dominios:            # 3. conta os domínios
        dominios[dominio] = 1
    else:
        dominios[dominio] += 1

print(usuarios)
print(dominios)

tupla_usuarios = tuple(usuarios)
print("Lista de usuários:", tupla_usuarios)

lista_usuarios = list(tupla_usuarios)
lista_usuarios[0], lista_usuarios[-1] = lista_usuarios[-1], lista_usuarios[0]
tupla_trocada = tuple(lista_usuarios)
print("Após troca de posições:", tupla_trocada)

print("\nRelatório:")
print("Quantidade de e-mails por domínio:")
for dominio, quantidade in dominios.items():
    print(f"{dominio}: {quantidade}")