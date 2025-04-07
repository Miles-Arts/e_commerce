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
sql='INSERT INTO id_personas(documento,nombres,apellidos,correo,metodo_de_pago,fecha_nacimiento,direccion,celular) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'

#Solicitud de datos al usuario
documento=input("Ingrese número de documento: ")
nombres=input("Ingrese su nombre: ").title()
apellidos=input("Ingrese apellidos: ").title()
correo=input("Ingrese el correo: ")
print("Ingrese 1 o 0")
metodo_pago=input("Ingrese el método de pago: ")
fecha_nacimiento=input("Ingrese su fecha de nacimiento: ")
direccion=input("Ingrese su dirección: ")
celular=input("Ingrese su número de celular: ")

#recolección de datos
datos=(documento,nombres,apellidos,correo,metodo_pago,fecha_nacimiento,direccion,celular)

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
