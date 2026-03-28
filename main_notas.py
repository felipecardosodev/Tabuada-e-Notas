
#Somando notas academicas
total_notas = 0
qtd_provas = 4

for i in range(1, qtd_provas + 1):
    nota = float(input(f"Digite a nota da prova {i}: "))
    total_notas = total_notas + nota # Acumulador

media = total_notas / qtd_provas
print(f"\nA média final do semestre é: {media}")

print("Fim do programa.")