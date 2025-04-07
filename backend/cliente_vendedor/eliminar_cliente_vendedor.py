# Importar módulo
import pandas as pd
import psycopg2 
from psycopg2 import sql, errors

# Conexión a la base de datos
conexion = psycopg2.connect(
    user='postgres',
    password='1234',
    host='127.0.0.1',
    port='5432',
    database='ecommerce'
)

# Crear cursor
cursor = conexion.cursor()

#sentencia SQL
sql='DELETE FROM cliente_vendedor WHERE id_venta=%s'

#solicitar dato al user
id_poducto=input("Ingrese ID de la venta a eliminar: ").strip()

#metodo execute
cursor.execute(sql,id_poducto)

#guardar cambios
conexion.commit()

#conteo registro  eliminado
registro_eliminado=cursor.rowcount

#mensaje a usuario
print(f"Registros eliminado {registro_eliminado}")

#cerra conexion
cursor.close()
conexion.close()



