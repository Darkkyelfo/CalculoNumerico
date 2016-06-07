# -*- coding: utf-8 -*-
'''
Created on 7 de jun de 2016

@author: Raul
'''

class PolinomioLagrange():
    '''
        Classe que implementa a interpolação pelo polinômio de Lagrange
    '''
    
    @staticmethod
    def p(x,vetorX,vetorY):
        lx = [0]*len(vetorX)
        #Calcula valor dos "L(x)s"
        for j, xj in enumerate(vetorX):
            for i,xi in enumerate(vetorX):
                if(j!=i):
                    lx[j]+=float((x-xi))/(xj-xi)
        px = 0#Armazena o valor do polin�mio no ponto x
        for i,y in enumerate(vetorY):
            px += y*lx[i]
        return px 
                    
                
            
            
            

        