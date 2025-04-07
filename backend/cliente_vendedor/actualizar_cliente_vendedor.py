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

#crear sentencia sql
sql='UPDATE cliente_vendedor SET id_venta=%s,id_vendedor=%%s WHERE id_venta=%s'

#consulta de datos usuario
id_venta=input("Ingrese ID de la venta a editar: ").strip()


#recoleccion de datos
datos=()

#utilizar execute
cursor.execute(sql,datos)

#guardar actualizacion - nueva informaicon
conexion.commit()

#contar numero actualzacione
actualizacion=cursor.rowcount

#monstar mensaj al usuario
print(f"Registro actualzado: {actualizacion}")

#cerrar conexion
cursor.close()
conexion.close()





