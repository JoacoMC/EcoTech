import mysql.connector

class eco_registro_tiempo:
    
    def conectar():
        cnx = mysql.connector.connect(username='root', password='',database='EcoTech')
        return cnx
    
    def insertar(fecha:str, cantidad_horas:int, descripcion:str, empleado_id_empleado:int, proyecto_id_proyecto:int):
        cnx = eco_registro_tiempo.conectar()
        cursor=cnx.cursor()
        sql = 'insert into departamento(fecha, cantidad_horas, descripcion, empleado_id_empleado, proyecto_id_proyecto) values (%s, %s, %s, %s, %s);'
        values = [fecha, cantidad_horas, descripcion, empleado_id_empleado, proyecto_id_proyecto]
        cursor.execute(sql,values)
        cnx.commit()
        cursor.close()
        cnx.close()
        return 