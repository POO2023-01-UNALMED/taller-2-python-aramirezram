class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self,color):
        if color in ["rojo","verde","amarillo","negro","blanco"]:
            self.color=color
            
class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
    def cantidadAsientos(self):
        x=0
        for i in self.asientos:
            if type(i)==type(Asiento):
                x=x+1
        return x
    def verificarIntegridad(self):
        legit=True
        for i in self.asientos:
            try:
                if i.registro!=self.registro!=self.motor.registro:
                    legit=False
                    return "Las piezas no son originales"
                    break    
            except:
                continue
        if legit==True:
            return "Auto original"
        
class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    def cambiarRegistro(self,registro):
        self.registro=registro
    def asignarTipo(self,tipo):
        if tipo in ["electrico","gasolina"]:
            self.tipo=tipo
 
        
            
    
