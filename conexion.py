import psycopg2

'''
En este archivo esta destinado unicamente a realizar la conexion a la base de datos 
Se puede importar a otros archivos donde sea necesaria la conexion

'''

def conectar():
    try:
        conexion = psycopg2.connect(
            user = 'postgres',
            password = 'admin',
            host='127.0.0.1',
            port='5432',
            database = "servicio_bd"
        )
        return conexion
    
    except Exception as e:
        print(f'Ocurrio un error de tipo: {e}')
        return None
    