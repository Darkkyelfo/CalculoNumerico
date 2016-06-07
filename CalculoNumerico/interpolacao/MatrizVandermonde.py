# -*- coding: utf-8 -*-
'''
Created on 2 de jun de 2016

@author: Raul
'''
from sistemasLineares.Matriz import Matriz
from sistemasLineares.MetodoDeGauss import MetodoDeGauss

class MatrizVandermonde():
    '''
    Classe que modela o método de interpolação pela matriz de Vandermonde.
    '''
    coeficientes = []#Guarda os valores dos coeficientes do polinômio.[a0,a1,a2,...,an]
    mVander = None#Armazena a matriz de vandermonde gerada sobre os pontos
    
    def __init__(self,vetorX,vetorFx):
        vetor = []
        for i,elemento in enumerate(vetorX):
            vetor.append([1])#adiciona o elemento 1 a linha da coluna
            for j in range(1,len(vetorX)):
                vetor[i].append(elemento**(j))#adiciona os elementos elevando a potência correta
            vetor[i].append(vetorFx[i])#adiciona o valor do Fi(x)
        self.mVander = Matriz(vetor)#cria a matriz de Vandermonde
        #encontra o valor dos coeficientes pelo método de Gauss
        self.coeficientes = MetodoDeGauss.resolverSistema(self.mVander)
    
    def pX(self,valor):
        resposta=self.coeficientes[0]
        for i in range(1,len(self.coeficientes)):
            resposta+=self.coeficientes[i]*valor**(i)
        
        return resposta
    
     
            

            
            
        

        