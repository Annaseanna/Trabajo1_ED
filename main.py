'''
Clase que se encarga del control principal del juego, crea los objetos y da los parametros para la finalización de la partida
'''
#Importamos las clases que vamos a usar
from ficha import Ficha
from juego import Juego
from maquina import Maquina
from jugador import Jugador
from collections import deque
from pyfiglet import figlet_format


class main:

  nombre = figlet_format("Domino \nPatoaventuras",font='broadway')
  print(nombre)

  # Actualizar la interfaz gráfica con el estado inicial
  print("¡Bienvenido! ¿Cual es tu nombre?")
  #Crea las 28 fichas 
  fichas = Ficha.crearFichas()
  #Crea las instancias de la clase maquina
  bots = (Maquina("Hugo"),Maquina("Paco"),Maquina("Luis"))
  #Crea la instancia del jugador
  jugador = Jugador(input())
  #Crea la instancia del juego
  juego = Juego(fichas,bots,jugador)
  input('Presiona enter para empezar el juego')
  tablero = deque()
  #Llama al metodo repartir de la clase juego O(n)
  juego.repartir(fichas,bots,jugador,tablero)
  #Generamos los turnos con el metodo de la clase juego O(1)
  turnos = juego.generarTurno(bots,jugador)
  #Contador para turnos
  i = 0
  #Contador para pasadas
  pasadas = 0

  #Si todos tienen al menos una pieza
  while len(jugador.piezas) and len(bots[0].piezas) and len(bots[1].piezas) and len(bots[2].piezas): 
    #Control del ganadpr
    a=0
    print("####### Tablero #######")
    #Muestra las piezas del tablero O(n)
    juego.showPiezas(tablero)
    print()
    #Llama al metodo jugar del bot o del jugador
    jugada = turnos[i].jugar(tablero) #0 si juega, 1 si pasa

    if jugada == 1:
      pasadas +=1
    else:
      pasadas = 0

    #Si los 4 jugadores pasaron
    if pasadas == 4:
      #Cuenta puntos para seleccionar ganador O(n*c) c por la cantidad de jugadores
      ganador=juego.seleccionarGanador(turnos)
      #Cambia el valor de a para que no se generen mas turnos
      a=1
      break
    i +=1
    #Modulo 4 para que no se exceda de la cantidad de jugadores
    i = i%4
  #Generador de turnos
  if a!=1:
    ganador=turnos[i-1]  
  print(f'El ganador del juego es: {ganador}')
