import mysql.connector

def Crear_tabla_envio():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = ("""
            Create table Pedido(
                id_Pedidos BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                id_Cliente_Pedido BIGINT NOT NULL,
                id_Envio_Pedido BIGINT NOT NULL,
                id_Producto_Pedido BIGINT NOT NULL,
                CONSTRAINT fk_Pedido_Cliente FOREIGN KEY (id_Cliente_Pedido) REFERENCES Cliente (id_Cliente),
                CONSTRAINT fk_Pedido_Envio_ FOREIGN KEY (id_Envio_Pedido) REFERENCES Envio (id_Envios),
                CONSTRAINT fk_Pedido_Producto FOREIGN KEY (id_Producto_Pedido) REFERENCES Producto (id_Producto))
        """)
        
        cursor.execute(query)
        conn.commit()
        print("Pedido")
        
    except mysql.connector.Error as error:
        print(error)

def InsertPedido(cliente,envio,producto):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        query = (f"""INSERT INTO Pedido (id_Cliente_Pedido,id_Envio_Pedido,id_Producto_Pedido) VALUES ({cliente},{envio},{producto})""")
        
        cursor.execute(query)
        conn.commit()
        print("Pedido añadido")
        
    except mysql.connector.Error as error:
        print(error)

def SeleccionarPedido():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""SELECT * FROM Pedido""")
        
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        print(datos)
    except mysql.connector.Error as error:
        print(error)

def ActualizarDatosCliente(id,cliente,envio,producto):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""UPDATE Pedido SET  id_Cliente_Pedido = {cliente}, id_Envio_Pedido = {envio} ,  id_Producto_Pedido = {producto} WHERE id_Pedidos = {id}""")
        
        cursor.execute(query)
        conn.commit()
        print("Actualizacion completada")
    except mysql.connector.Error as error:
        print(error)

def eliminarDatosPedido(id):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""DELETE FROM Pedido WHERE id_Pedidos = {id}""")
        
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        print("pedido eliminado")
    except mysql.connector.Error as error:
        print(error)

#Crear_tabla_envio()
#InsertPedido(1,1,1)
#SeleccionarPedido()
#ActualizarDatosCliente()
#eliminarDatosPedido()



