from mysql.connector import MySQLConnection, connect
from modelo import Departamento

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
            dep = Departamento(nombre=row[1], gerente=row[2])
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

