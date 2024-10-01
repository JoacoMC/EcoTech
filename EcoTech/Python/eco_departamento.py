import mysql.connector

class eco_departamento:
    
    def conectar():
        cnx = mysql.connector.connect(username='root', password='',database='EcoTech')
        return cnx
    
    def insertar(nombre:str, gerente: int):
        cnx = eco_departamento.conectar()
        cursor=cnx.cursor()
        sql = 'insert into departamento(nombre, gerente) values (%s, %s);'
        values = (nombre, gerente)
        cursor.execute(sql,values)
        cnx.commit()
        cursor.close()
        cnx.close()
        return 