from scipy.stats import expon
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter, attrgetter, methodcaller


class objeto:
	def __init__(self, Tchegada, Tentrada, Tservico, TservicoManipulavel):
		self.Tchegada = Tchegada
		self.Tentrada = Tentrada
		self.Tservico = Tservico
		self.TservicoManipulavel = TservicoManipulavel
	def __repr__(self):
		return repr((self.Tchegada, self.Tentrada, self.Tservico,self.TservicoManipulavel))
	def weighted_grade(self):
		return 'CBA'.index(self.Tchegada)

	def getTchegada(self):
		return self.Tchegada
	def getTentrada(self):
		return self.Tentrada
	def getTservico(self):
		return self.Tservico
	def getTservicoManipulavel(self):
		return self.TservicoManipulavel
	def setTchegada(self,valor):
		self.Tchegada = valor
	def setTentrada(self,valor):
		self.Tentrada = valor
	def setTservico(self,valor):
		self.Tservico = valor
	def setTservicoManipulavel(self,valor):
		self.TservicoManipulavel = valor



#define a quantidade de elementos do teste.
tamanho = 10

#tamanho padrao 10 e depois colocar tamanho variavel.

#Gerando tempos de chegada aleatorios e ordenando.
Tchegada = expon.rvs(size=tamanho)

Tchegada.sort()

#Copiando para uma lista em que os valores serao modificados (se o objeto chegar atrasado o seu tempo aumenta, por exemplo) ou apagados
Tentrada = Tchegada

#Gerando tempos de servico aleatorios.
Tservico = expon.rvs(size=tamanho)
TservicoManipulavel = Tservico

'''
#Teste de impressao
for i in range(0, tamanho):
	print("%d Tempo de chegada: %.4f" %(i+1,Tentrada[i]))
	print("%d Tempo de servico: %.4f\n" %(i+1,TservicoManipulavel[i]))
'''
Tprocessamento = 0.0
Tatendimento = 0.0
#Lista de tamanhos das filas
Tamanhos = []
#Tamanho maximo e medio da fila
TamanhoMaximo = 0.0
TamanhoMedio = 0.0

filaEspera = []
filaAtendidos = []
#Objetos que serao atendidos
objetos = []
#Objeto que esta sendo atendido
atendimento = []

#Inserindo oos objetos com seus atributos na lista de objetos.
for i in range(0,tamanho):
	objetos.append(objeto(Tchegada[i],Tchegada[i],Tservico[i],Tservico[i]))
'''
#Ordenando os objetos por tempo de servico
objetos = sorted(objetos, key=attrgetter('Tservico'))
print(objetos)
'''

#Teste de impressao
for i in range(0, tamanho):
	print("Objetos[%d]: \nTempo de chegada: %.4f\nTempo de servico: %.4f\n" %(i+1,
	objetos[i].Tchegada,objetos[i].Tservico))
	#print("%d Tempo de servico: %.4f\n" %(i+1,TservicoManipulavel[i]))

'''
for i in range(0, 100):
	Tprograma = Tprograma + Tservico[i]

print("Tempo total: %.0f"%(Tprograma*100))
'''
i = 0
total = 0
sair = "N"

while(sair == "N"):
	#verificar se o tempo de atendimento ja acabou.
	if(atendimento != []):
		if(len(atendimento) == 1):
			#print(atendimento[0])
			if(Tatendimento >= atendimento[0].getTservico()):
				print("acabou atendimento")
				filaAtendidos.append(atendimento[0])
				atendimento = atendimento[1:]
				if(len(filaEspera) == 0):
					print("Entrou com Tprocessamento = %.4f" %Tprocessamento)
					objetos[0].setTentrada(Tprocessamento)
					atendimento.append(objetos[0])
					print(atendimento)
					Tatendimento = 0.0
					objetos = objetos[1:]
					total = total + 1
				else:
				#elif(len(filaEspera) != 0):
					print("Fila")
					print("Entrou com Tprocessamento = %.4f" %Tprocessamento)
					filaEspera[0].setTentrada(Tprocessamento)
					atendimento.append(filaEspera[0])
					print(atendimento)
					Tatendimento = 0.0
					filaEspera = filaEspera[1:]
					total = total + 1
				#print("\n\n\nsaiu\n\n\n")
				#if(filaEspera != []):
					#filaEspera[0]
			else:
				Tatendimento = Tatendimento + 0.0001
				#print("NAO saiu")
				#print(Tatendimento)
	#else:
		#print("vazia")

	#Se chegar a vez e tiver vaga e a fila tiver vazia ele entra. Senao vai para a fila de espera.
	if(objetos != []):
		if(Tprocessamento >= objetos[0].Tchegada):
			if(atendimento == []):
				print("acabou atendimento")
				if(len(filaEspera) == 0):
				#else if(filaEspera == []):
					print("Entrou com Tprocessamento = %.4f" %Tprocessamento)
					objetos[0].setTentrada(Tprocessamento)
					atendimento.append(objetos[0])
					print(atendimento)
					Tatendimento = 0.0
					objetos = objetos[1:]
					total = total + 1
				else:
				#elif(len(filaEspera) != 0):#Entrando na fila de espera
					#print("Fila")
					filaEspera.append(objetos[0])
					objetos = objetos[1:]
					#print(filaEspera)
			else:
			#elif(len(filaEspera) != 0):#Entrando na fila de espera
				#print("Fila")
				filaEspera.append(objetos[0])
				objetos = objetos[1:]
				#print(filaEspera)

	#Se nao existirem mais objetos para processar a simulacao acaba
	if((len(objetos) == 0) and (len(filaEspera) == 0) ):
		sair = "S"

	Tprocessamento = Tprocessamento + 0.0001
	if(len(filaEspera) > TamanhoMaximo):
		TamanhoMaximo = len(filaEspera)

	Tamanhos.append(len(filaEspera))
	#if (i == 3):
	#	sair = "S"
print("\n")
TamanhoMedio = sum(Tamanhos) #Soma todos os elementos do vetor
TamanhoMedio = TamanhoMedio/len(Tamanhos) #Fazendo a media

print("Total = %d\nTamanho Maximo da fila: %d\nTamanho Medio da fila: %d" %(total,TamanhoMaximo,TamanhoMedio))
