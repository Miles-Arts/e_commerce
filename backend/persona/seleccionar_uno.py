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

# Consulta SQL
sql = 'SELECT * FROM id_personas'

#Buscar por ID
id_persona=input("Ingrese ID persona: ").strip()

#Método execute
cursor.execute(sql, id_persona)

#mostrar resultados
registros=cursor.fetchone()

# Obtener nombres de columnas desde el cursor
#columnas = [desc[0] for desc in cursor.description]

# Crear DataFrame con pandas
#df = pd.DataFrame(registros, columns=columnas)

#Organiozar tablas
# Configura el formato de salida
#pd.set_option("display.max_columns", None)
#pd.set_option("display.width", 1000)
#pd.set_option("display.colheader_justify", "center")
#pd.set_option("display.max_colwidth", None)
#df.sort_values(by='documento', inplace=True)

# Mostrar DataFrame
#print(df)

#mostrar en terminal
print(registros)



# Cerrar cursor y conexión
cursor.close()
conexion.close()












