# -*- coding: utf-8 -*-
'''
Created on 17 de mai de 2016

@author: Raul
'''
import math
from raizesFuncoes.Funcao import Funcao

class MetodoBissecao():
    
    @staticmethod
    def zeroFuncao(funcao,a,b,e):
        xk=float((a+b))/2
        ak=a
        bk=b
        iteracoes=0
        while True:
            xkant=xk
            if(Funcao.fx(xk,funcao)==0):
                return xk
            elif(Funcao.fx(ak,funcao)*Funcao.fx(xk,funcao)<0):
                bk=xk
            else:
                ak=xk
            xk=float((ak+bk))/2
            erro=math.fabs(xk - xkant)
            iteracoes=iteracoes+1
            if erro<=e:
                return xk,iteracoes
        