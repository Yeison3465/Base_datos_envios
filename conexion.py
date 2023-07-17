import mysql.connector

def añadir_columna():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        print("Conexion establecida")
        
    except mysql.connector.Error as error:
        print(f"Error al añadir columna: {error}")
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

