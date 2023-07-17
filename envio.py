import mysql.connector

def Crear_tabla_envio():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        
        query = ("""
            Create table Envio(
                id_Envios BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                id_Cliente_Envio BIGINT NOT NULL,
                id_Empleado_Envio BIGINT NOT NULL,
                id_Vehiculo_Envio BIGINT NOT NULL,
                id_Producto_Envio BIGINT NOT NULL,
                CONSTRAINT fk_Envios_Cliente FOREIGN KEY (id_Cliente_Envio) REFERENCES Cliente (id_Cliente),
                CONSTRAINT fk_Envios_Empleado FOREIGN KEY (id_Empleado_Envio) REFERENCES Empleado (id_Empleado),
                CONSTRAINT fk_Envios_Vehiculo FOREIGN KEY (id_Vehiculo_Envio) REFERENCES Vehiculo (id_Vehiculo),
                CONSTRAINT fk_Envios_Producto FOREIGN KEY (id_Producto_Envio) REFERENCES Producto (id_Producto))
        """)
        
        cursor.execute(query)
        conn.commit()
        print("Envios")
        
    except mysql.connector.Error as error:
        print(error)
    
def InsertarEnvio(cliente,empleado,vehiculo,producto):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""INSERT INTO Envio (id_Cliente_Envio,id_Empleado_Envio,id_Vehiculo_Envio,id_Producto_Envio) VALUES ({cliente},{empleado},{vehiculo},{producto})""")
        
        cursor.execute(query)
        conn.commit()
        print("Producto añadido")
        
    except mysql.connector.Error as error:
        print(error)

def SeleccionarEnvio():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""SELECT * FROM Envio""")
        
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        print(datos)
    except mysql.connector.Error as error:
        print(error)

def ActualizarDatosEnvio(id,cliente,empleado,vehiculo,producto):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""UPDATE Envio SET id_Cliente_Envios = {cliente}, id_Empleado_Envio = {empleado} , id_Vehiculo_Envio = {vehiculo},id_Producto_Envio = {producto} WHERE id_Envios = {id}""")
        
        cursor.execute(query)
        conn.commit()
        print("Actualizacion completada")
    except mysql.connector.Error as error:
        print(error)

def eliminarDatosEnvio(id):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""DELETE FROM Envio WHERE id_Envios = {id}""")
        
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        print("Envio eliminado")
    except mysql.connector.Error as error:
        print(error)



#Crear_tabla_envio()
#InsertarEnvio(1,1,1,1)
#SeleccionarEnvio()
#ActualizarDatosEnvio()
#eliminarDatosEnvio()



