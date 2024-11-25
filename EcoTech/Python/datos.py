from mysql.connector import MySQLConnection, connect
from modelo import Departamento,Empleado,Proyecto_empleado,Proyecto,RegistroTiempo,Usuario
from datetime import date

class CrudDepartamento:
    def __init__(self):
        self.username = 'root'
        self.password = ''
        self.database = 'EcoTech'

    def conectar(self) -> MySQLConnection:
        cnx = connect(username='root', password='',database='EcoTech')
        return cnx
    
    def insertar(self, departamento : Departamento):
        cnx = self.conectar()
        cursor=cnx.cursor()
        sql = 'insert into departamento(nombre, gerente) values (%s, %s);'
        values = (departamento.nombre, departamento.gerente)
        cursor.execute(sql,values)
        cnx.commit()
        cursor.close()
        cnx.close()
        return 
    
    def obtener(self):
        cnx = self.conectar()
        cursor=cnx.cursor()
        sql = 'select * from departamento'
        cursor.execute(sql)
        resulset = cursor.fetchall()
        departamentos = []
        for row in resulset:
            dep = Departamento(id_departamento= row[0],nombre=row[1], gerente=row[2])
            departamentos.append(dep)
        cnx.close()
        return departamentos
    
    def buscar(self, buscar):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql1 = 'select nombre, gerente from departamento where id_departamento=%s'
        values1 = (buscar,)
        cursor.execute(sql1,values1)
        result = cursor.fetchone()
        return result
    
    def buscar_por_nombre(self, buscar):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql1 = 'select id_departamento from departamento where nombre=%s'
        values1 = (buscar,)
        cursor.execute(sql1,values1)
        result = cursor.fetchone()
        return result[0]
    
    def modificar(self, nombre : str, gerente: int, id_departamento) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'update departamento set nombre= %s, gerente= %s where id_departamento = %s'
        values = (nombre, gerente,id_departamento)
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

    def eliminar(self, id_departamento: int) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'delete from departamento where id_departamento = %s'
        values = (id_departamento,)
        cursor.execute(sql, values)
        cnx.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        cnx.close()
        return filas_afectadas > 0

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
        sql = 'insert into empleado(nombre, direccion, telefono, correo, inicio_contrato, salario, departamento_id_departamento) values (%s, %s, %s, %s, %s, %s, %s)'
        # Tupla con parametros
        values = (empleado.nombre, empleado.direccion,empleado.telefono,empleado.correo,empleado.inicio_contrato,empleado.salario, empleado.id_departamento)
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
        query = "select id_empleado, nombre, direccion, telefono, correo, inicio_contrato, salario, departamento_id_departamento from empleado"
        cursor.execute(query)
        result = cursor.fetchall()
        empleados = []
        for row in result:
            emp = Empleado(id_empleado= row[0], nombre=row[1], direccion=row[2], telefono=row[3],correo=row[4],inicio_contrato=row[5],salario=[6],id_departamento=row[7])
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
    
    def obtener_ultima_id(self):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'select max(id_empleado) from empleado'
        cursor.execute(sql)
        id_empleado = cursor.lastrowid
        return id_empleado
    
    def buscar_por_nombre(self, buscar):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql1 = 'select id_empleado from empleado where nombre=%s'
        values1 = (buscar,)
        cursor.execute(sql1,values1)
        result = cursor.fetchone()
        return result[0]
    
    def modificar(self, empleado:Empleado, id_empleado) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'UPDATE empleado SET nombre = %s, direccion = %s, telefono = %s, correo = %s, inicio_contrato = %s, salario = %s, departamento_id_departamento = %s WHERE id_empleado = %s'
        values = (empleado.nombre, empleado.direccion, empleado.telefono, empleado.correo, empleado.inicio_contrato, empleado.salario, empleado.id_departamento, id_empleado)
        
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

    def buscar(self, buscar):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql1 = 'select fecha, cantidad_horas, descripcion, empleado_id_empleado, proyecto_id_proyecto from registro_tiempo where proyecto_id_proyecto = %s'
        values1 = (buscar,)
        cursor.execute(sql1,values1)
        result = cursor.fetchone()
        return result
    
    def modificar(self, id_registro: int, fecha : date, nuevas_horas: int, nueva_descripcion: str, id_empleado : int, id_proyecto : int) -> bool:
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'update registro_tiempo set fecha = %s, cantidad_horas = %s, descripcion = %s, empleado_id_empleado=%s, proyecto_id_proyecto=%s where id_registro_tiempo = %s'
        values = (fecha, nuevas_horas, nueva_descripcion, id_empleado, id_proyecto, id_registro)
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

class CrudUsuario:
    def __init__(self):
        self.username = 'root'
        self.password = ''
        self.database = 'EcoTech'

    def conectar(self) -> MySQLConnection:
        cnx = connect(user=self.username, password=self.password, database=self.database)
        return cnx
    
    def insertar(self, usuario : Usuario):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'insert into usuario (id_usuario, nombre, contraseña, permiso, id_empleado) values (%s, %s, %s, %s, %s)'
        values = (usuario.id_usuario, usuario.nombre, usuario.contraseña, usuario.permiso, usuario.id_empleado)
        cursor.execute(sql, values)
        id_registro = cursor.lastrowid
        cnx.commit()
        cursor.close()
        cnx.close()
        return id_registro

    def obtener_ultima_id(self):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'select max(id_usuario) from usuario'
        cursor.execute(sql)
        id_usuario = cursor.fetchone()
        print(id_usuario)
        cursor.close()
        cnx.close()
        return id_usuario[0]

    def obtener(self):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'select id_usuario, nombre, contraseña, permiso, id_empleado from usuario'
        cursor.execute(sql)
        resultset = cursor.fetchall()
        usuarios = []
        for row in resultset:
            usu = Usuario(id_usuario= row[0], nombre=row[1], contraseña=row[2],permiso=row[3], id_empleado=row[4])
            usuarios.append(usu)
        cursor.close()
        cnx.close()
        return usuarios

    def buscar(self, buscar : int):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql1 = 'select nombre, contraseña, permiso from usuario where id_usuario=%s'
        values1 = (buscar,)
        cursor.execute(sql1,values1)
        result = cursor.fetchone()
        return result
    
    def buscar_por_nombre(self, buscar):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql1 = 'select id_usuario from usuario where nombre=%s'
        values1 = (buscar,)
        cursor.execute(sql1,values1)
        result = cursor.fetchone()
        return result[0]
    
    def modificar(self, nombre : str, contraseña : str, permiso : str, id_usuario : int):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'update usuario set nombre = %s, contraseña = %s, permiso = %s where id_usuario = %s'
        values = (nombre, contraseña, permiso, id_usuario)
        cursor.execute(sql, values)
        cnx.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        cnx.close()
        return filas_afectadas > 0

    def eliminar(self, id_usuario):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'delete from usuario where id_usuario = %s'
        values = (id_usuario,)
        cursor.execute(sql, values)
        cnx.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        cnx.close()
        return filas_afectadas > 0

