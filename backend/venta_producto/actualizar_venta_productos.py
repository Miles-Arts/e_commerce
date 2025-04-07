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
sql='UPDATE venta_producto SET id_vendedor=%s,id_venta=%s,id_compra=%s,precio_producto=%s WHERE id_venta=%s'

#consulta de datos usuario
id_vendedor=input("Ingrese ID vendedor: ").strip()
id_venta=input("Ingrese ID venta: ").strip()
id_compra=input("Ingrese ID compra: ").strip()
precio_producto=input("Ingrese precio producto: ").strip()

#recoleccion de datos
datos=(id_vendedor,id_venta,id_compra,precio_producto)

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





