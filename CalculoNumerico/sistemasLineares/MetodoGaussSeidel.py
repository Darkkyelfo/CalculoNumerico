# -*- coding: utf-8 -*-
'''
Created on 7 de mai de 2016

@author: Raul
'''
from MetodoIterativo import MetodoIterativo
import math
class MetodoDeGaussSeidel(MetodoIterativo):
    
    def resolverSistema(self,matriz,vetorInicial,erro):
        if(self.criterioDeLinhas(matriz)==True):
            self.qtIteracoes=0
            respostas = vetorInicial
            while True:
                erroAtual=0
                self.qtIteracoes+=1
                for i in range(matriz.linhas):
                    xAnt=respostas[i]#Guarda o valor anterior de Xi
                    respostas[i]=matriz.matriz[i][matriz.colunas-1]# Resposta recebe bi 
                    for j in range(matriz.colunas-1):
                        if(j!=i):
                            respostas[i]=respostas[i]-matriz.matriz[i][j]*respostas[j]
                    respostas[i]=float(respostas[i])/matriz.matriz[i][i]
                    erroAtual = math.fabs(xAnt-respostas[i]) + erroAtual
                if(erroAtual<=erro):
                    return respostas
        else:#O sistemas não atende ao critério de linhas
            return -1
           



    
        