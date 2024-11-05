from mysql.connector import MySQLConnection, connect
from datetime import date

class RegistroTiempo:
    def __init__(self, fecha: date, cantidad_horas: int, descripcion: str, id_empleado: int, id_proyecto: int) -> None:
        self.fecha = fecha
        self.cantidad_horas = cantidad_horas
        self.descripcion = descripcion
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto

class CrudRegistroTiempo:
    def __init__(self) -> None:
        self.username = 'root'
        self.password = ''
        self.database = 'EcoTech'

    def conectar(self) -> MySQLConnection:
        cnx = connect(user=self.username, password=self.password, database=self.database)
        return cnx
    
    def insertar(self, registro: RegistroTiempo) -> int:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'insert into registro_tiempo (fecha, cantidad_horas, descripcion, empleado_id_empleado, proyecto_id_proyecto) values (%s, %s, %s, %s, %s)'
        values = (registro.fecha, registro.cantidad_horas, registro.descripcion, registro.id_empleado, registro.id_proyecto)
        cursor.execute(sql, values)
        cnx.commit()
        cursor.close()
        cnx.close()
    
    def obtener(self) -> list[RegistroTiempo]:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'select fecha, cantidad_horas, descripcion, empleado_id_empleado, proyecto_id_proyecto from registro_tiempo'
        cursor.execute(sql)
        resultset = cursor.fetchall()
        registros = []
        for row in resultset:
            reg = RegistroTiempo(fecha=row[0], cantidad_horas=row[1], descripcion=row[2], id_empleado=row[3], id_proyecto=row[4])
            registros.append(reg)
        cursor.close()
        cnx.close()
        return registros

    def obtener_por_empleado(self, id_empleado: int) -> list[RegistroTiempo]:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'select fecha, cantidad_horas, descripcion, empleado_id_empleado, proyecto_id_proyecto from registro_tiempo where empleado_id_empleado = %s'
        values = (id_empleado,)
        cursor.execute(sql, values)
        resultset = cursor.fetchall()
        registros = []
        for row in resultset:
            reg = RegistroTiempo(
                fecha=row[0], cantidad_horas=row[1], descripcion=row[2], id_empleado=row[3], id_proyecto=row[4])
            registros.append(reg)
        cursor.close()
        cnx.close()
        return registros

    def obtener_por_proyecto(self, id_proyecto: int) -> list[RegistroTiempo]:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'select fecha, cantidad_horas, descripcion, empleado_id_empleado, proyecto_id_proyecto from registro_tiempo where proyecto_id_proyecto = %s'
        values = (id_proyecto,)
        cursor.execute(sql, values)
        resultset = cursor.fetchall()
        registros = []
        for row in resultset:
            reg = RegistroTiempo(fecha=row[0], cantidad_horas=row[1], descripcion=row[2], id_empleado=row[3], id_proyecto=row[4])
            registros.append(reg)
        cursor.close()
        cnx.close()
        return registros

    def modificar(self, id_registro: int, nuevas_horas: int, nueva_descripcion: str) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'update registro_tiempo set cantidad_horas = %s, descripcion = %s where id_registro_tiempo = %s'
        values = (nuevas_horas, nueva_descripcion, id_registro)
        cursor.execute(sql, values)
        cnx.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        cnx.close()
        return filas_afectadas > 0

    def eliminar(self, id_registro: int) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'delete from registro_tiempo where id_registro_tiempo = %s'
        values = (id_registro,)
        cursor.execute(sql, values)
        cnx.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        cnx.close()
        return filas_afectadas > 0