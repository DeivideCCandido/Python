N: int;
soma: float; media: float

print("Quantos numeros voce vai digitar ? ", end="")
N = int(input())
vet: [float] = [0 for x in range(N)]

for i in range(0, N):
 vet[i] = float(input("Digite um numero: "))

print("\nVALORES = ", end="")
for i in range(0, N):
    print(f"{vet[i]:.1f}  ", end="")

soma = 0
for i in range(0, N):
    soma = soma + vet[i]

print(f"\nSOMA = {soma:.2f}")
media = soma / N
print(f"MEDIA = {media:.2f}")
