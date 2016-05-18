# -*- coding: utf-8 -*-
'''
Created on 17 de mai de 2016

@author: Raul
'''
from raizesFuncoes.Funcao import Funcao
import math

class MetodoDeNewton():
    
    @staticmethod
    def zeroFx(x0,funcao,dfuncao,e):
        xk=x0
        iteracoes=0
        while True:
            xkant=xk
            xk=xk - Funcao.fx(xk,funcao)/float(Funcao.fx(xk,dfuncao))
            erro=math.fabs(xk-xkant)#math.fabs é o módulo de um número
            iteracoes=iteracoes+1
            if(erro<=e):
                return xk,iteracoes#python permite "multiretorno" :P
        