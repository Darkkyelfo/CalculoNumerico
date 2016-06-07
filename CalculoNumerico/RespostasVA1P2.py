# -*- coding: utf-8 -*-
'''
Created on 16 de mai de 2016

@author: Raul
'''
from sistemasLineares.Matriz import Matriz
from sistemasLineares.FatoracaoLU import FatoracaoLU
from sistemasLineares.MetodoGaussSeidel import MetodoDeGaussSeidel
from sistemasLineares.MetodoJacobi import MetodoDeJacobi

#Primeira Questão
print("1)\n")
A = Matriz([[1,-1,2],[3,7,-4],[5,-2,1]])
b=Matriz([[-2],[1],[5]])
c=Matriz([[1],[-1],[3]])
fat=FatoracaoLU(A)
#a)
print("a)\n")
print("Os elementos que seriam 0 na matriz U aqui são os 'm's da matriz L \n" )
A.imprimirMatriz()
#b)
print("b)\n")
print("Para Ax=b os valores são:%s\n"%fat.resolverSistema(b))
print("Para Ax=c os valores são:%s"%fat.resolverSistema(c))
#Segunda Questão
print("\n2)\n")
A = Matriz([[1,3,1,-2],[5,2,2,3],[0,6,8,-6]])
jacobi=MetodoDeJacobi()
print("Solucao por jacobi:%s\nquantidade de iterações:%s "%(jacobi.resolverSistema(A,[0,0,0],0.05),jacobi.qtIteracoes))
gS=MetodoDeGaussSeidel()
print("\nSolucao por Gauss Seidel:%s\nquantidade de iterações:%s "%(gS.resolverSistema(A,[0,0,0],0.05),gS.qtIteracoes))