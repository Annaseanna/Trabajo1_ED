'''
Clase que se encarga de dar los atributos a las fichas y generar sus instancias 
'''
class Ficha:
  #Constructor de la clase
  def __init__(self,n1,n2):
    self.n1=n1
    self.n2=n2
    self.suma= n1+n2

  #Setter de valores para cada lado
  def setN1N2(self,n1,n2):
    self.n1=n1
    self.n2=n2
    
#El método crearFichas se encarga de crear todas las fichas como objetos dentro de un arreglo de redimensionamiento
  def crearFichas():
    fichas = [Ficha(0,0),
            Ficha(0,1),
            Ficha(0,2),
            Ficha(0,3),
            Ficha(0,4),
            Ficha(0,5),
            Ficha(0,6),
            Ficha(1,1),
            Ficha(1,2),
            Ficha(1,3),
            Ficha(1,4),
            Ficha(1,5),
            Ficha(1,6),
            Ficha(2,2),
            Ficha(2,3),
            Ficha(2,4),
            Ficha(2,5),
            Ficha(2,6),
            Ficha(3,3),
            Ficha(3,4),
            Ficha(3,5),
            Ficha(3,6),
            Ficha(4,4),
            Ficha(4,5),
            Ficha(4,6),
            Ficha(5,5),
            Ficha(5,6),
            Ficha(6,6)]
    return fichas

  #Metodo toString de la clase ficha
  def __str__(self):
    return f'({self.n1}|{self.n2})'