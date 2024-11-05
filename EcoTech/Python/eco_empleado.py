from mysql.connector import MySQLConnection, connect
from datetime import date

class Empleado:
    def __init__(self, nombre: str, direccion: str, telefono: str, correo: str, inicio_contrato: date, salario:int, departamento_id_departamento : int) -> None:
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.inicio_contrato = inicio_contrato
        self.salario = salario
        self.departamento_id_departamento = departamento_id_departamento

class CrudEmpleado:
    def __init__(self) -> None:
        self.username = 'root'
        self.password = ''
        self.database = 'EcoTech'

    def conectar(self) -> MySQLConnection:
        cnx = connect(user=self.username, password=self.password, database=self.database)
        return cnx
    
    def insertar(self, empleado : Empleado) -> bool:
        # Obtener una conexion
        cnx = self.conectar()
        # Crear un cursor
        cursor = cnx.cursor()
        # Configurar la consulta con parametros
        sql = 'insert into empleado(nombre, direccion, telefono, correo, inicio_contrato, salario, departamento_id_departamento ) values (%s, %s, %s, %s, %s, %s, %s)'
        # Tupla con parametros
        values = (empleado.nombre, empleado.direccion,empleado.telefono,empleado.correo,empleado.inicio_contrato,empleado.salario, empleado.departamento_id_departamento)
        # Ejecutar la consulta + los parametros
        cursor.execute(sql, values)
        # Obtener el id insertado en la tabla persona
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    
    def obtener(self) -> list[Empleado]|None:
        cnx = self.conectar()
        cursor = cnx.cursor()
        query = "select nombre,direccion, telefono, correo, inicio_contrato, salario, departamento_id_departamento from empleado"
        cursor.execute(query)
        result = cursor.fetchall()
        empleados = []
        for row in result:
            emp = Empleado(nombre=row[0], direccion=row[1], telefono=row[2],correo=row[3],inicio_contrato=row[4],salario=[5],departamento_id_departamento=row[6])
            empleados.append(emp)
        cursor.close()
        cnx.close()
        return empleados
    
    def modificar(self, empleado:Empleado, salario:int) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'select id_empleado from empleado where nombre=%s'
        values = (empleado.nombre)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if result is not None:
            id_empleado = result[0]
            sql2 = 'update mecanico set salario=%s where id_empleado=%s'
            values2 = (salario,id_empleado)
            cursor.execute(sql2, values2)
            cnx.commit()
        cursor.close()
        cnx.close()
        return True
    def eliminar(self, empleado:Empleado) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'select id_empleado from persona where nombre=%s'
        values = (empleado.apellido)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if result is not None:
            id_empleado = result[0]
            sql2 = 'delete from empleado where id_persona=%s;'
            values2 = (id_empleado)
            cursor.execute(sql2, values2)
            cnx.commit()
        cursor.close()
        cnx.close()
        return True