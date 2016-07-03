# -*- coding: utf-8 -*-
'''
Created on 26 de jun de 2016

@author: Raul
'''

from integracaoNumerica.MetodoTrapezio import *
from integracaoNumerica.Metodo1TercoSimpson import *

fxs = [0,1.8,2,4,4,6,4,3.6,3.4,2.8,0]
resultado = MetodoTrapezio.integrarComPontos(fxs,2)
#a)
print(u"a) Método dos trapézios:%s"%resultado)
#b)
resultado = Metodo1TercoSimpson.integrarComPontos(fxs,2)
print(u"b) Método 1/3 de Simpson:%s"%resultado)
