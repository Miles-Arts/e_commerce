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
sql='UPDATE id_personas SET documento=%s,nombres=%s,apellidos=%s,correo=%s,metodo_de_pago=%s,fecha_nacimiento=%s,direccion=%s,celular=%s WHERE id_persona=%s'

#consulta de datos usuario
id_persona=input("Ingrese ID de la persona a Editar: ").strip()
documento=input("Ingrese número de documento: ")
nombres=input("Ingrese su nombre: ").title()
apellidos=input("Ingrese apellidos: ").title()
correo=input("Ingrese el correo: ")
print("Ingrese 1 o 0")
metodo_pago=input("Ingrese el método de pago: ")
fecha_nacimiento=input("Ingrese su fecha de nacimiento: ")
direccion=input("Ingrese su dirección: ")
celular=input("Ingrese su número de celular: ")

#recoleccion de datos
datos=(documento,nombres,apellidos,correo,metodo_pago,fecha_nacimiento,direccion,celular,id_persona)

#utilizar execute
cursor.execute(sql,datos)

#guardar actualizacion - nueva informaicon
conexion.commit()

#contar numero actualzacione
actualizacion=cursor.rowcount

#monstar mensaj al usuraio
print(f"Registro actualzado: {actualizacion}")

#cerra conexion
cursor.close()
conexion.close()





