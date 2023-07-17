import mysql.connector

def Crear_tabla_PD():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = ("""
            Create table Pedido_producto(
                id_Pedido_PD BIGINT NOT NULL ,
                id_Producto_PD BIGINT NOT NULL,
                CONSTRAINT fk_Pedido_PD FOREIGN KEY (id_Pedido_PD) REFERENCES Pedido (id_Pedidos),
                CONSTRAINT fk_Producto_PD FOREIGN KEY (id_Producto_PD) REFERENCES Producto (id_Producto)
                )
        """)
        
        cursor.execute(query)
        conn.commit()
        print("pd")
        
    except mysql.connector.Error as error:
        print(error)

def InsertPD(pedido,producto):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""INSERT INTO  Pedido_producto (id_Pedido_PD,id_Producto_PD) VALUES ({pedido},{producto})""")
        
        cursor.execute(query)
        conn.commit()
        print("Pedido añadido")
        
    except mysql.connector.Error as error:
        print(error)

def SeleccionarPD():
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""SELECT * FROM Pedido_producto""")
        
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        print(datos)
    except mysql.connector.Error as error:
        print(error)

def ActualizarDatosPD(id,pedido,producto):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""UPDATE Pedido_producto SET  id_Pedido_PD = {pedido},  id_Producto_PD = {producto} WHERE id_Pedido_PD  = {id}""")
        
        cursor.execute(query)
        conn.commit()
        print("Actualizacion completada")
    except mysql.connector.Error as error:
        print(error)


def eliminarDatosPedido(pedido):
    try:
        conn = mysql.connector.connect(user='root', password='tommy', host='localhost', port='3306', database='envios')
        cursor = conn.cursor()
        
        query = (f"""DELETE FROM Pedido_producto WHERE id_Pedido_PD = {pedido}""")
        
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        print("pedido eliminado")
    except mysql.connector.Error as error:
        print(error)

#Crear_tabla_envio()
#InsertPedido(1,1)
#SeleccionarPD()
#ActualizarDatosPD()
#eliminarDatosPedido()



