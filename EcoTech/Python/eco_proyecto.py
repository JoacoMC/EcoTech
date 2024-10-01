import mysql.connector

class eco_proyecto:
    
    def conectar():
        cnx = mysql.connector.connect(username='root', password='',database='EcoTech')
        return cnx
    
    def insertar(nombre:str, descripcion:str, fecha:str):
        cnx = eco_proyecto.conectar()
        cursor=cnx.cursor()
        sql = 'insert into departamento(nombre, descripcion, fecha) values (%s, %s);'
        values = [nombre, descripcion, fecha]
        cursor.execute(sql,values)
        cnx.commit()
        cursor.close()
        cnx.close()
        return 