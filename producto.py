import mysql.connector

def Crear_tabla_producto():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = ("""
            Create table Producto(
            id_Producto BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            Nombre_Producto VARCHAR(255) NOT NULL,
            Descripcion VARCHAR(255) NOT NULL,
            Precio REAL NOT NULL,
            Cantidad INT NOT NULL)
        """)
        
        cursor.execute(query)
        conn.commit()
        print("Producto")
    except mysql.connector.Error as error:
        print(error)


def InsertProducto(nombreproducto,descrip,precio,cantidad):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""INSERT INTO Producto (Nombre_Producto,Descripcion,Precio,Cantidad) VALUES ('{nombreproducto}','{descrip}',{precio},{cantidad})""")
        
        cursor.execute(query)
        conn.commit()
        print("Producto añadido")
    except mysql.connector.Error as error:
        print(error)

def SeleccionarProducto():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""SELECT * FROM Producto""")
        
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        print(datos)
    except mysql.connector.Error as error:
        print(error)

def ActualizarProducto(id,nombreproducto,descrip,precio,cantidad):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""UPDATE Producto SET Nombre_Producto = '{nombreproducto}', Descripcion = '{descrip}' , Precio = {precio} , Cantidad = {cantidad} WHERE id_Producto = {id}""")
        
        cursor.execute(query)
        conn.commit()
        print("Actualizacion completada")
    except mysql.connector.Error as error:
        print(error)

def eliminarProducto(id):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        query = (f"""DELETE FROM Producto   WHERE id_Producto = {id}""")
        
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        print("Producto eliminado")
    except mysql.connector.Error as error:
        print(error)

#Crear_tabla_producto()
#InsertProducto("camisa", "color rojo",12000,60000)
#SeleccionarProducto()
#ActualizarDatosCliente(1,"Medias","Color verde",12000,6000)
#eliminarProducto(2)
