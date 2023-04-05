def atribuirNota():
    nome = str(input("Insira o nome do aluno: "))
    notas =  []
    for i in range(3): 
        notas.append(float(input("Insira a nota {}: ".format(i +1))))
    with open ('Notas.txt', 'a+') as file: 
        file.write(f"{nome}: {notas[0]},{notas[1]},{notas[2]}\n")
        file.close()
        
with open ('Notas.txt', 'r') as file:
    alunos = file.readline()
    while alunos:
        nome, notas = alunos.split(':')  
        notasFloat = list(map(float, notas.split(',')))
        media = sum(notasFloat)/3 
                
        if media >= 7:
            with open("aprovados.txt", "w") as aprovados:
                aprovados.write(f"{nome}: {notasFloat}, {media} - Aprovado\n")
                aprovados.close()
        elif media >= 5:
            with open("exame.txt", "w") as exame:
                exame.write(f"{nome}: {notasFloat}, {media} - Exame\n")
                exame.close()
        else:
            with open("reprovados.txt", "w") as reprovados:
                reprovados.write(f"{nome}: {notasFloat}, {media} - Reprovado\n")
                reprovados.close()   
        alunos = file.readline()
    file.close
    
    