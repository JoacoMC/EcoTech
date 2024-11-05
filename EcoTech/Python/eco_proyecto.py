from mysql.connector import MySQLConnection, connect
from datetime import date

class Proyecto:
    def __init__(self,nombre: str, descripcion: str, fecha_inicio: date) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio

    #def agregar_proyecto(self, proyecto: Proyecto):
     #   self.lista_proyectos.append(proyecto)

class CrudProyecto:
    def __init__(self) -> None:
        self.username = 'root'
        self.password = ''
        self.database = 'EcoTech'
    
    def conectar(self) -> MySQLConnection:
        cnx = connect(user=self.username, password=self.password, database=self.database)
        return cnx
    def insertar(self, proyecto : Proyecto) -> bool:
        # Obtener una conexion
        cnx = self.conectar()
        # Crear un cursor
        cursor = cnx.cursor()
        # Configurar la consulta con parametros
        sql = 'insert into proyecto(nombre, descripcion, fecha_inicio) values (%s, %s, %s)'
        # Tupla con parametros
        values = (proyecto.nombre, proyecto.descripcion,proyecto.fecha_inicio)
        # Ejecutar la consulta + los parametros
        cursor.execute(sql, values)
        # Obtener el id insertado en la tabla persona
        id_proyecto = cursor.lastrowid
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    
    def obtener(self) -> list[Proyecto]|None:
        cnx = self.conectar()
        cursor = cnx.cursor()
        query = "select nombre,descripcion,fecha_inicio from proyecto"
        cursor.execute(query)
        result = cursor.fetchall()
        proyectos = []
        for row in result:
            proy = Proyecto(nombre=row[0], descripcion=row[1], fecha_inicio=row[2])
            proyectos.append(proy)
        cursor.close()
        cnx.close()
        return proyectos
    
    def modificar(self, proyecto:Proyecto, nueva_desc : str) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'select id_proyecto from proyecto where nombre=%s'
        values = (proyecto.nombre)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if result is not None:
            id_proyecto = result[0]
            sql2 = 'update proyecto set descripcion=%s where id_proyecto=%s'
            values2 = (nueva_desc,id_proyecto)
            cursor.execute(sql2, values2)
            cnx.commit()
        cursor.close()
        cnx.close()
        return True
    def eliminar(self, proyecto:Proyecto) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'select id_proyecto from proyecto where nombre=%s'
        values = (proyecto.nombre)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if result is not None:
            id_proyecto = result[0]
            sql2 = 'delete from proyecto where id_proyecto=%s;'
            values2 = (id_proyecto)
            cursor.execute(sql2, values2)
            cnx.commit()
        cursor.close()
        cnx.close()
        return True
