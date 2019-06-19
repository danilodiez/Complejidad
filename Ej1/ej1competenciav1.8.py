import time
from functools import lru_cache

@lru_cache(None)

def sumdivisores(n):
    aux=n
    suma=1
    factor=2
    if n % factor == 0:     #si el valor en el que el factor quedo es valido, multiplicamos el factor por si mismo, y reducimos el numero siendo factorizado
        potencia=factor*factor
        n=n//factor
        while (n % factor) ==0:  #aca factorizamos
            potencia=potencia*factor
            n=n//factor
        suma=suma*(potencia-1) #Aca multiplicamos el valor por el resultado de la factorizacion
        suma=suma//(factor-1)
    factor=3
    while (factor*factor)<=n and n>1:#continuamos hasta que el valor por el cual factorizamos sea menor que la raiz cuadrada del numero 
        if n % factor == 0:     #si el valor en el que el factor quedo es valido, multiplicamos el factor por si mismo, y reducimos el numero siendo factorizado
            potencia=factor*factor
            n=n//factor
            while (n % factor) ==0:  #aca factorizamos
                potencia=potencia*factor
                n=n//factor
            suma=suma*(potencia-1) #Aca multiplicamos el valor por el resultado de la factorizacion
            suma=suma//(factor-1)#Aca continua la aplicacion de la formula p^a=p^(a+1)-1 / (p-1)
                   #a que realmente, no estamos calculando los primos. Esto se explica debajo
        factor=factor+2
    if n>1:
        suma=suma*(n+1)
    return suma-aux


def amigos(maxim):
    start=time.time()
    lista=[]
    for k in range(2,maxim):
        if k % 2 == 0 or k % 5 ==0:
            sumaa=sumdivisores(k)
            if k < sumaa:  #elimina cuadrados perfectos y bastantes calculos innecesarios
                sumab=sumdivisores(sumaa)
                if(sumab==k):
                    lista.append(k)
                    lista.append(sumaa)
    end=time.time()
    print(end-start)
    return lista

m=input('Ingrese un valor maximo: ')
print(amigos(m))
