# -*- coding: utf-8 -*-
'''
Created on 16 de mai de 2016

@author: Raul
'''
from interpolacao.MatrizVandermonde import MatrizVandermonde
from interpolacao.PolinomioLagrange import PolinomioLagrange

#Interpolação para o raio interno por Vandermonde
print(u"Interpolação para o raio interno por matriz de Vandermonde:\n")  
prx = MatrizVandermonde([0,12],[0.2301,0.2077])
print(u"Valores dos coeficiente:%s\n"%prx.coeficientes)
print(u"Estimativa raio interno para x=3: %s"%prx.pX(3))
print(u"Estimativa raio interno para x=6: %s"%prx.pX(6))
print(u"Estimativa raio interno para x=9: %s\n"%prx.pX(9))
#Interpolaçaõ para espessura da parede arterial
print(u"Interpolação para espessura da parede arterial:\n") 
phx = MatrizVandermonde([0,12],[0.0499,0.0472])
print(u"Valores dos coeficiente:%s\n"%phx.coeficientes)
print(u"Estimativa da espessura da parede arterial para x=3: %s"%phx.pX(3))
print(u"Estimativa da espessura da parede arterial para x=6: %s"%phx.pX(6))
print(u"Estimativa da espessura da parede arterial para x=9: %s"%phx.pX(9))

#Interpolação para o raio interno por Lagrange
print(u"Interpolação para o raio interno por Lagrange:\n") 
print(u"Estimativa raio interno para x=3: %s"%PolinomioLagrange.p(3, [0,12], [0.2301,0.2077]))
print(u"Estimativa raio interno para x=6: %s"%PolinomioLagrange.p(6, [0,12], [0.2301,0.2077]))
print(u"Estimativa raio interno para x=9: %s\n"%PolinomioLagrange.p(9, [0,12], [0.2301,0.2077]))

print(u"Interpolação para espessura da parede arterial por Lagrange:\n")
print(u"Estimativa da espessura da parede arterial para x=3: %s"%PolinomioLagrange.p(3, [0,12], [0.0499,0.0472]))
print(u"Estimativa da espessura da parede arterial para x=6: %s"%PolinomioLagrange.p(6, [0,12], [0.0499,0.0472]))
print(u"Estimativa da espessura da parede arterial para x=9: %s\n"%PolinomioLagrange.p(9, [0,12], [0.0499,0.0472]))
 


