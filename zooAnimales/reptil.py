from .animal import Animal
class Reptil(Animal):
  listado=[]
  iguanas=0
  serpientes=0
  def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
    super().__init__(nombre,edad,habitat,genero)
    self._colorEscamas=colorEscamas
    self._largoCola=largoCola
    Reptil.listado.append(self)
    Animal.cr+=1
  @classmethod
  def cantidadReptiles(cls):
    return len(cls.listado)
  @classmethod
  def crearIguana(cls,nombre,edad,genero):
    cls.iguanas+=1
    return Reptil(nombre,edad,"humedal",genero,"verde",3)
  @classmethod
  def crearSerpiente(cls,nombre,edad,genero):
    cls.serpientes+=1
    return Reptil(nombre,edad,"jungla",genero,"blanco",1)
  def getColorEscamas(self):return self._colorEscamas
  def getLargoCola(self):return self._largoCola
  def movimiento(self):
    return "reptar"