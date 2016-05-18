# -*- coding: utf-8 -*-
'''
Created on 7 de mai de 2016

@author: Raul
'''

from MetodoIterativo import MetodoIterativo
import math
class MetodoDeJacobi(MetodoIterativo):
    
    def resolverSistema(self,matriz,vetorInicial,erro):
        if(self.criterioDeLinhas(matriz)==True):
            self.qtIteracoes=0
            respostas = [0]*matriz.linhas
            xi=vetorInicial
            while True:
                self.qtIteracoes+=1
                erroAtual=0
                for i in range(matriz.linhas):#Percorre as linhas da matriz
                    respostas[i]=matriz.matriz[i][matriz.colunas-1]#Recebe bi(termo independente) 
                    for j in range(matriz.colunas-1):#percorre as colunas da matriz
                        if(j!=i):
                            respostas[i]=respostas[i]-matriz.matriz[i][j]*xi[j]
                    respostas[i]=float(respostas[i])/matriz.matriz[i][i]#divide o somatorio pelo coeficiente da vari�vel a ser encontrada
                    erroAtual = math.fabs(xi[i]-respostas[i]) + erroAtual
                if(erroAtual<=erro):
                    return respostas
                for i,elemento in enumerate(respostas):#As respostas encontradas anteriormente passam a compor a novo vetor de valores para os coeficiente 
                    xi[i]=elemento
        else:#O sistemas não atende ao critério de linhas
            return -1