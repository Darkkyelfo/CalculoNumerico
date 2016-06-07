# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 18:14:12 2016

@author: Raul
"""
import math

class MetodoDeGauss():
    
    @staticmethod
    def _acharMelhorPivo(matriz,linha):#método protected 
        pivo = [matriz.matriz[linha][linha],linha]
        for i in range(linha,matriz.linhas):
            if(math.fabs(matriz.matriz[i][linha])>math.fabs(pivo[0])):
                pivo[0]=matriz.matriz[i][linha]
                pivo[1]=i
        return pivo[1]#retorna a posição do melhor pivô
    
    @staticmethod
    def __triangularizacao(matriz):#Método private
        for i in range(matriz.linhas-1):
            pivo = MetodoDeGauss._acharMelhorPivo(matriz,i)
            matriz.trocarLinhas(i,pivo)#faz a troca de linhas com a linha do melhor pivô
            for j in range(i+1,matriz.linhas):#realiza as operações dentro da matriz(multiplicar linha por m e depois somar ou subtrair com outra linha).
                m = float(matriz.matriz[j][i])/matriz.matriz[i][i]
                linhaM=matriz.multiplicarLinha(i,m)
                matriz.subLinha(j,linhaM)
    
    @staticmethod
    def _acharX(matriz):#Método protected
        '''
            Encontra os valores das incognitas do sistemas quando a matriz está triangularizada
        '''
        respostas=[1]*(matriz.colunas-1)
        aux=matriz.colunas-2
        for i in range(matriz.linhas-1,-1,-1):#percorre a matriz de baixo pra cima
            soma=0
            div=0
            nNulo=False
            for j in range(i,matriz.colunas-1):
                if(nNulo==False and matriz.matriz[i][j]!=0):
                    nNulo=True
                    div=matriz.matriz[i][j]
                else:
                    soma=soma + matriz.matriz[i][j]*respostas[j]
            respostas[aux]=(matriz.matriz[i][j+1]-soma)/float(div)
            aux-=1
        return respostas
        
    @staticmethod
    def resolverSistema(matriz):#Método público
        MetodoDeGauss.__triangularizacao(matriz)
        respostas=MetodoDeGauss._acharX(matriz)
        return respostas
                
            



            
    