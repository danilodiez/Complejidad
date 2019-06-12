import xlrd
from pandas import *
from numpy import *
import generarExcel
import time

my_sheet 	= 'Sheet1'

def buscarReposicion(idArt):
	for i in array:
		if(i[1]==idArt):
			if(i[2]>5):
				print('La sucursal ',i[0],' puede reponer')

generarExcel.generarXLSX()

file_name 	= 'contSucArt.xlsx' 
contSucArt 	= read_excel(file_name, sheet_name = my_sheet, header=0)

array = contSucArt.values 
inicio=time.time()
i=0
flag=False
while i < (len(array)):
	
	if (array[i][2]==0):
		
		idSuc=array[i][0]	
		idArt = array[i][1]	
		print ("--------------La sucursal ", int(idSuc), " no posee: ", int(idArt),'-------------------------')
		flag=True

		#BUSCAR REPONEDOR
		buscarReposicion(idArt)
		print("**********************************************************************")

	#INCREMENTAR i EN BUCLE SUPERIOR
	i+=1

if flag==False:
	print("No hay problemas de stock en las sucursales")
fin=time.time()
print('Tiempo total: ', (fin-inicio),' segundos')
