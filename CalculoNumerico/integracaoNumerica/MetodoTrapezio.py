# -*- coding: utf-8 -*-
'''
Created on 26 de jun de 2016

@author: Raul
'''
from raizesFuncoes.Funcao import *
import math
class MetodoTrapezio(object):
    
    @staticmethod
    #Integra a função recebendo a mesma como string
    def integrarComFuncao(fx,h,a,b):
        fa = Funcao.fx(a,fx)
        fb = Funcao.fx(b,fx)
        somatorio = 0
        trocou=False
        if(a<b):
            temp=a
            a=b
            b=temp
            trocou=True
        for i in range(a+1,b,h):
            somatorio+=Funcao.fx(i,fx)  
        resposta = h*((fa+fb)/2.0 +somatorio)
        if trocou:
            resposta = -resposta
        return resposta
    
    @staticmethod
    #Integra a função recebendo uma lista com os fxs e xs.
    def integrarComPontos(fxs,h):
        somatorio = 0
        for i in range(1,len(fxs)-1):
            somatorio+=fxs[i]
        resposta = h*((fxs[0]+fxs[-1])/2.0 + somatorio)
        return resposta

        