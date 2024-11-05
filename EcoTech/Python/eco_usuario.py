from mysql.connector import MySQLConnection, connect

class Usuario:

    def __init__(self, id_usuario : int, nombre : str, contraseña : str, permiso : str, id_empleado: int):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.contraseña = contraseña
        self.permiso = permiso
        self.id_empleado = id_empleado


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

    def modificar(self, usuario : Usuario):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'update usuario set nombre = %s, contraseña = %s, permiso = %s where id_usuario = %s'
        values = (usuario.nombre, usuario.contraseña, usuario.permiso, usuario.id_usuario)
        cursor.execute(sql, values)
        cnx.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        cnx.close()
        return filas_afectadas > 0

    def eliminar(self, usuario : Usuario):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql = 'delete from usuario where id_usuario = %s'
        values = (usuario.id_usuario,)
        cursor.execute(sql, values)
        cnx.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        cnx.close()
        return filas_afectadas > 0
