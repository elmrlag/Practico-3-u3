from ClaseInscripcion import claseInscripcion
import csv
class Taller:
    __idTaller= int
    __nombre= str
    __vacantes=int
    __montoInscripcion=int
    __inscripciones= None
    insActual=0
    def __init__(self,v1,v2,v3,v4):
        self.__idTaller=v1
        self.__nombre=v2
        self.__vacantes=v3
        self.__montoInscripcion=v4
        self.__inscripciones=[]
    @classmethod
    def getinsActual(cls):
        cls.insActual+=1
        return cls.insActual
    def inscribirPersona(self,persona,fecha):
        ins=claseInscripcion(self,persona,fecha,False)
        self.__inscripciones.append(ins)
        self.__vacantes=int(self.__vacantes)
        self.__vacantes-=1
    def mostrarInscriptos(self):
        for acta in self.__actas:
            print(acta)
    def getId(self):
        return(self.__idTaller)
    def getNombre(self):
        return(self.__nombre)
    def getMonto(self):
        return(self.__montoInscripcion)
    def cambiarPago(self,v1):
        for x in range(0,len(self.__inscripciones)):
            if(self.__inscripciones[x].getDNI()==v1):
                self.__inscripciones[x].Pagar()
    def guardar(self):
        with open(f'InscripcionA{self.__nombre}.csv', 'w', newline='') as f:
            thewriter=csv.writer(f)
            thewriter.writerow(["dni","idTaller","fechaInscripcion ","pago"])
            for x in range(0,len(self.__inscripciones)):
                v1=self.__inscripciones[x].getDNI()
                v2=self.__nombre
                v3=self.__inscripciones[x].getFecha()
                v4=self.__inscripciones[x].getPago()
                thewriter.writerow([v1,v2,v3,v4])


