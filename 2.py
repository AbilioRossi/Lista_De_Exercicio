#Função para validar se os dados enviados pelo usurario estão entre os esperados 
def validar(msg, validos):
    valor = str(input(msg)).upper()
    while not valor in validos:
        print("Digitou errado")
        valor = str(input(msg)).upper()
    return valor

#Definindo as respontas esperadas, e craindo a lista onde seja armazenada as respostas 
elevadores = ['A', 'B', 'C']
turnos = ['M', 'V', 'N']
respostas = []

#Loop while para que possa ser recebidas as respostas, e para valida-las utilizando a função "validar"
while (True):
    elevador = validar("Informe o elevador mais utilizado(A, B, C): ", elevadores)
    turno = validar("Informe o turno mais utilizado(M, V, N): ", turnos)
    respostas.append([elevador, turno])
    if input("Deseja continuar?(S/N) ").upper() != "S": break
    
#Separandos as respondas pelo elevador e turno 
contador_elevadores = {(e,t): 0 for e in elevadores for t in turnos}
for a, b in respostas: 
    contador_elevadores[(a, b)] += 1 

#Retorna o elevador maais utilizado e em que turno ele é mais utilizado 
elevador_mais_utilizado =  max(elevadores, key=lambda e: sum(contador_elevadores[(e, t)] for t in turnos))
turno_mais_utilizado_especifico = max(turnos, key=lambda t: contador_elevadores[(elevador_mais_utilizado, t)])
print("O elevador mais utilizado é o {}, e ele está em mais moviemntado no turno {}".format(elevador_mais_utilizado, turno_mais_utilizado_especifico))

#Retorna o turno mais utilizado contando todos os elevadores
elevador_mais_utilizado = max(turnos, key=lambda t: sum(contador_elevadores[e, t] for e in elevadores))
print("O turno mais movimento é o {}".format(elevador_mais_utilizado))

#Faz o calculo da diferença percentual entre o elevador/turno mais usado e o menos usado 
mais_usado = contador_elevadores[max(contador_elevadores)]
menos_usado = contador_elevadores[min(contador_elevadores)]
diferenca_percentual = (mais_usado - menos_usado)/ menos_usado * 100
print("A diferença percentual entre o elevador/turno mais utilizado e o menos é de {}%".format(diferenca_percentual))

