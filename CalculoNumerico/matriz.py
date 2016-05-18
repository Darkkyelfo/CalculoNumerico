# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:56:02 2016

@author: Raul
"""

class Matriz():
    matriz=[]
    linhas=0
    colunas=0
    
    def __init__(self,vetor):
        
        self.matriz=vetor
        self.linhas = len(self.matriz)
        for i in self.matriz[0]:
            self.colunas=self.colunas+1
    
    
    def somar(self,matrizA):
        
        if(matrizA.linhas==self.linhas and matrizA.colunas==self.colunas):
            for i,linha in enumerate(matrizA.matriz):
                for j,coluna in enumerate(linha):
                    self.matriz[i][j]=self.matriz[i][j]+coluna
        else:
            print(u"Não é possível realizar essa operação")
            
    
    def subtrair(self,matrizA):
        
        if(matrizA.linhas==self.linhas and matrizA.colunas==self.colunas):
            for i,linha in enumerate(matrizA.matriz):
                for j,coluna in enumerate(linha):
                    self.matriz[i][j]=self.matriz[i][j]-coluna
        else:
            print(u"Não é possível realizar essa operação")

    def produto(self,matrizA):
        
        if(self.colunas==matrizA.linhas):
            matrizNova = [0]*self.linhas
            for i in range(self.linhas):
                matrizNova[i]=[0]*matrizA.colunas
            
            for i in range(len(self.matriz)):
                for j in range(len(matrizA.matriz[0])):
                    for k in range(len(matrizA.matriz)):
                        matrizNova[i][j]=matrizNova[i][j] + self.matriz[i][k]*matrizA.matriz[k][j]

                        
            return matrizNova
            
    def trocarLinhas(self,linhaA,linhaB):
        aux = self.matriz[linhaA]
        self.matriz[linhaA]=self.matriz[linhaB]
        self.matriz[linhaB]=aux
    
    def multiplicarLinha(self,linha,escalar):
        novaLinha = [0]*self.colunas
        for i,elemento in enumerate(self.matriz[linha]):
            novaLinha[i]=elemento*escalar
        return novaLinha
    
    def subLinha(self,linha,vLinha):
        for j in range(self.colunas):
            self.matriz[linha][j]=self.matriz[linha][j]-vLinha[j]
            
    def somarLinha(self,linha,vLinha):
        for j in range(self.colunas):
            self.matriz[linha][j]=self.matriz[linha][j]+vLinha[j]

    
    def imprimirMatriz(self):
        for i in self.matriz:
            print("%s\n"%i)    
            
            
            




