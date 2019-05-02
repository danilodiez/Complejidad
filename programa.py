
import xlrd
from pandas import *
from numpy import *

my_sheet 	= 'Hoja1'

def buscarSuc(idSuc):
	file_name 	= 'sucursales.xlsx' 
	sucursales 	= read_excel(file_name, sheet_name = my_sheet)
	sucursales 	= sucursales.values

	i=0
	while (idSuc != sucursales[i][0]):
		i+=1
	nombreSuc = sucursales[i][1]
	return nombreSuc

def buscarReposicion(idArt):
	for i in array:
		if(i[1]==idArt):
			if(i[2]>5):
				print('La sucursal ',buscarSuc(i[0]),' puede reponer')

def buscarArt(idArt):
	file_name 	= 'articulos.xlsx' 
	articulos 	= read_excel(file_name, sheet_name = my_sheet)
	articulos 	= articulos.values

	i=0
	while (idArt != articulos[i][0]):
		i+=1
	
	nombreArt = articulos[i][1]
	return nombreArt



file_name 	= 'contSucArt.xlsx' 
contSucArt 	= read_excel(file_name, sheet_name = my_sheet, header=0)

array = contSucArt.values 

i=0
while i < (len(array)):
	
	if (array[i][2]==0):
		
		idSuc=array[i][0]	
		idArt = array[i][1]	
		print ("--------------La sucursal ", buscarSuc(idSuc), " no posee: ", buscarArt(idArt),'-------------------------')
		

		#BUSCAR REPONEDOR
		buscarReposicion(idArt)
		print("**********************************************************************")

		

	#INCREMENTAR i EN BUCLE SUPERIOR
	i+=1


	
	

