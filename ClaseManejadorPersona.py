from ClasePersona import Persona
from ClaseTaller import Taller
class manejadorPersona:
    __personas=[]
    def __init__(self):
        self.__personas=[]
    def agregarPersona(self,id):
        v1=input("Ingrese el nombre de la persona que desea inscribir: ")
        v2=input("Ingrese la direccion de la persona que desea inscribir: ")
        v3=input("Ingrese el dni persona que desea inscribir: ")
        p1=Persona(v1,v2,v3,id)
        self.__personas.append(p1)
        return(p1)
    def buscarTaller(self,dni):
        for x in range(0,len(self.__personas)):
            if (self.__personas[x].getDNI() == dni):
                DNI=int(self.__personas[x].getCurso())
                return(DNI)
    def ListarXId(self,id):
        print("DNI \t\t Nombre \t Direccion")
        for x in range(0,len(self.__personas)):
            if (self.__personas[x].getCurso() == id):
                print(f"{self.__personas[x].getDNI()} \t\t {self.__personas[x].getNom()} \t\t {self.__personas[x].getDir()}")