class Animal():
  totalAnimales=0
  cm=0
  ca=0
  cp=0
  cr=0
  can=0
  def __init__(self, nombre="",edad=0,habitat="",genero="M"):
    self._nombre=nombre
    self._edad=edad
    self._habitat=habitat
    self._genero=genero
    self._zona=[]
    Animal.totalAnimales+=1
  def movimiento(self):
    return "desplazarse"
  @classmethod
  def totalPorTipo(cls):
    return "Mamiferos : "+str(cls.cm)+"\n" + "Aves : "+str(cls.ca)+"\n" + "Reptiles : "+str(cls.cr)+"\n" + "Peces : "+str(cls.cp)+"\n" + "Anfibios : "+str(cls.can)
  def toString(self):
    return "Mi nombre es "+str(self._nombre)+", tengo una edad de " +str(self._edad)+", habito en "+self._habitat+" y mi genero es "+str(self._genero)
  def getHabitat(self): return self._habitat
  def setHabitat(self,a): self._habitat=a
  def getNombre(self): return self._nombre
  def setNombre(self,a): self._nombre=a
  def getEdad(self): return self._edad
  def setEdad(self,a): self._Edad=a
  def getGenero(self): return self._genero
  def setGenero(self,a): self._genero=a
