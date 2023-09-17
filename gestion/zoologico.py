class Zoologico():
  def __init__(self, nombre="",ubicacion=""):
    self._nombre = nombre
    self._ubicacion = ubicacion
    self._zonas=[]
  def agregarZonas(self,zona):
    self._zonas.append(zona)
  def cantidadTotalAnimales(self):
    total=0
    for zone in self._zonas:
      total+=zone.cantidadAnimales()
    return total
  def getNombre(self): return self._nombre
  def getUbicacion(self): return self._ubicacion
  def getZona(self): return self._zonas