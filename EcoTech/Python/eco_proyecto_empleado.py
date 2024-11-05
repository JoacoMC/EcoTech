from mysql.connector import MySQLConnection, connect

class Proyecto_empleado:
    def __init__(self, id_proyecto: int, id_empleado: int) -> None:
        self.id_proyecto = id_proyecto
        self.id_empleado = id_empleado

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

    def eliminar(self, proyecto_empleado:Proyecto_empleado) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'select id_proyecto where id_empleado = %s'
        values = (proyecto_empleado.id_proyecto,proyecto_empleado.id_empleado)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if result is not None:
            id_proyecto = result[0]
            sql2 = 'delete from proyecto_empleado where id_proyecto=%s;'
            values2 = (proyecto_empleado.id_proyecto,proyecto_empleado.id_empleado )
            cursor.execute(sql2, values2)
            sql3 = 'delete from proyecto_empleado where id_empleado=%s'
            values3 = (proyecto_empleado.id_proyecto,proyecto_empleado.id_empleado)
            cursor.execute(sql3, values3)
            cnx.commit()
        cursor.close()
        cnx.close()
        return True


    