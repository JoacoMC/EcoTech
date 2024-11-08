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
    
    def buscar(self, buscar : int):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql1 = 'select nombre, descripcion, fecha_inicio from proyecto where id_proyecto=%s'
        values1 = (buscar,)
        cursor.execute(sql1,values1)
        result = cursor.fetchone()
        return result
    
    def modificar(self, nombre : str, nueva_desc : str, fecha_inicio : date,  id_proyecto:int) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'update proyecto set nombre= %s, descripcion= %s, fecha_inicio = %s where id_proyecto = %s'
        values = (nombre, nueva_desc ,fecha_inicio, id_proyecto)
        try:
            cursor.execute(sql, values)
            cnx.commit()
            filas_afectadas = cursor.rowcount
            if filas_afectadas > 0:
                return True, "Modificación exitosa."
            else:
                return False, "No se encontró el proyecto o no hubo cambios."
        except Exception as e:
            return False, f"Error en la modificación: {str(e)}"
        finally:
            cursor.close()
            cnx.close()

    def eliminar(self, id_proyecto : int) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'delete from proyecto where id_proyecto = %s'
        values = (id_proyecto,)
        cursor.execute(sql, values)
        cnx.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        cnx.close()
        return filas_afectadas > 0
