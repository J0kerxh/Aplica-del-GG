import sys
import funciones as fp
import numpy as np
#from matplotlib.pyplot import *


def main():
    if (len(sys.argv)!=4):
        print("Ingrese la cantidad de argumentos (3)")
        return 0
    
    n= int(sys.argv[1])
    k= int(sys.argv[2])
    filename=sys.argv[3]
    print "correcto"    

################# Solo para probar randomizadamente
    f = open(filename,'wb')
    for i in range(100):
        f.write('%d,%d\n'%(np.random.rand()*100-50,np.random.rand()*100-50))            
    f.close()    
#################

    f = open(filename,'r')
            
    M = []
    cant=0
    for line in f:
        L = line.split(',')
        
        if( len(L)!=n ):
            print('No cumple con el n')
            return    
        for i in range(n):
            L[i] = int(L[i])
        M.append(L)
        cant+=1

    M = np.array(M)

    mn = []
    mx = []

    for i in range(n):
        mx.append(M[0][i])
        mn.append(M[0][i])

    for i in range(cant):
        for j  in range(n):
            if M[i][j] > mx[j]:
                mx[j]= M[i][j]
            elif M[i][j] < mn[j]:
                mn[j]= M[i][j]    


    R = []
    for j in range(k):
        R.append( np.random.rand(n) )
        for i in range(n):
            R[j][i] = (mx[i] - mn[i])*(R[j][i]-0.5)*(1.5) + (mn[i]+mx[i])/2.0 
            #Se restringe el rango de los pivotes para que no esten tan alejados de los datos

    #print R
    flag =[]
    for i in range(cant):
        flag.append(0)        


    while( True ):
        cambio=0
        for i in range(cant):
            nuevo = fp.asignar( M[i] , R )                    
            if( nuevo != flag[i] ):
                cambio+=1
            flag[i] = nuevo
                
        if cambio==0:
            break;
        R = fp.centroides(flag,M,R)                           
        #print R                

    print(R)
    #print(M)
    num = []
    for i in range(cant):
        num.append(0)
        
    for i in range(cant):
        num[ flag[i] ]+=1

    for i in range(k):
        print( 'CLASE %d : %d elem '%(i,num[i]) )
    #print (flag)                                
    

            
            
if __name__=="__main__" :
    main()


