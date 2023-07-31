x: int; y: int; troca: int; impares: int

print("Digite dois numeros: ")
x = int(input())
y = int(input())

if x > y:
    troca = x
    x = y
    y = troca

impares = 0
for i in range(x+1, y):
    if i % 2 != 0:
        impares = impares + i

print(f"SOMA DOS IMPARES = {impares}")
