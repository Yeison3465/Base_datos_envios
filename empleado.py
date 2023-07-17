import mysql.connector
def Crear_tabla_empleado():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = ("""
            Create table Empleado(
            id_Empleado BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            Nombre_Empleado VARCHAR(255) NOT NULL,
            Apellidos_Empleado VARCHAR(255) NOT NULL,
            Telefono VARCHAR(255) NOT NULL,
            Correo_Empleado VARCHAR(255) NOT NULL)
        """)
        
        cursor.execute(query)
        conn.commit()
        print("Empleado")
    except mysql.connector.Error as error:
        print(error)

def InsertEmpleado(nombre,apellidos,telefono,correo_empleado):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""INSERT INTO Empleado (Nombre_Empleado,Apellidos_Empleado,Telefono_Empleado,Correo_Empleado) VALUES ('{nombre}','{apellidos}','{telefono}','{correo_empleado}')""")
        
        cursor.execute(query)
        conn.commit()
        print("Empleado añadido")
        
    except mysql.connector.Error as error:
        print(error)

def SeleccionarEmpleado():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""SELECT * FROM Empleado""")
        
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        print(datos)
    except mysql.connector.Error as error:
        print(error)

def ActualizarDatosCliente(id,nombre,apellido,telefono,correo):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""UPDATE Empleado SET Nombre_Empleado = '{nombre}', Apellidos_Empleado = '{apellido}' , Telefono_Empleado = '{telefono}' , Correo_Empleado = '{correo}'WHERE id_Empleado = {id}""")
        
        cursor.execute(query)
        conn.commit()
        print("Actualizacion completada")
    except mysql.connector.Error as error:
        print(error)

def eliminarDatosCliente(id):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        query = (f"""DELETE FROM Empleado  WHERE id_Empleado = {id}""")
        
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        print("Empleado eliminado")
    except mysql.connector.Error as error:
        print(error)



#Crear_tabla_empleado()
#InsertEmpleado("Arturo","Mendoza","300211133","Arturo@gmail.com")
#SeleccionarEmpleado()
#ActualizarDatosCliente(1,"Jorge","Mendoza","30001111","Jose@gmail.com")
#eliminarDatosCliente(2)