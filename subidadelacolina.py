import json
import random
from operator import itemgetter

with open('subidadelacolina.json') as file:
	data = json.load(file)

NodRut=[]

SigNod=[]

Hijos=[]

Sig = []
def subidadelacolina(inicio,final,NodAnt):
    NodRut.append(inicio)
    print("--------------------------------------")
    print("Valor Inicial "+inicio)
    print("Valor Anterior "+NodAnt)
    if Sig:
        del Sig[:]
        del Hijos[:]
    if final == inicio:
        print("Se encontro")
        return inicio
    if NodAnt == "":
        NodAnt = inicio

    for d in data:
        if d[0] == inicio:
            if NodAnt != "":
                if d[1] != NodAnt:
                    Hijos.append(d)
    

  
    print(min(Hijos, key=itemgetter(2))[:])
    
    meen = (min(Hijos, key=itemgetter(2))[2])

   
    for c in Hijos:
        if c[2] == meen:
           
            Sig.append(c)
    print("Posibles Rutas")
    print(Sig)
    nummeen = 0
    for n in Sig:
        nummeen = nummeen +1
       
        if nummeen > 1:
            r = random.random()
  
            if r < 0.5:
                Sig.pop()
            else: 
                Sig.pop(0)
        else:
            print("")
    if Sig:
        for n in Sig:
            print("Ruta elegida")
            print(n[1])
            return subidadelacolina(n[1],final,inicio)
    print("--------------------------------------------")

def hijos(lista,actual):
    H = filter(lambda  a: a[0] == actual,lista)
    return list(H)   
arch=subidadelacolina("Z","I","")
if arch:
    print("Se encontro")
    print(arch)
    print("Ruta usada")
    print(NodRut)
