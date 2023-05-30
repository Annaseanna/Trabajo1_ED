'''
Clase que se encarga de los metodos del juego como
la interaccion con los puntos, repartir fichas y la generacion de los turnos
'''
#Se importa random para revolver las fichas 
import random
class Juego:
  #Variable de clase que indica que jugador tiene el 6
  tiene6=None 
  #Constructor
  def __init__(self,fichas,maquinas,jugador):
    self.fichas=fichas
    self.maquinas=maquinas
    self.jugador=jugador


#El método showPiezas se encarga de mostrar las piezas del jugador correspondiente, este método tiene una eficiencia O(N)
  def showPiezas(self, L):
    lista = [str(a) for a in L]
    print(''.join(lista))
#Reparte los objetos de fichas a cada jugador
  def repartir(self,fichas,bots,jugador,tablero):
    #Mezcla las fichas. Eficiencia O(n)
    random.shuffle(fichas)
    for i in range(28):
      #Separamos segun los indices
      if i<7:
        #Si tiene el (6|6)
        if fichas[i].suma ==12:
          Juego.tiene6=bots[0]
          #Agrega la ficha al tablero
          tablero.append(fichas[i])
          print(f"Ha jugado {bots[0].nombre}")
          #Muestra el tablero
          self.showPiezas(tablero)     
        else:
          #Agrega las fichas (diferentes al (6|6) al bot 1
          bots[0].piezas.append(fichas[i])
      elif i<14:
        #Si tiene el (6|6)
        if fichas[i].suma ==12:
          Juego.tiene6=bots[1]
          #Agrega la ficha al tablero
          tablero.append(fichas[i])
        else:
          #Agrega las fichas (diferentes al (6|6) al bot 2
          bots[1].piezas.append(fichas[i])
      elif i<21:
        #Si tiene el (6|6)
        if fichas[i].suma ==12:
          Juego.tiene6=bots[2]
          #Agrega la ficha al tablero
          tablero.append(fichas[i])
        else:
          #Agrega las fichas (diferentes al (6|6) al bot 3
          bots[2].piezas.append(fichas[i])    
      else:
        #Si tiene el (6|6)
        if fichas[i].suma ==12:
          Juego.tiene6=jugador
          #Agrega la ficha al tablero
          tablero.append(fichas[i])
        else:
          #Agrega las fichas (diferentes al (6|6) al jugador
          jugador.piezas.append(fichas[i])
    return "Las fichas han sido repartidas"

  #Metodo que se encarga de generar los turnos (O( n))
  def generarTurno(self,bots,jugador):
    #Orden por defecto
    orden = [bots[0],bots[1],bots[2],jugador]
    #Indica el indice del jugador que tiene6
    indice=orden.index(Juego.tiene6)
    #Se realiza un swap con el ultimo de la lista por defecto
    orden[indice],orden[-1]=orden[-1],orden[indice]#O(1)
    print(f"Estan jugando: {orden[-1]}, {orden[0]}, {orden[1]} y {orden[2]}")
    print(f"Ha jugado {orden[-1].nombre}")
    return orden


#El método contarPuntos se encarga de contar los puntos de las piezas del jugador correspondiente, este método tiene una eficiencia O(N)
  def contarPuntos(self,jugador):
    suma = 0
    for ficha in jugador.piezas:
      suma += ficha.suma
    return suma

  #El método contarPuntos se encarga de contar los puntos de las piezas del jugador correspondiente, este método tiene una eficiencia O(n*c) donde c es el numero de jugadores 
  def seleccionarGanador(self,turnos):
    puntaje=100
    for jugador in turnos: #O(c) Solo se recorre 4 veces
      puntaje1=self.contarPuntos(jugador)#O(n)
      if puntaje1<puntaje:
        puntaje=puntaje1
        ganador = jugador    
    return ganador.nombre

  