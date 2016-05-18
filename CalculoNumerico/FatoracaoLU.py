# -*- coding: utf-8 -*-
'''
Created on 7 de mai de 2016

@author: Raul
'''
from metodoDeGauss import MetodoDeGauss

class FatoracaoLU():
    '''
    Ax=b
    A=LU
    LUx=b
    Ux=Y
    LY=b
    
    '''
    matriz=None
    vTrocas=[]#Vetor para armazenar as linhas trocadas
    def __init__(self,matriz):
        self.matriz=matriz
        self.__gerarLU()
        
    def __gerarLU(self):#Método privado
        '''
        Nessa implementação utiliza-se apenas uma matriz para representar a fatoração LU
        U é a parte da diagonal superior da matriz e L é a parte inferior.
        '''
        mL=[]#Matriz auxiliar que guarda os "m"s e suas posições 
        for i in range(self.matriz.linhas-1):
            pivo = MetodoDeGauss._acharMelhorPivo(self.matriz,i)
            self.matriz.trocarLinhas(i,pivo)#faz a troca de linhas com a linha do melhor pivô
            self.vTrocas.append([i,pivo])
            for j in range(i+1,self.matriz.linhas):#realiza as operações dentro da matriz(multiplicar linha por m e depois somar ou subtrair com outra linha).
                m = float(self.matriz.matriz[j][i])/self.matriz.matriz[i][i]
                linhaM=self.matriz.multiplicarLinha(i,m)
                self.matriz.subLinha(j,linhaM)
                mL.append([m,j,i])
        for k in mL:#add os "m"s a matriz
            self.matriz.matriz[k[1]][k[2]]=k[0]
    
    def __acharY(self,b):#Método privado
        '''
        Método responsavel por encontar os valores do vetor "Y"
        '''
        for posi in self.vTrocas:#Realiza a troca de linhas no vetor de carga
            b.trocarLinhas(posi[0],posi[1])
        vetorY=[b.matriz[0][0]]  
        for i in range(1,self.matriz.linhas):
            soma=0
            for j in range(i):
                soma=soma+self.matriz.matriz[i][j]*vetorY[j]
            vetorY.append(b.matriz[i][0]-soma)
            
        for posi in self.vTrocas:#Desfaz a troca de linhas no vetor de carga.Para não modifica-lo fora do método
            b.trocarLinhas(posi[0],posi[1])
          
        return vetorY
    
    def resolverSistema(self,b):
        vY=self.__acharY(b)
        #adiciona o vetor Y como última coluna na matriz
        for i,elemento in enumerate(vY):
            self.matriz.matriz[i].append(elemento)
        self.matriz.colunas+=1
        #Resolve o sistema.
        respostas=MetodoDeGauss._acharX(self.matriz)
        #Remove a coluna inserida(y).
        for i in range(self.matriz.linhas):
            aux=self.matriz.matriz[i]
            del aux[self.matriz.colunas-1]
        self.matriz.colunas-=1
        
        return respostas     
           



   
        
        
        

    


        