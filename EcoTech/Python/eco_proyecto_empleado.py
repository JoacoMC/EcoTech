import mysql.connector

class eco_proyecto_empleado:
    
    def conectar():
        cnx = mysql.connector.connect(username='root', password='',database='EcoTech')
        return cnx
    
    def insertar(id_proyecto:int, id_empleado: int):
        cnx = eco_proyecto_empleado.conectar()
        cursor=cnx.cursor()
        sql = 'insert into departamento(id_proyecto, id_empleado) values (%s, %s);'
        values = (id_proyecto, id_empleado)
        cursor.execute(sql,values)
        cnx.commit()
        cursor.close()
        cnx.close()
        return 