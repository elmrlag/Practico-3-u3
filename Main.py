from ClaseTaller import Taller
from ClasePersona import Persona
from ManejadorTaller import manejadorTaller
from ClaseManejadorPersona import manejadorPersona
if __name__=='__main__':
    x=input("Decea crear el archivo (si o no): ")
    if (x=="si"):
        Talleres=manejadorTaller(False)
        Talleres.crearArchivo()
    else:
        Talleres=manejadorTaller(True)
    Personas=manejadorPersona()
    id=input("Ingrese el id del taller que se desea inscribir: ")
    persona=Personas.agregarPersona(id)
    v2=input("Ingrese la fecha de la inscripcion: ")
    Talleres.AgregarPersona(id,persona,v2)
    v1=input("Ingrese el DNI de la Persona para saber en que curso esta inscripto: ")
    taller=Personas.buscarTaller(v1)
    Talleres.buscarNombreTaller(taller)
    v1=input("Ingrese la id del taller para saber los datos de los alumnos: ")
    Personas.ListarXId(v1)
    v1=input("Ingrese el DNI de la persona para pagar lo que adeuda: ")
    Talleres.Pagar(v1)
    Talleres.generarArchivo()
    