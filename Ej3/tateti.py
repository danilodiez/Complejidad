tablero = [2,2,2,2,2,2,2,2,2] #2-->Vacio
valores = [8,3,4,1,5,9,6,7,2]
Jugador = []
Maquina = []

def CheckEmpty(n):
	if (tablero[n]==2):
		return 1
	return 0

def Mover(n):
	Maquina.append(n)
	print(n+1)
	tablero[n] = 0

def Hacer2():
	if (tablero[4]==2):
		return 4
	if (tablero[1]==2):
		return 1
	if (tablero[3]==2):
		return 3
	if (tablero[5]==2):
		return 5
	if (tablero[7]==2):
		return 7
	return EmptyPlace()

def EmptyPlace():
	for i in range(10):
		if (tablero[i]==2):
			return i 

def turnos(turno):
	if(turno==1):
		return Mover(0)
	if(turno==2):
		if (tablero[4]==2):
			return Mover(4)
		else:
			Mover(0)
	if (turno==3):
		if (tablero[8]==2):
			return Mover(8)
		else:
			return Mover(3)
	if (turno==4):
		if (PosibleTriunfo(Jugador)!=10):
			return Mover(PosibleTriunfo(Jugador))
		else:
			return Mover(Hacer2())
	if (turno==5):
		if (PosibleTriunfo(Maquina)!=10):
			return Mover(PosibleTriunfo(Maquina))
		else:
			if(PosibleTriunfo(Jugador)!=10):
				return Mover(PosibleTriunfo(Jugador))
			else:
				if (tablero[6]==2):
					return Mover(6)
				else:
					return Mover(2)
	if (turno==6):
		if (PosibleTriunfo(Maquina)!=10):
			return Mover(PosibleTriunfo(Maquina))
		else:
			if (PosibleTriunfo(Jugador)!=10):
				return Mover(PosibleTriunfo(Jugador))
			else:
				return Mover(Hacer2())
	if (turno==7):
		if (PosibleTriunfo(Maquina)!=10):
			return Mover(PosibleTriunfo(Maquina))
		else:
			if (PosibleTriunfo(Jugador)!=10):
				return Mover(PosibleTriunfo(Jugador))
			else: 
				return EmptyPlace()
	if (turno==8):
		if (PosibleTriunfo(Maquina)!=10):
			return Mover(PosibleTriunfo(Maquina))
		else:
			if (PosibleTriunfo(Jugador)!=10):
				return Mover(PosibleTriunfo(Jugador))
			else:
				return EmptyPlace()
	if (turno==9):
		if (PosibleTriunfo(Maquina)!=10):
			return Mover(PosibleTriunfo(Maquina))
		else:
			if (PosibleTriunfo(Jugador)!=10):
				return Mover(PosibleTriunfo(Jugador))
			else:
				return EmptyPlace()

def PosibleTriunfo(lista):
	lenght = len(lista) - 1
	for i in range(lenght):
		suma = valores[lista[i]] + valores[lista[lenght]]
		if (((15 - suma)>0 and (15-suma)<=9) and tablero[valores.index(15-suma)]==2):
			return valores.index(15-suma)
	return 10

print('Elija X o O')
if (input()=='X'): 
	modo = 0 #Empieza el jugador 
else: 
	modo = 1 #Empieza la maquina
for turno in range(1,10):
	if ((modo==0 and turno%2!=0)or(modo==1 and turno%2==0)):
		print('Realice su jugada.')
		jugada = int(input())-1
		while (CheckEmpty(jugada)!=1):
			print('Realice su jugada.')
			jugada = int(input())-1
		Jugador.append(jugada)
		tablero[jugada] = 0
		if (CheckWin(Jugador,turno)==1):
			print('Player Wins')
			break
	else:	
		turnos(turno)	
		if (CheckWin(Maquina,turno)==1):
			print('CPU Wins')
			break
print('Game Over')
