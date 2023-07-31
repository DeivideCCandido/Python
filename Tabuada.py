N: int; resultado: int

print("Deseja a tabuada para qual valor ? ", end="")
N = int(input())

for i in range(1, 11):
    resultado = N * i
    print(f"{N} x {i} = {resultado}")
