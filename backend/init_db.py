import os
import glob
import psycopg2

def execute_sql_script(cursor, sql_file_path):
    """
    Lee y ejecuta el contenido de un archivo SQL.
    """
    print(f"Ejecutando script: {sql_file_path}")
    with open(sql_file_path, 'r', encoding='utf-8') as file:
        sql_script = file.read()
    # Ejecuta el script SQL; si el script contiene múltiples sentencias,
    # podrías necesitar usar cursor.execute() varias veces o cursor.executemany()
    cursor.execute(sql_script)

def main():
    # Define el directorio base donde se encuentran los archivos SQL.
    # Suponiendo que este script se encuentra en la carpeta 'backend'.
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Buscar recursivamente archivos .sql en el directorio base y sus subcarpetas.
    sql_files = glob.glob(os.path.join(base_dir, '**', '*.sql'), recursive=True)
    
    # Ordenar los archivos SQL (por ejemplo alfabéticamente) para asegurar un orden de ejecución.
    sql_files.sort()
    
    print("Scripts SQL a ejecutar:")
    for f in sql_files:
        print(f"  - {f}")
    
    # Configuración de la conexión a tu base de datos
    try:
        conn = psycopg2.connect(
            user='postgres',
            password='1234',
            host='127.0.0.1',
            port='5432',
            database='ecommerce'
        )
        cursor = conn.cursor()
        print("Conexión a la base de datos establecida.")

        # Iterar sobre cada archivo SQL y ejecutarlo
        for sql_file in sql_files:
            try:
                execute_sql_script(cursor, sql_file)
                conn.commit()  # Confirma cada script; si prefieres, puedes hacer commit al finalizar todos.
            except Exception as e:
                print(f"Error al ejecutar {sql_file}: {e}")
                conn.rollback()
                # Dependiendo de tus necesidades, puedes optar por detener la ejecución en caso de error o continuar
                # Para detener: raise e

        print("Todos los scripts ejecutados correctamente.")

    except Exception as ex:
        print("Error estableciendo la conexión a la base de datos:", ex)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print("Conexión cerrada.")

if __name__ == '__main__':
    main()
