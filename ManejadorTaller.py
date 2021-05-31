from ClaseTaller import Taller
import csv
class manejadorTaller:
    __talleres=[]

    def __init__(self,Leer):
        if (Leer==True):
            titulo = True
            archivo1 = open("Talleres.csv")
            reader = csv.reader(archivo1, delimiter=",")
            for fila in reader:
                if titulo == False:
                    v1 = fila[0]
                    v2 = fila[1]
                    v3 = fila[2]
                    v4 = fila[3]
                    taller = Taller(v1, v2, v3, v4)
                    self.__talleres.append(taller)
                if titulo == True:
                    titulo = False
            archivo1.close()
        else:
            __talleres=[]
    def crearArchivo(self):
        #archivo=open("Talleres.csv","w")
        with open('Talleres.csv', 'w', newline='') as f:
            thewriter=csv.writer(f)
            thewriter.writerow(["Id","Nombre","Vacantes","Inscripcion"])
            bandera=input("Ingrese el nombre del taller(escriba listo para finalizar):")
            while(bandera!="listo"):
                v1=input("Ingrese la id del taller: ")
                v2=input("ingrese la cantidad de vacantes: ")
                v3=input("ingrese el monto de inscripcion:")
                taller=Taller(v1,bandera,v2,v3)
                self.__talleres.append(taller)
                thewriter.writerow([v1,bandera,v2,v3])
                bandera=input("Ingrese el nombre del taller(escriba listo para finalizar):")
        #archivo.close()
    def buscarTaller(self,v1):
        for x in range(0,len(self.__talleres)):
            if (self.__talleres[x].getId()==v1):
                return(x)
    def buscarNombreTaller(self,v1):
        for x in range(0,len(self.__talleres)):
            v2=int(self.__talleres[x].getId())
            if (v2==v1):
                print(f"La persona esta inscripto en {self.__talleres[x].getNombre()} y adeuda {self.__talleres[x].getMonto()}")
    def AgregarPersona(self,v1,persona,fecha):
        x=self.buscarTaller(v1)
        self.__talleres[x].inscribirPersona(persona,fecha)
    def Pagar(self,v1):
        for x in range(0,len(self.__talleres)):
            self.__talleres[x].cambiarPago(v1)
    def generarArchivo(self):
        for x in range(0,len(self.__talleres)):
            self.__talleres[x].guardar()
