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

#Crear sentencia SQL
sql='INSERT INTO cliente_vendedor(id_vendedor,id_venta) VALUES(%s,%s)'

#Solicitud de datos al usuario
id_venta=input("Ingrese ID venta: ").strip()
#id_vendedor=input("Ingrese Id vendedor: ").strip()


#recolección de datos
datos=(id_venta)

#utilizar execute
cursor.execute(sql,datos)

#guardar registro- datos
conexion.commit()

#mensaje insert datos
#registros insertados
registros=cursor.rowcount

#mostra mensaje
print(f"registro insertado: {registros}")

#cerra conexion
cursor.close()
conexion.close()
