from database.db import get_connection
from .entities.Ecommerce import Ecommerce

class Ecommerce_Model():
    
    @classmethod
    def get_ecommerce(self):
        try:
            connection=get_connection()
            personas=[]
            
            with connection.cursor() as cursor:
                
                cursor.execute("SELECT  documento, nombres, apellidos, correo, metodo_de_pago, fecha_nacimiento, direccion, celular, id_persona FROM id_personas ORDER BY documento ASC")
                resulset=cursor.fetchall()
                
                for row in resulset:
                    ecommerce = Ecommerce(
                        documento=row[0],
                        nombres=row[1],
                        apellidos=row[2],
                        correo=row[3],
                        metodo_de_pago=row[4],
                        fecha_nacimiento=row[5],
                        direccion=row[6],
                        celular=row[7],
                        id_persona=row[8]
                    )
                    personas.append(ecommerce.to_JSON()) 
                    
            connection.close()
            return personas        
                    
        except Exception as ex:
            raise Exception(ex)
                
