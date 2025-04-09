class Ecommerce:
    def __init__(self,  documento, nombres, apellidos, correo, metodo_de_pago, fecha_nacimiento, direccion, celular, id_persona):
        
        self.documento = documento
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.metodo_de_pago = metodo_de_pago
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.celular = celular
        self.id_persona = id_persona
        
    def to_JSON(self):
        return {
            
                'documento': self.documento,
                'nombres': self.nombres,
                'apellidos': self.apellidos,
                'correo': self.correo,
                'metodo_de_pago': self.metodo_de_pago,
                'fecha_nacimiento': self.fecha_nacimiento,
                'direccion': self.direccion,
                'celular': self.celular,
                'id_persona': self.id_persona
        }    

#def __repr__(self):
    #return f"<Ecommerce {self.nombres} {self.apellidos}>"
    
    
