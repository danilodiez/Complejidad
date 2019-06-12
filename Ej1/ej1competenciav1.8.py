import time
def sumdivisores(n):
    aux=n
    suma=1
    p=2
    while (p*p)<=n and n>1:
        if n % p == 0:
            j=p*p
            n=n//p
            while (n % p) ==0:
                j=j*p
                n=n//p
            suma=suma*(j-1)
            suma=suma//(p-1)
        if p==2:
            p=3
        else:
            p=p+2
    if n>1:
        suma=suma*(n+1)
    return suma-aux

start=time.time()
maxim=1000000
lista=[]
for k in range(2,maxim):
    if k % 2 == 0 or k % 5 ==0:
        sumaa=sumdivisores(k)
        if k < sumaa:
            sumab=sumdivisores(sumaa)
            if(sumab==k):
                lista.append(k)
                lista.append(sumaa)
end=time.time()
print(end-start)
print(lista)


