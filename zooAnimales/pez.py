from animal import Animal
class Pez(Animal):
  listado=[]
  salmones=0
  bacalaos=0
  def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidadAletas):
    super().__init__(nombre,edad,habitat,genero)
    self._colorEscamas=colorEscamas
    self._cantidadAletas=cantidadAletas
    Pez.listado.append(self)
    super.totalAnimales+=1
  @classmethod
  def cantidadPeces(cls):
    return len(cls.listado)
  @classmethod
  def crearSalmon(cls,nombre,edad,genero):
    cls.salmones+=1
    return Pez(nombre,edad,"oceano",genero,"rojo",6)
  @classmethod
  def crearBacalao(cls,nombre,edad,genero):
    cls.bacalaos+=1
    return Pez(nombre,edad,"oceano",genero,"gris",6)
  def getColorEscamas(self):return self._colorEscamas
  def getCantidadAletas(self):return self._cantidadAletas