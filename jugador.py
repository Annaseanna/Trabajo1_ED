'''
Clase que se encarga de definir los atributos del jugador y dar las funcionalidades para que este pueda jugar sus piezas
'''
class Jugador:
  #Constructor de la clase jugador
  def __init__(self,nombre):
    self.nombre=nombre
    self.piezas=[]

  #Duplicamos el método para que funcionara tanto para el tablero como para las fichas but toca modificar el que ya tenía solo las fichas O(n)
  def showPiezas(self):
    lista = [str(a) for a in self.piezas]
    print(''.join(lista))

  #toString para el nombre del jugador
  def __str__(self):
    return self.nombre

  def logicaJugar(self,tablero,n):
    #Controla el lado del tablero donde se juega
    option=""
    if (tablero[0].n1 == self.piezas[n].n1 or tablero[0].n1 == self.piezas[n].n2) and (tablero[-1].n2 == self.piezas[n].n1 or tablero[-1].n2 == self.piezas[n].n2):
      option=input("seleccione el lado en el que quiere colocar la ficha: I(izquierda) o D(Derecha)")
      #Si la opcion es izquierda
      if option=="I" or option=="i":
        if tablero[0].n1 == self.piezas[n].n1:
          #Cambiamos el setter de las piezas del jugador
          self.piezas[n].setN1N2(self.piezas[n].n2,self.piezas[n].n1)
          #Agregamos a la izquierda del tablero y la quitamos de las piezas del jugador O(n)
          tablero.appendleft(self.piezas.pop(n))  
        elif tablero[0].n1 == self.piezas[n].n2:
          #Agregamos a la izquierda del tablero y la quitamos de las piezas del jugador O(n)
          tablero.appendleft(self.piezas.pop(n))
      #Si la condicion es derecha
      elif option=="D" or option=="d":
        if tablero[-1].n2 == self.piezas[n].n1:
          #Agregamos a la derecha del tablero y la quitamos de las piezas del jugador O(n)
          tablero.append(self.piezas.pop(n))
        elif tablero[-1].n2 == self.piezas[n].n2:
          #Cambiamos el setter de las piezas
          self.piezas[n].setN1N2(self.piezas[n].n2,self.piezas[n].n1)
          #Agregamos a la derecha del tablero y la quitamos de las piezas del jugador O(n)
          tablero.append(self.piezas.pop(n))

    #Condiciones cuando solo se pueden jugar las piezas en un lado del tablero
    elif tablero[0].n1 == self.piezas[n].n1:
      self.piezas[n].setN1N2(self.piezas[n].n2,self.piezas[n].n1) #Alteramos el setter
      #Agregamos a la izquierda del tablero y la quitamos de las piezas del jugador O(n)
      tablero.appendleft(self.piezas.pop(n))  
    elif tablero[0].n1 == self.piezas[n].n2:
      #Agregamos a la izquierda del tablero y la quitamos de las piezas del jugador O(n)
      tablero.appendleft(self.piezas.pop(n))
    elif tablero[-1].n2 == self.piezas[n].n1:
      #Agregamos a la derecha del tablero y la quitamos de las piezas del jugador O(n)
      tablero.append(self.piezas.pop(n))
    elif tablero[-1].n2 == self.piezas[n].n2:                     
      self.piezas[n].setN1N2(self.piezas[n].n2,self.piezas[n].n1) #Alteramos el setter
      #Agregamos a la derecha del tablero y la quitamos de las piezas del jugador O(n)
      tablero.append(self.piezas.pop(n))
    else:
      print('no puedes jugar esa pieza, intenta con otra.')
      return True
    print(f'{self.nombre} has jugado. Quedaste con {len(self.piezas)} piezas')
    return False

  #Metodo que permite al jugador poner 1 o 2 piezas 
  def jugar(self, tablero):
    x=True
    print(f"<----------- Tu turno {self.nombre} ----------->")
    while x: #Si juega bien es O(1) si no depende de las c veces que juegue mal O(n*c)
      print("Estas son tus piezas:")
      #Muestra las fichas por jugador
      self.showPiezas() 
      n = int(input('¿Cual ficha deseas jugar?(ingresa el índice correspondiente) \n ó ingresa: \n -1) Para pasar \n  9) Para tapicui \n'))
      #Si elige pasar
      if n == -1:
        print(f"{self.nombre} acabas de pasar. Tienes {len(self.piezas)} piezas")
        return 1
      #Si elige hacer tapicui
      elif n == 9:
        #Toma los indices de las dos fichas que quiere jugar
        a,b = map(int,input('¿Cuales fichas deseas jugar (ingresar los índices con espacio entre sí)?').split())
        #Valida primero si ambas fichas son pares
        if self.piezas[a].n1==self.piezas[a].n2 and self.piezas[b].n1==self.piezas[b].n2:
          #Llama al metodo logicaJugar(O(n))
          a1=self.logicaJugar(tablero,a)
          #Si se jugo una ficha
          if not a1:
            #Vuelve a llamar a la funcion con el segundo par
            a2=self.logicaJugar(tablero,b-1)
          #Hace el print cuando se jueguen las dos
          if not a1 and not a2:
            print(f"{self.nombre}, has hecho un tapicui.Yujuuu!. Tienes {len(self.piezas)} piezas")
            break
        #Ingreso indices de fichas que no sirven ara el tapicui
        else:
          print("No es una ficha valida para hacer tapicui")
      #Se vuelve a llamar a logica jugar que es O(n)
      else:
        x=self.logicaJugar(tablero,n)

      
