#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>
#include <errno.h>

extern int errno;
const char consonantes[22]={'b','c','d','e','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'};
const char vocales[5]={'a','e','i','o','u'};
int indexe[6]={0,0,0,0,0,0};

char *generar_nombres(char nuevonombre[])
{
    int count;
    nuevonombre[6]='\0';
    for(count=0;count<6;count=count+2)
    {
       nuevonombre[count]=consonantes[indexe[count]];
       nuevonombre[count+1]=vocales[indexe[count+1]];
    }
    if(indexe[5]==4)
    {
        indexe[5]=0;
        indexe[4]++;
    }
    else indexe[5]++;
    if(indexe[4]==22)
    {
        indexe[4]=0;
        indexe[3]++;
    }
    if(indexe[3]==4)
    {
        indexe[3]=0;
        indexe[2]++;
    }
    if(indexe[2]==22)
    {
        indexe[2]=0;
        indexe[1]++;
    }
    if(indexe[1]==4)
    {
        indexe[1]=0;
        indexe[0]++;
    }
    if(indexe[0]==22)
    {
       indexe[0]=0;
    }
    nuevonombre[0]=toupper(nuevonombre[0]);
    return nuevonombre;
}
struct sucursales{
    int id;
    char nombre[20];
};
struct articulos
{
    unsigned int id;
    char nombre[7];
};
struct artxSucursal
{
    unsigned int id;
    unsigned int idsucursal;
    unsigned int idarticulo;
    unsigned int cantidad;
};
struct articulos tablaArticulos[200000];
struct sucursales tablaSucursales[200];
struct artxSucursal tablaArtxSucur[4000000];
void imprimeArtxSucur(struct artxSucursal tabla[], unsigned int longiTabla)
{
    printf("      ID   ID-S   ID-A   Stock\n");
    printf("--------------------------------------------------------\n");
    int k;
    for(k=0;k<longiTabla;k++)
    {
        printf("%8d%6d%7d%6d \n",tabla[k].id, tabla[k].idsucursal, tabla[k].idarticulo,tabla[k].cantidad);
    }
}
void imprimesucursales(struct sucursales tabla[], unsigned int longiTabla)
{
    printf("  ID   NombreSucursal\n");
    printf("------------------------\n");
    int k;
    for(k=0;k<longiTabla;k++)
    {
        printf("%6d    %s \n",tabla[k].id, tabla[k].nombre);
    }
}
void imprimearticulos(struct articulos tabla[], unsigned int longiTabla)
{
    printf("  ID   NombreArticulo\n");
    printf("------------------------\n");
    int k;
    for(k=0;k<longiTabla;k++)
    {
        printf("%6d    %s \n",tabla[k].id, tabla[k].nombre);
    }
}
int main()
{
    srand(time(NULL));
    char nombre[7];
    unsigned int cont=0,cont2;
    long unsigned int numArticulos, numSucursales, numArtxSucur;
    printf("Inserte numero de articulos. No superar los 200 mil. Tenga piedad de su RAM\n");
    scanf("%lu",&numArticulos);
    while(cont<numArticulos)
    {
        tablaArticulos[cont].id=cont;
        strcpy(tablaArticulos[cont].nombre,generar_nombres(nombre));
        cont=cont+1;
    }
    //imprimearticulos(tablaArticulos,numArticulos);
    printf("Inserte numero de sucursales. No superar las 200\n");
    scanf("%lu",&numSucursales);
    cont=0;
    numArtxSucur=numArticulos*numSucursales;
    while(cont < numSucursales)
    {
        tablaSucursales[cont].id=cont;
        strcpy(tablaSucursales[cont].nombre,generar_nombres(nombre));
        cont++;
    }
    //imprimesucursales(tablaSucursales,numSucursales);
    printf("Generando tabla\n");
    int auxsucursal=0;
    int auxarticulo=0;
    for(cont=0;cont<numArtxSucur;cont++)
    {
        tablaArtxSucur[cont].id=cont;
        tablaArtxSucur[cont].idsucursal=auxsucursal;
        tablaArtxSucur[cont].idarticulo=auxarticulo;
        tablaArtxSucur[cont].cantidad=rand()%20;
        auxarticulo++;
        if(auxarticulo==numArticulos)
        {
            auxarticulo=0;
            auxsucursal++;
        }

    }
    imprimeArtxSucur(tablaArtxSucur,numArtxSucur);
    getchar();
    getchar();
    return 0;
}
