# -*- coding: utf-8 -*-
'''
Created on 17 de mai de 2016

@author: Raul
'''
import math
from abc import ABCMeta,abstractmethod


class MetodoIterativo():
    __metaclass__ = ABCMeta
    
    qtIteracoes=None
    def criterioDeLinhas(self,matriz):
        try:
            linha=0#Linha que se está verificando 
            ltrocar=1#Linha para possivel permuta 
            while True:
                soma=0
                for j in range(matriz.colunas-1):
                    if(j!=linha):
                        soma=soma+math.fabs(matriz.matriz[linha][j])
                if(math.fabs(matriz.matriz[linha][linha])<soma):#Se aii < somatorio
                    matriz.trocarLinhas(linha,ltrocar)#Troca a atual com a linha seguinte
                    ltrocar+=1
                else:#Se o critério de linhas estiver satisfeito
                    if(linha==matriz.linhas-1):#Se a última linha atende o critério então termine
                        return True 
                    linha+=1#vai verificar a próxima linha
                    ltrocar+=linha#a linha seguinte passa a ser a próxima permuta possivel
        except(IndexError):
            return False
    
    @abstractmethod
    def resolverSistema(self):
        pass

                
                    
                    
                
              
        
        
        
    
        