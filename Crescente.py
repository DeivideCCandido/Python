x: int; y: int

print("Digite dois numeros: ")
x = int(input())
y = int(input())

while x != y:
    if x > y:
        print(f"DECRESCENTE!")
    else:
        print(f"CRESCENTE!")

    print("Digite outros dois numeros: ")
    x = int(input())
    y = int(input())
