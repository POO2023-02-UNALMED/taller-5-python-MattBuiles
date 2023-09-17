from animal import Animal
class Anfibio(Animal):
  listado=[]
  ranas=0
  salamandras=0
  def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
    super().__init__(nombre,edad,habitat,genero)
    self._colorPiel=colorPiel
    self._venenoso=venenoso
    Anfibio.listado.append(self)
    super.totalAnimales+=1
  @classmethod
  def cantidadAnfibio(cls):
    return len(cls.listado)
  @classmethod
  def crearRana(cls,nombre,edad,genero):
    cls.ranas+=1
    return Anfibio(nombre,edad,"selva",genero,"rojo",True)
  @classmethod
  def crearSalamandra(cls,nombre,edad,genero):
    cls.salamandras+=1
    return Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
  def isVenenoso(self):return self._venenoso
  def getColorPiel(self):return self._colorPiel