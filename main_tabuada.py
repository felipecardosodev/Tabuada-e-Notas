# FOR 
#Gerador de Tabuada Automático

num = int(input("Deseja ver a tabuada de qual numero? "))

print(f"\nTabuada do {num}:")
for i in range(1, 11):
    resultado = num * i 
    print(f"{num} x {i} = {resultado}")

print("Fim do programa\n")

#Somando notas academicas
total_notas = 0
qtd_provas = 4

for i in range(1, qtd_provas + 1):
    nota = float(input(f"Digite a nota da prova {i}: "))
    total_notas = total_notas + nota # Acumulador

media = total_notas / qtd_provas
print(f"\nA média final do semestre é: {media}")

print("Fim do programa.")