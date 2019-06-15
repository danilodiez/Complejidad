from os import system, name
tablero = [2, 2, 2, 2, 2, 2, 2, 2, 2]  # 2-->Vacio
valores = [8, 3, 4, 1, 5, 9, 6, 7, 2]
tableroprin = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

def limpia():
	if name == 'nt':
		_=system('cls')
	else:
		_=system('clear')

def tablerof():
    print(str(tableroprin[0])+" "+str(tableroprin[1])+" "+str(tableroprin[2]))
    print(str(tableroprin[3])+" "+str(tableroprin[4])+" "+str(tableroprin[5]))
    print(str(tableroprin[6])+" "+str(tableroprin[7])+" "+str(tableroprin[8]))


def Avido(modo):
    Maquina = []
    Jugador = []
    ultimo = []
    turno = 1
    while turno < 10 and not Win(ultimo):
        if ((modo == 0 and turno % 2 != 0)or(modo == 1 and turno % 2 == 0)):
            limpia()
            print('Realice su jugada.')
            tablerof()
            jugada = int(input())-1
            while (CheckEmpty(jugada) != 1):
                print('Realice su jugada.')
                jugada = int(input())-1
            if(modo == 0):
                tableroprin[jugada] = 'X'
            else:
                if modo == 1:
                    tableroprin[jugada] = 'O'
            Jugador.append(valores[jugada])
            tablero[jugada] = 0
            ultimo = Jugador
        else:
            Mover(SeleccionCandidato(turno, Jugador, Maquina), Maquina, modo)
            ultimo = Maquina
        turno += 1
        
        


def CheckEmpty(n):
    if (tablero[n] == 2):
        return True
    return False


def Mover(n, Maquina, modo):
    Maquina.append(valores[n])
    if modo == 0:
        tableroprin[n] = 'O'
    if modo == 1:
        tableroprin[n] = 'X'
    tablero[n] = 0


def EmptyPlace():
    for i in range(10):
        if (tablero[i] == 2):
            return i


def Lados():
    if (CheckEmpty(4)):
        return 4
    if (CheckEmpty(1)):
        return 1
    if (CheckEmpty(3)):
        return 3
    if (CheckEmpty(5)):
        return 5
    if (CheckEmpty(7)):
        return 7
    return EmptyPlace()


def SeleccionCandidato(turno, Jugador, Maquina):
    if(turno == 1):
        return 0
    if(turno == 2):
        if (CheckEmpty(4)):
            return 4
        else:
            return 0
    if (turno == 3):
        if (CheckEmpty(8)):
            return 8
        else:
            return 3
    if (turno == 4):
        if (PosibleTriunfo(Jugador) != 10):
            return PosibleTriunfo(Jugador)
        else:
            return Lados()
    if (turno == 5):
        if (PosibleTriunfo(Maquina) != 10):
            return PosibleTriunfo(Maquina)
        else:
            if(PosibleTriunfo(Jugador) != 10):
                return PosibleTriunfo(Jugador)
            else:
                if (tablero[6] == 2):
                    return 6
                else:
                    return 2
    if (turno == 6):
        if (PosibleTriunfo(Maquina) != 10):
            return PosibleTriunfo(Maquina)
        else:
            if (PosibleTriunfo(Jugador) != 10):
                return PosibleTriunfo(Jugador)
            else:
                return Lados()
    if (turno == 7):
        if (PosibleTriunfo(Maquina) != 10):
            return PosibleTriunfo(Maquina)
        else:
            if (PosibleTriunfo(Jugador) != 10):
                return PosibleTriunfo(Jugador)
            else:
                return EmptyPlace()
    if (turno == 8):
        if (PosibleTriunfo(Maquina) != 10):
            return PosibleTriunfo(Maquina)
        else:
            if (PosibleTriunfo(Jugador) != 10):
                return PosibleTriunfo(Jugador)
            else:
                return EmptyPlace()
    if (turno == 9):
        return EmptyPlace()


def PosibleTriunfo(lista):
    lenght = len(lista) - 1
    for i in range(lenght):
        suma = lista[i] + lista[lenght]
        if (((15 - suma) > 0 and (15-suma) <= 9) and CheckEmpty(valores.index(15-suma))):
            return valores.index(15-suma)
    return 10


def Win(lista):
    if (len(lista) > 2):
        tres = len(lista) - 1
        dos = tres - 1
        uno = dos - 1
        while (dos > 0):
            while (uno >= 0):
                if (lista[uno]+lista[dos]+lista[tres] == 15):
                    return True
                uno -= 1
            dos -= 1
            uno = dos - 1
    return False


print('Elija X o O')
if (input() == 'X'):
    Avido(0)  # Empieza el jugador
else:
    Avido(1)  # Empieza la maquina
print('Game Over')
