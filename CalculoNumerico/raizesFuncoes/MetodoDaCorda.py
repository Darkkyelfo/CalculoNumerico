# -*- coding: utf-8 -*-
'''
Created on 17 de mai de 2016

@author: Raul
'''
from raizesFuncoes.Funcao import Funcao
import math

class MetodoDaCorda():
    
    @staticmethod
    def zeroFuncao(funcao,a,b,e):
        xk=a
        iteracoes=0
        while True:
            xkant=xk
            xk= xk - float((b-a))/(Funcao.fx(b,funcao)-Funcao.fx(a,funcao))*Funcao.fx(xk,funcao)
            erro=math.fabs(xk - xkant)
            iteracoes=iteracoes+1
            if erro<e:
                return xk,iteracoes
        