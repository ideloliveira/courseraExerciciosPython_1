import os
contador = 1
reprovado = 0
recuperacao = 0
aprovado = 0
desempenho = 0
notas = []
for i in range(6):
    nota = float(input("Entre com  nota do %dº aluno: "%(contador)))
    notas.append(nota)
    contador = contador + 1
    os.system('cls')

for alunoNota in notas:
    if alunoNota >= 5:
        aprovado = aprovado + 1
        if alunoNota > 8:
            desempenho = desempenho + 1            
    elif alunoNota >=3.0 and alunoNota < 5.0:
        recuperacao = recuperacao + 1
    else:
        reprovado = reprovado + 1        


print("Total de alunos = %g" %(len(notas)))
print("Numero de Alunos reprovados = %g"%(reprovado))
print("Numero de Alunos recuperação = %g"%(recuperacao))
print("Numero de Alunos aprovado = %g"%(aprovado))
print("Numero de Alunos com desempenho muito bom = %g"%(desempenho))
