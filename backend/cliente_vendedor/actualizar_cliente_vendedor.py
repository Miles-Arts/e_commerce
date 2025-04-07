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
sql='UPDATE productos SET nombre_producto=%s,categoria_producto=%s,caracteristicas_producto=%s,tipo_producto=%s,tamano_producto=%s,precio_producto=%s,mes_del_producto=%s WHERE id_producto=%s'

#consulta de datos usuario
id_producto=input("Ingrese ID del producto a editar: ").strip()
nombre_producto=input("Ingrese nombre producto: ").title()
categoria_producto=input("Ingrese categoría producto: ").title()
caracteristicas_producto=input("Ingrese caracterisrticas producto: ")
tipo_producto=input("Ingrese tipo producto (seco - liquido - granos): ")
tamano_producto=input("Ingrese tamaño en número- dimensiones - peso - litros : ")
precio_producto=input("Ingrese precio del producto: ")
mes_del_producto=input("Ingrese mes de la cosecha: ").title()

#recoleccion de datos
datos=(nombre_producto,categoria_producto,caracteristicas_producto,tipo_producto,tamano_producto,precio_producto,mes_del_producto,id_producto)

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





