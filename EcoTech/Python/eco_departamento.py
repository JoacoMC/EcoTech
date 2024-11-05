from mysql.connector import MySQLConnection, connect

class Departamento:
    def __init__(self, nombre : str, gerente : int) -> None:
        self.nombre = nombre
        self.gerente = gerente

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
            dep = Departamento(nombre=row[0], gerente=row[1])
            departamentos.append(dep)
        cnx.close()
        return departamentos

    def modificar(self, departamento: Departamento, gerente: int) -> bool:
        cnx = self.conectar()
        cursor=cnx.cursor()
        sql = 'select id_departamento from departamento where nombre=%s'
        values = (departamento.nombre)
        cursor.execute(sql.values)
        result = cursor.fetchone()
        if result is not None:
            id_departamento = result[0]
            sql2 = 'update departamento set gerente=%s where id_departamento=%s'
            values2 = (gerente, id_departamento)
            cursor.execute(sql2, values2)
            cnx.commit()
        cursor.close()
        cnx.close()
        return

    def eliminar(self, departamento: Departamento) -> bool:
        cnx = self.conectar()
        cursor=cnx.cursor()
        sql = 'select id_departamento from departamento where nombre=%s ;'
        valor = (departamento.nombre)
        cursor.execute(sql, valor)
        result = cursor.fetchone()
        if result is not None:
            id_departamento = result[0]
            sql2 = 'delete from departamento where id_departamento=%s;'
            valor2 = (id_departamento,)
            cursor.execute(sql2, valor2)
            cnx.commit()
        cursor.close()
        cnx.close()
        return

