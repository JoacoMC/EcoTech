from mysql.connector import MySQLConnection, connect
from modelo import Proyecto_empleado


class CrudProyectoEmpleado:
    def __init__(self) -> None:
        self.username = 'root'
        self.password = ''
        self.database = 'EcoTech'
    def conectar(self) -> MySQLConnection:
        cnx = connect(user=self.username, password=self.password, database=self.database)
        return cnx 
    
    def insertar(self, proyecto_empleado:Proyecto_empleado) -> bool:
        # Obtener una conexion
        cnx = self.conectar()
        # Crear un cursor
        cursor = cnx.cursor()
        # Configurar la consulta con parametros
        sql = 'insert into proyecto_empleado(id_proyecto,id_empleado) values (%s, %s)'
        # Tupla con parametros
        values = (proyecto_empleado.id_proyecto,proyecto_empleado.id_empleado)
        # Ejecutar la consulta + los parametros
        cursor.execute(sql, values)
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    
    def obtener(self) -> list[Proyecto_empleado]:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'select id_proyecto,id_empleado from proyecto_empleado '
        cursor.execute(sql)
        # resultset es una lista de tuplas, cada item de la tupla representa un valor de columna
        resultset = cursor.fetchall()
        Proyecto_Empleados = []
        for row in resultset:
            proyem = Proyecto_empleado(id_proyecto=row[0], id_empleado=row[1])
            Proyecto_Empleados.append(proyem)
        cursor.close()
        cnx.close()
        return Proyecto_Empleados
    
    def buscar(self, buscar : int):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql1 = 'select id_proyecto,id_empleado from proyecto_empleado where id_proyecto =%s'
        values1 = (buscar,)
        cursor.execute(sql1,values1)
        result = cursor.fetchone()
        return result
    
    def modificar(self, id_proyecto : int, id_empleado : int) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'update proyecto_empleado set id_proyecto= %s, id_empleado= %s where id_proyecto = %s'
        values = (id_proyecto, id_empleado, id_proyecto)
        try:
            cursor.execute(sql, values)
            cnx.commit()
            filas_afectadas = cursor.rowcount
            if filas_afectadas > 0:
                return True, "Modificación exitosa."
            else:
                return False, "No se encontró el departamento o no hubo cambios."
        except Exception as e:
            return False, f"Error en la modificación: {str(e)}"
        finally:
            cursor.close()
            cnx.close()
    
    def eliminar(self, id_proyecto: int) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'delete from proyecto_empleado where id_proyecto = %s'
        values = (id_proyecto,)
        cursor.execute(sql, values)
        cnx.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        cnx.close()
        return filas_afectadas > 0


    