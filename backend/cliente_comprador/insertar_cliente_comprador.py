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
sql='INSERT INTO cliente_comprador(id_compra,id_comprador) VALUES(%s,%s)'

#Solicitud de datos al usuario
id_compra=input("Ingrese ID compra: ").title()
Id_comprador=input("Ingrese ID comprador: ").title()

#recolección de datos
datos=(id_compra,Id_comprador)

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
