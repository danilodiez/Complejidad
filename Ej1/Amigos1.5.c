#include    <stdlib.h>
#include    <stdio.h>
#include    <math.h>
#include <time.h>

void printarray(int array[]);
long int sumadivisores(long int,long int, long int);
int *amigos(int arreglo[],int maxelem);

int main ()
{
    int arreglo[600];
    int cant;
    printf("Ingresar cantidad de numeros a analizar\n");
    scanf("%d",&cant);
    amigos(arreglo,cant);
    printarray(arreglo);

    return 0;
}

long int sumadivisores(long int a,long int cont,long int step)
{
    long int i,raiz,sumador=1;
    raiz=sqrt(a);
    for (i=cont; i <=raiz ; i+=step )
    {
        if ((a % i)==0 && i!=a/i)
        {
            sumador += i + a/i;
        }
    }
    return sumador;
}

int *amigos(int arreglo[],int maxelem)
{
    int cantidad=0;
    clock_t t_ini,t_fin;
    double secs;
    t_ini=clock();
    long int i,indice=1;
    long int sumaa, sumab, cont, step;
    for (i=1; i<maxelem;i++ )
    {

        if (i%2!=0)
        {
            cont=3;
            step=2;
        }
        else
        {
            cont=2;
            step=1;
        }
        sumaa = sumadivisores(i,cont,step);
        if(i < sumaa)
        {
          sumab = sumadivisores(sumaa,cont,step);
          if (sumab==i)
          {
            arreglo[indice]=i;
            indice++;
            arreglo[indice]=sumaa;
            indice++;
            cantidad=cantidad+2;
          }
        }

    }
    t_fin=clock();
    secs=(double)(t_fin - t_ini)/CLOCKS_PER_SEC;
    printf("%.16g segundos\n",secs);
    arreglo[0]=cantidad+1;
    return arreglo;
}
void printarray(int array[])
{
    int i,length=array[0];
    for(i=1;i<length;i++)
    {
        printf("%d \n",array[i]);
    }
}
