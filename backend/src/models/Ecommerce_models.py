from database.db import get_connection
from .entities.Ecommerce import Ecommerce

class Ecommerce_Model():
        
    @classmethod
    def get_ecommerce(self):
        try:
            connection = get_connection()
            personas = []

            with connection.cursor() as cursor:
                # Asegúrate de que el orden de las columnas coincida con el constructor de Ecommerce
                cursor.execute("""
                    SELECT id_persona, documento, nombres, apellidos, correo, metodo_de_pago, fecha_nacimiento, direccion, celular
                    FROM id_personas
                    ORDER BY documento ASC
                """)
                resulset = cursor.fetchall()

                for row in resulset:
                    ecommerce = Ecommerce(
                        id_persona=row[0],         # id_persona
                        documento=row[1],          # documento
                        nombres=row[2],            # nombres
                        apellidos=row[3],          # apellidos
                        correo=row[4],             # correo
                        metodo_de_pago=row[5],     # metodo_de_pago
                        fecha_nacimiento=row[6],   # fecha_nacimiento
                        direccion=row[7],          # direccion
                        celular=row[8]             # celular
                    )
                    personas.append(ecommerce.to_JSON())

            connection.close()
            return personas

        except Exception as ex:
            raise Exception(ex)
                
    @classmethod
    def get_ecommerce_by_id(self, id_persona):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                # Asegúrate de que el orden de las columnas coincida con el constructor de Ecommerce
                cursor.execute("""
                    SELECT id_persona, documento, nombres, apellidos, correo, metodo_de_pago, fecha_nacimiento, direccion, celular
                    FROM id_personas
                    WHERE id_persona = %s
                """, (id_persona,))
                row = cursor.fetchone()

                ecommerce = None

                if row is not None:
                    ecommerce = Ecommerce(
                        id_persona=row[0],         # id_persona
                        documento=row[1],          # documento
                        nombres=row[2],            # nombres
                        apellidos=row[3],          # apellidos
                        correo=row[4],             # correo
                        metodo_de_pago=row[5],     # metodo_de_pago
                        fecha_nacimiento=row[6],   # fecha_nacimiento
                        direccion=row[7],          # direccion
                        celular=row[8]             # celular
                    )
                    ecommerce = ecommerce.to_JSON()

            connection.close()
            return ecommerce

        except Exception as ex:
            raise Exception(ex)
        
@classmethod
def add_ecommerce(self, id_personas):
    try:
        connection = get_connection()

        with connection.cursor() as cursor:
            # Inserta los datos en la base de datos
            cursor.execute("""
                INSERT INTO id_personas (documento, nombres, apellidos, correo, metodo_de_pago, fecha_nacimiento, direccion, celular, id_persona)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                id_personas.documento,
                id_personas.nombres,
                id_personas.apellidos,
                id_personas.correo,
                id_personas.metodo_de_pago,  # Booleano
                id_personas.fecha_nacimiento,  # Fecha
                id_personas.direccion,
                id_personas.celular,
                id_personas.id_persona
            ))

            affected_rows = cursor.rowcount
            connection.commit()

        connection.close()
        return affected_rows

    except Exception as ex:
        raise Exception(ex)