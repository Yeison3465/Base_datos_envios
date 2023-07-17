import mysql.connector

def Crear_tabla_cliente():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = ("""
            Create table Cliente(
            id_Cliente BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            Nombre VARCHAR(255) NOT NULL,
            Apellidos VARCHAR(255) NOT NULL,
            Telefono VARCHAR(255) NOT NULL)
        """)
        
        cursor.execute(query)
        conn.commit()
        print("Cliente")
        
    except mysql.connector.Error as error:
        print(error)

def InsertCliente(nombre,apellidos,telefono):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""INSERT INTO Cliente (Nombre,Apellidos,Telefono) VALUES ('{nombre}','{apellidos}','{telefono}')""")
        
        cursor.execute(query)
        conn.commit()
        print("Cliente añadido")
        
    except mysql.connector.Error as error:
        print(error)

def SeleccionarClientes():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""SELECT * FROM Cliente""")
        
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        print(datos)
    except mysql.connector.Error as error:
        print(error)

def ActualizarDatosCliente(id,nombre,apellido,telefono):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""UPDATE Cliente SET Nombre = '{nombre}', Apellidos = '{apellido}' , Telefono = '{telefono}' WHERE id_Cliente = {id}""")
        
        cursor.execute(query)
        conn.commit()
        print("Actualizacion completada")
    except mysql.connector.Error as error:
        print(error)

def eliminarDatosCliente(id):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""DELETE FROM cliente WHERE id_Cliente = {id}""")
        
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        print("cliente eliminado")
    except mysql.connector.Error as error:
        print(error)


#InsertCliente("mafe","solar","33135331")
#Crear_tabla_cliente()
#SeleccionarClientes()
#ActualizarDatosCliente(2,"Carlos","Mendoza","343434343")
#eliminarDatosCliente(6)