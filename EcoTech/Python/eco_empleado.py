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
    
    def buscar(self, buscar):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql1 = 'select nombre, direccion, telefono, correo, inicio_contrato, salario, departamento_id_departamento from empleado where id_empleado=%s'
        values1 = (buscar,)
        cursor.execute(sql1,values1)
        result = cursor.fetchone()
        return result
    
    def modificar(self, empleado:Empleado, id_empleado) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'UPDATE empleado SET nombre = %s, direccion = %s, telefono = %s, correo = %s, inicio_contrato = %s, salario = %s, departamento_id_departamento = %s WHERE id_empleado = %s'
        values = (empleado.nombre, empleado.direccion, empleado.telefono, empleado.correo, empleado.inicio_contrato, empleado.salario, empleado.departamento_id_departamento, id_empleado)
        
        try:
            cursor.execute(sql, values)
            cnx.commit()
            filas_afectadas = cursor.rowcount
            if filas_afectadas > 0:
                return True, "Modificación exitosa."
            else:
                return False, "No se encontró el empleado o no hubo cambios."
        except Exception as e:
            return False, f"Error en la modificación: {str(e)}"
        finally:
            cursor.close()
            cnx.close()

    def eliminar(self, id_usuario) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'delete from empleado where id_empleado = %s'
        values = (id_usuario,)
        cursor.execute(sql, values)
        cnx.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        cnx.close()
        return filas_afectadas > 0