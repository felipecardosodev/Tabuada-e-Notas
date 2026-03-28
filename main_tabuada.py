# FOR 
#Gerador de Tabuada Automático

num = int(input("Deseja ver a tabuada de qual numero? "))

print(f"\nTabuada do {num}:")
for i in range(1, 11):
    resultado = num * i 
    print(f"{num} x {i} = {resultado}")

print("Fim do programa\n")
