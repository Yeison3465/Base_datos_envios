import mysql.connector
def Crear_tabla_vehiculo():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = ("""
            Create table Vehiculo(
            id_Vehiculo BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            Capacidad  INT NOT NULL,
            Tipo_Vehiculo VARCHAR(255) NOT NULL,
            Disponible BOOLEAN NOT NULL)
        """)
        
        cursor.execute(query)
        conn.commit()
        print("Cliente")

        
    except mysql.connector.Error as error:
        print(error)



def insertar_Vehiculo(capacidad,Tipvehi, disponible):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = f"INSERT INTO Vehiculo (Capacidad,Tipo_Vehiculo,Disponible) VALUES ({capacidad}, '{Tipvehi}',{disponible})"
        
        cursor.execute(query)
        conn.commit()
        
        print("Registro insertado exitosamente.")
        
        cursor.close()
        conn.close()
        
    except mysql.connector.Error as error:
        print(f"ERROR al conectar a la base de datos: {error}")

def SeleccionarVehiculo():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""SELECT * FROM Vehiculo""")
        
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        print(datos)
    except mysql.connector.Error as error:
        print(error)


def ActualizarDatosCliente(id,capacidad,tipovehi,disponible):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""UPDATE Vehiculo SET Capacidad = {capacidad}, Tipo_Vehiculo = '{tipovehi}' , Disponible = {disponible} WHERE id_Vehiculo = {id}""")
        
        cursor.execute(query)
        conn.commit()
        print("Actualizacion completada")
    except mysql.connector.Error as error:
        print(error)

def eliminarVehiculo(id):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""DELETE FROM Vehiculo  WHERE id_Vehiculo = {id}""")

        
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        print("Vehiculo eliminado")
    except mysql.connector.Error as error:
        print(error)
#Crear_tabla_vehiculo()
#insertar_Vehiculo(500,"Camion",False)
#SeleccionarVehiculo()
#ActualizarDatosCliente(1,1000,"Caminada",False)
#eliminarVehiculo(2)


