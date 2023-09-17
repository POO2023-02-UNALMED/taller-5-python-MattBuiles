from gestion.zona import Zona
from mamifero import Mamifero
from ave import Ave
from pez import Pez
from reptil import Reptil
from anfibio import Anfibio
class Animal():
  totalAnimales=0
  def __init__(self, nombre="",edad=0,habitat="",genero="M"):
    self._nombre=nombre
    self._edad=edad
    self._habitat=habitat
    self._genero=genero
    self._zona=[]
    totalAnimales+=1
  def movimiento(self,mensaje="desplazarse"):

    if isinstance(self,Anfibio):return "saltar"
    elif isinstance(self,Ave):return "volar"
    elif isinstance(self,Reptil):return "reptar"
    elif isinstance(self,Pez):return "nadar"
    else: return "desplazarse"

    #return mensaje
  def totalPorTipos(self):
    return "Mamiferos: "+str(Mamifero.cantidadMamiferos())+"\n" + "Aves: "+str(Ave.cantidadAves())+"\n" + "Reptiles: "+str(Reptil.cantidadReptiles())+"\n" + "Peces: "+str(Pez.cantidadPeces())+"\n" + "Anfibios: "+str(Anfibio.cantidadAnfibios())
  def __str__(self):
    return "Mi nombre es "+self._nombre+", tengo una edad de " +self._edad+", habito en "+self._habitat+" y mi genero es "+self._genero
  def getHabitat(self): return self._habitat
  def setHabitat(self,a): self._habitat=a
  def getNombre(self): return self._nombre
  def setNombre(self,a): self._nombre=a
  def getEdad(self): return self._edad
  def setEdad(self,a): self._Edad=a
  def getGenero(self): return self._genero
  def setGenero(self,a): self._genero=a
