class Persona:
    __nombre=str
    __dir=str
    __dni=str
    __idTaller=int
    def __init__(self,v1,v2,v3,v4):
        self.__nombre=v1
        self.__dir=v2
        self.__dni=v3
        self.__idTaller=v4
    def getDNI(self):
        return(self.__dni)
    def getCurso(self):
        return(self.__idTaller)
    def getNom(self):
        return(self.__nombre)
    def getDir(self):
        return(self.__dir)