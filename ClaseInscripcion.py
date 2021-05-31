class claseInscripcion:
    __taller=None
    __persona=None
    __fechaInscripcion=str
    __pago=bool
    def __init__(self,v1,v2,v3,v4):
        self.__taller=v1
        self.__persona=v2
        self.__fechaInscripcion=v3
        self.__pago=v4
    def Pagar(self):
        self.__pago=True
    def getDNI(self):
        return(self.__persona.getDNI())
    def getFecha(self):
        return(self.__fechaInscripcion)
    def getPago(self):
        return(self.__pago)
