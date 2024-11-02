import mysql.connector

class eco_usuario:
    
    def conectar():
        cnx = mysql.connector.connect(username='root', password='',database='EcoTech')
        return cnx
    
    def insertar(nombre:str,contraseña:str,permiso:str) -> bool:
        cnx = eco_usuario.conectar()
        cursor=cnx.cursor()
        sql = 'insert into usuario(nombre, contraseña, permiso) values(%s,%s, %s);'
        values = [nombre, contraseña, permiso]
        cursor.execute(sql,values)
        cnx.commit()
        cursor.close()
        cnx.close()
        return 
