#Importação de biblioteca para criar uma tabela com os resultados
from tabulate import tabulate

#Criação da classe funcionarios 
class Funcinarios: 
    def __init__(self, nome, horas, turno, categoria):
        self.nome = nome
        self.horas = horas
        self.turno = turno
        self.categoria = categoria
        
#Função que valida os dados informados 
    def Validar(self, lista):
        if ((self.turno == 'M' or self.turno == 'V' or self.turno == 'N') and (self.categoria == 'O' or self.categoria == 'G')):
           print("FUNCIONARIO VALIDO, ele será adicionado a lista")
           lista.append(self)
        else:
            print("FUNCIONARIO INVALIDO, ele não será adiconado a lista")
    
#Função que calcula o salario com base nas informações 
    def Calcular(self, tabela):
        if self.categoria == "G":
            if self.turno == "N":
                valor = 10
            else:
                valor = 15   
        else: 
            if self.turno == "N":
                valor = 9
            else: 
                valor = 14
                
        salarioHoras = ((valor*1320)/100)*self.horas
        salarioTotal = salarioHoras + 1320
        lista = [self.nome, self.turno, self.horas, salarioHoras, salarioTotal]
        tabela.append(lista)
        
                
        
 #Definindo as arrays           
funcionarios = []
tabela = [['Nome','Turno','Horas Trabalhadas', 'Salario Horas', 'Salario Final' ]]

#Loop while para a coleta de informação
while True:
    novo = Funcinarios(str(input("Nome do funcionario: ")), int(input("Horas trabalhados no mês: ")), str(input("Turno: ")).upper(), str(input("Categoria: ")).upper())
    novo.Validar(funcionarios)
    if str(input("Deseja adicionar outro funcionario? ")).upper() != "SIM": break

#Loop for para realziar o calculo de todos os funcionarios que estão na lista  
for i in funcionarios:
    i.Calcular(tabela)
    
#Print do resultado em tabela 
print(tabulate(tabela))
