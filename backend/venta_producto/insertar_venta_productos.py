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
sql='INSERT INTO venta_producto(id_vendedor,id_venta,id_compra,precio_producto) VALUES(%s,%s,%s,%s)'

#Solicitud de datos al usuario

id_vendedor=input("Ingrese ID vendedor: ").strip()
id_venta=input("Ingrese ID venta: ").strip()
id_compra=input("Ingrese ID compra: ").strip()
precio_producto=input("Ingrese precio producto: ").strip()


#recolección de datos
datos=(id_vendedor,id_venta,id_compra,precio_producto)

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
