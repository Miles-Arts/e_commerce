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
sql='UPDATE cliente_comprador SET id_compra=%s,id_comprador=%s WHERE id_compra=%s'

#consulta de datos usuario
id_compra=input("Ingrese ID del producto a editar: ").strip()


#recoleccion de datos
datos=(id_compra)

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





