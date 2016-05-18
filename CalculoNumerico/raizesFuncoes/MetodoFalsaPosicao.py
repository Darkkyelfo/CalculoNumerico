# -*- coding: utf-8 -*-
'''
Created on 17 de mai de 2016

@author: Raul
'''
import math
from raizesFuncoes.Funcao import Funcao

class MetodoFalsaPosicao():
    
    @staticmethod
    def zeroFuncao(funcao,a,b,e):
        ak=a
        bk=b
        xk = bk - Funcao.fx(bk,funcao)*(float((bk-ak))/(Funcao.fx(bk,funcao)-Funcao.fx(ak,funcao)))
        iteracoes=0
        while True:
            xkant=xk
            if(Funcao.fx(xk,funcao)==0):
                return xk
            elif(Funcao.fx(ak,funcao)*Funcao.fx(xk,funcao)<0):
                bk=xk
            else:
                ak=xk
            xk = bk - Funcao.fx(bk,funcao)*(float(bk-ak)/(Funcao.fx(bk,funcao)-Funcao.fx(ak,funcao)))
            erro=math.fabs(xk - xkant)
            iteracoes=iteracoes+1
            if erro<=e:
                return xk,iteracoes
        