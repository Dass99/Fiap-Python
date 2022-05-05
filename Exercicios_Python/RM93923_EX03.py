notaAtual_Impar = 0
notaAtual_Par = 0

for k in range(1,51,2):

        print("\n!!!VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES!!!\n")
        notasImpares = float(input(f"informe a nota do aluno {k}: "))
        notaAtual_Impar += notasImpares
        mediaImpar = notaAtual_Impar/25

for j in range(2,51,2):

        print("\n!!!VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES!!!\n")
        notasPares = float(input(f"Informe a nota do aluno {j}: "))
        notaAtual_Par +=  notasPares
        mediaPar = notaAtual_Par /25

print("\n")
print(f"Média da metade par da turma: {mediaPar}")
print(f"Média da metade impar da turma: {mediaImpar}")

if(mediaPar > mediaImpar):
    print("\nA metade par da turma teve a maior nota")

else:
    print("\nA metade ímpar da turma  teve a maior nota")



