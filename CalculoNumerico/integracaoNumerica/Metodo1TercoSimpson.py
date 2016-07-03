'''
Created on 26 de jun de 2016

@author: Raul
'''
from raizesFuncoes.Funcao import *
class Metodo1TercoSimpson(object):

    @staticmethod
    def integrarComPontos(fxs,h):
        n = len(fxs)-1
        if(n%2!=0):
            return False
        else:
            pares=0
            impares=0
            for i in range(1,len(fxs)-1):
                if(i%2==0):
                    pares+=fxs[i]
                else:
                    impares+=fxs[i]
            resultado = (h/3.0)*(fxs[0] + 2*pares +4*impares + fxs[-1])
            return resultado
    
    
    @staticmethod
    def integrarComFuncao(funcao,a,b,n):
        if(n%2!=0):
            return False
        else:
            h = float((b-a))/n
            pares = 0
            impares = 0 
            for i in (1,n-1):
                xi = a + i*h
                if(i%2==0):
                    pares = Funcao.fx(xi, funcao)
                else:
                    impares = Funcao.fx(xi, funcao)  
            resultado = (h/3.0)*(Funcao.fx(a, funcao) + 2*pares + 4*impares + Funcao.fx(b, funcao))
            return resultado       
        
        