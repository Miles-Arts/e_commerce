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
sql='INSERT INTO venta_producto(id_vendedor,id_venta_,id_compra,precio_producto) VALUES(%s,%s,%s,%s)'

#Solicitud de datos al usuario

nombre_producto=input("Ingrese nombre producto: ").title()
categoria_producto=input("Ingrese categoría producto: ").title()
caracteristicas_producto=input("Ingrese caracterisrticas producto: ")
tipo_producto=input("Ingrese tipo producto (seco - liquido - granos): ")


#recolección de datos
datos=()

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
