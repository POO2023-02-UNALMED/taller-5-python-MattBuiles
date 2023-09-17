from zooAnimales.animal import Animal
class Zona():
  def __init__(self, nombre="",zoo=None):
    self._nombre = nombre
    self._zoo = zoo
    self._animales=[]
  def agregarAnimales(self,animal):
    self._animales.append(animal)
  def cantidadAnimales(self): return len(self._animales)
  def getAnimales(self): return self._animales
  def getZoo(self): return self._zoo
  def getNombre(self): return self._nombre