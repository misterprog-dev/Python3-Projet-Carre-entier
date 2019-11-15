#-*- coding : utf-8 *-
import math
import random

"""
Projet : Projet Python, Representer un entier naturel comme somme de quatre carres
Etudiant : DIAKITE SOUMAILA
"""
############ ZONE FONCTION #############################
#Etape 1
#Retourne (p,q)  tel que m = p^2 + q^2
#Si il est Impossible d'écrire, on retourne (-1,-1)
def Etape1(m):
    #Si on a 0 , on p=0,q=0
    if(m == 0):
        p=0
        q=0
        return p , q
    #Sinon on effectue le traitement
    p = math.floor(math.sqrt(m))
    #On vérifie si m est un carré parfait
    if(m == math.floor(math.sqrt(m))**2):
        q=0
        return p , q
    else:
        res = m-p**2
        if(res == 1):
            q=1
            return p , q
        #on vérifie si le reste est un carré parfait
        else:
            if(res == math.floor(math.sqrt(res))**2):
                q = math.floor(math.sqrt(res))
                return p,q
            else:
            #on retourne (-1,-1) pour dire qu'il est impossibe d'établir l'écriture
                return -1,-1            

#Etape 2: trouver m tel que m et n-m  soient tous les deux sommes de deux carrés puis sort un quadruple (a, b, c, d)
def Etape2(n):
    if(Etape1(n) != (-1,-1)):
        a , b = Etape1(n)
        c , d = 0 , 0
        return a,b,c,d
    else:
        m=0
        for i in range(0,n):
            if(Etape1(i) != (-1,-1) and Etape1(n-i) !=(-1,-1)):
                m = i
        a,b = Etape1(m)
        c,d = Etape1(n-m)
        return a,b,c,d                
#Programme de test du resultat final 
def Etape3_Test(nombre, res):
    a,b,c,d = res
    if( nombre - (a**2 + b**2 + c**2 + d**2)  == 0):
        return True
    else:
        return False

          
######### PROGRAMME PRINCIPAL #############
print("PROJET: Representer un entier naturel comme somme de quatre carres\n")
rep = 1
while (rep ==1):
    nombre = random.randrange(1000)
    print("Le nombre aléatoire est : ", nombre,"\n")
    res = Etape2(nombre)
    a,b,c,d = res
    if(Etape3_Test(nombre , res)):
        print(nombre ,"   =  ", a,"^2  +", b , "^2  +", c,"^2  +", d , "^2 ")
        rep = int(input("\nEssayer encore : 1-oui 0-non  :    "))