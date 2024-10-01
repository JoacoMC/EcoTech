import mysql.connector

class eco_empleado:
    
    def conectar():
        cnx = mysql.connector.connect(username='root', password='',database='EcoTech')
        return cnx
    
    def insertar(nombre:str, direccion:str, telefono:str, correo:str, inicio_contrato:str, salario:int):
        cnx = eco_empleado.conectar()
        cursor=cnx.cursor()
        sql = 'insert into empleado(nombre, direccion, telefono, correo, inicio_contrato, salario) values (%s, %s, %s, %s, %s, %s);'
        values = [nombre, direccion, telefono, correo, inicio_contrato, salario]
        cursor.execute(sql,values)
        cnx.commit()
        cursor.close()
        cnx.close()
        return 
    

eco_empleado.insertar('joaquin', 'rengo', '999999', 'hola@gmail.com', '01/03/2024', 50000)
print("hola mundo")
print("Chao")