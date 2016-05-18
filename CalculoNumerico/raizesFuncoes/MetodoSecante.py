'''
Created on 17 de mai de 2016

@author: Raul
'''
import math
from raizesFuncoes.Funcao import Funcao
class MetodoSecante():
    
    @staticmethod
    def acharZeroFunc(x0,x1,funcao,e):
        xk=x1
        xk0=x0
        iteracoes=0
        while True:
            xk1=xk - (xk - xk0)/(Funcao.fx(xk,funcao)-Funcao.fx(xk0,funcao))*Funcao.fx(xk,funcao)
            erro = math.fabs(xk1-xk)
            xk0=xk
            xk=xk1
            iteracoes=iteracoes+1
            if erro<=e:
                return xk,iteracoes
        