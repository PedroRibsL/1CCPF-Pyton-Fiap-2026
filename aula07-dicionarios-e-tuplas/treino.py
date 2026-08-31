personagens = [
    {"Nome": "Peter Benjamin Parker", "Idade": 25, "Ocupação": "Vigilante", "Vivo": True},
    {"Nome": "Gwen Stacy", "Idade": 22, "Ocupação": "Interesse amoroso", "Vivo": False},
]

id = input("Digite o ID do personagem (Começa em 0): ")
id = int(id)

if 0 <= id < len(personagens):
    personagem = personagens[id]
    print(f"\nID: {id}")
    print(f"Nome: {personagem['Nome']}")
    print(f"Idade: {personagem['Idade']}")
    print(f"Ocupação: {personagem["Ocupação"]}")
    print(f"Vivo: {"Sim" if personagem["Vivo"] else "Não"}")