'''
Clase que se encarga de los metodos del juego como
la interaccion con los puntos, repartir fichas y la generacion de los turnos
'''
#Importamos libreria para el tiempo
from time import sleep
class Maquina:
  #Constructor de la clase maquina
  def __init__(self,nombre):
    self.nombre=nombre
    self.piezas=[]
  #toString del atributo nombre  
  def __str__(self):
    return self.nombre

  #Metodo que se encarga de dar la posibilidad de jugar a la maquina 
  def jugar(self,tablero):
    print(f"<----------- {self.nombre} ----------->")
    #Alertas que se activan si son fichas del tapicui
    alerta1=False
    alerta2=False
    #Se utiliza en jugadas normales
    d = 0
    #Se utiliza para sacar primero las dobles
    p = 0
    #Identifica la mas pesada
    suma = -1
    izq = tablero[0].n1 #Lado izquierdo del tablero 
    der = tablero[-1].n2 #Lado derecho del tablero
    #O(n^2) porque recorre todas las fichas y hace pop
    for i in range(len(self.piezas)):
      n1 = self.piezas[i].n1 
      n2 = self.piezas[i].n2
      #tapicui
      if n1 == izq and n2 == izq:
        #Alerta activa si se puede tapicui
        alerta1=True
        #Almacenamos el indice
        jugada1=i
      elif n2 == der and n1 == der:
        #Alerta activa si se puede tapicui
        alerta2=True
        #Almacenamos el indice
        jugada2=i

      #jugada dobles
      if n1==n2:
        if n1 == izq:
          jugada3 = i #Almacenamos el indice
          p = 1 #Nos dirige a una la opcion para quitar y agregar la pieza al tablero
        elif n1 == der:
          jugada3 = i #Almacenamos el indice
          p = 2 #Nos dirige a una la opcion para quitar y agregar la pieza al tablero

      #jugada normal
      #Siempre obtiene la ficha mas pesada 
      if self.piezas[i].suma > suma:   
        if n1 == izq:
          #Actualiza el valor de la variable suma
          suma = self.piezas[i].suma
          jugada = i #Almacenamos el indice
          d = 1 #Nos dirige a una la opcion para quitar y agregar la pieza al tablero de la jugada normal
        elif n2 == izq:
          suma = self.piezas[i].suma
          jugada = i #Almacenamos el indice
          d = 2 #Nos dirige a una la opcion para quitar y agregar la pieza al tablero de la jugada normal
        elif n1 == der:
          suma = self.piezas[i].suma
          jugada = i #Almacenamos el indice
          d = 3 #Nos dirige a una la opcion para quitar y agregar la pieza al tablero de la jugada normal
        elif n2 == der:
          suma = self.piezas[i].suma
          jugada = i #Almacenamos el indice
          d = 4 #Nos dirige a una la opcion para quitar y agregar la pieza al tablero de la jugada normal

    #tapicui
    if alerta1 and alerta2:
      #Agregamos a la izquierda y se la sacamos al bot (O(n))
      tablero.appendleft(self.piezas.pop(jugada1))
      #Agregamos a la derecha y se la sacamos al bot (O(n))
      tablero.append(self.piezas.pop(jugada2))
      print(f"El bot {self.nombre} hizo tapicui. Tiene {len(self.piezas)} piezas")
      return 0

    
    #Primero dobles
    elif p==1:
      #Agregamos la ficha a la izquierda y se la sacamos al bot (O(n))
      tablero.appendleft(self.piezas.pop(jugada3))
    elif p==2:
      #Agregamos la ficha a la derecha y se la sacamos al bot (O(n))
      tablero.append(self.piezas.pop(jugada3))
    
    #jugada normal
    elif d == 1:
      #Cambiamos el setter para que quede inverso el orden
      self.piezas[jugada].setN1N2(self.piezas[jugada].n2,self.piezas[jugada].n1)
      #Agregamos la ficha a la izquierda y se la sacamos al bot (O(n))
      tablero.appendleft(self.piezas.pop(jugada))
    elif d == 2:
      #Agregamos la ficha a la izquierda y se la sacamos al bot (O(n))
      tablero.appendleft(self.piezas.pop(jugada))
    elif d == 3:
      #Agregamos la ficha  a la derecha y se la sacamos al bot (O(n))
      tablero.append(self.piezas.pop(jugada))
    elif d == 4:
      #Cambiamos el setter para que quede inverso el orden
      self.piezas[jugada].setN1N2(self.piezas[jugada].n2,self.piezas[jugada].n1)
      #Agregamos la ficha  a la derecha y se la sacamos al bot (O(n))
      tablero.append(self.piezas.pop(jugada))
      
    else:
      print(f"El bot {self.nombre} paso. Tiene {len(self.piezas)} piezas")
      #Retorna 1 si pasa 
      sleep(2)
      return 1
    print(f'El bot {self.nombre} ha jugado. Quedo con {len(self.piezas)} piezas')
    sleep(2)
    return 0
    