nome1: str; nome2: str
idade1: int; idade2: int
media: float

print(f"Dados da primeira pessoa: ")
nome1 = input("Nome: ")
idade1 = int(input("Idade: "))

print(f"Dados da segunda pessoa: ")
nome2 = input("Nome: ")
idade2 = int(input("Idade: "))

media = (idade1 + idade2) / 2

print(f"A idade media de {nome1} e {nome2} e de {media} anos")
