from tabulate import tabulate

ma = 0
mb = 0 
mc = 0
va = 0
vb = 0
vc = 0
na = 0
nb = 0
nc = 0
    
while True:
    novo = (str(input("Elevador: ")).upper(), str(input("Horario: ")).upper())
    if ((novo[0] == 'A' or novo[0] == 'B' or novo[0] == 'C') and (novo[1]== 'M' or novo[1]== 'V' or novo[1]== 'N')):
        print("O morador será adicionado a lista")
        if novo [0] == "A" and novo[1] == "M":
            ma +=1 
        elif novo [0] == "B" and novo[1] == "M":
            mb +=1 
        elif novo [0] == "C" and novo[1] == "M":
            mc +=1
        elif novo [0] == "A" and novo[1] == "V":
            va +=1 
        elif novo [0] == "B" and novo[1] == "V":
            vb +=1
        elif novo [0] == "C" and novo[1] == "V":
            vc +=1 
        elif novo [0] == "A" and novo[1] == "N":
            na +=1 
        elif novo [0] == "B" and novo[1] == "N":
            nb +=1 
        else:
            nc += 1
        if str(input("Deseja adicionar outro morador? ")).upper() != "SIM": break
    else:
        print("INFORMAÇÕES INVALIDAS, ele não será adiconado a lista")
        continue
    
    
a = [ma, va, na]
b = [mb, vb, nb]
c = [mc, vc, nc]
asomado = [ma + va + na]
bsomado = [mb + vb + nb]
csomado = [mc + vc + nc]

elevadortotal = [asomado, bsomado, csomado]

m = [ma + mb + mc]
v = [va + vb + vc]
n = [na + nb + nc]

horariototal = [m ,v , n]

elevadormais = elevadortotal.index(max(elevadortotal))
horariomais = elevadortotal[elevadormais].index(max(elevadortotal[elevadormais]))
if horariomais == 0: 
    x = "matutino"
elif horariomais == 1: 
    x = "vespertino"
else: 
    x = "noturno"
    
if elevadormais == 0: 
    print("O elevador A é o mais utilziado, e seu maior fluxo se encontra no periodo " + x)
elif elevadormais == 1: 
    print("O elevador B é o mais utilziado, e seu maior fluxo se encontra no periodo " + x)
else: 
    print("O elevador C é o mais utilziado, e seu maior fluxo se encontra no periodo " + x)
    
periodomias = horariototal.index(max(horariototal))
if periodomias == 0: 
    x = "matutino"
elif periodomias == 1: 
    x = "vespertino"
else: 
    x = "noturno"
    
print("O periodo com mais fluxo entre todos os elevadores é o " + x )


manha = ((max(m)-min(m))/ max(m))*100
tarde = ((max(v)-min(v))/ max(v))*100
noite = ((max(n)-min(n))/ max(n))*100

tabela = [["Periodo", "diferença porcentual"], ["Matutino", manha, "%"], ["Vespertino", tarde, "%"], ["Noturno", noite, "%"]]
print(tabulate(tabela))




