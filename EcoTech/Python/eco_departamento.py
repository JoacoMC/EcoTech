import mysql.connector

class eco_departamento:
    
    def conectar():
        cnx = mysql.connector.connect(username='root', password='',database='EcoTech')
        return cnx
    
    def insertar(nombre:str, gerente: int):
        cnx = eco_departamento.conectar()
        cursor=cnx.cursor()
        sql = 'insert into departamento(nombre, gerente) values (%s, %s);'
        values = (nombre, gerente)
        cursor.execute(sql,values)
        cnx.commit()
        cursor.close()
        cnx.close()
        return 
    
    def obtener():
        cnx = eco_departamento.conectar()
        cursor=cnx.cursor()
        sql = 'select * from departamento'
        cursor.execute(sql)
        resulset = cursor.fetchall()
        for row in resulset:
            print('ID: {}, NOMBRE: {}, GERENTE: {}'.format(row[0],row[1],row[2]))
        cursor.close()
        cnx.close()

    def modificar(nombre:str, gerente: int):
        cnx = eco_departamento.conectar()
        cursor=cnx.cursor()
        sql = 'select id_departamento from departamento where nombre=%s;'
        cursor.execute(sql, nombre)
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

    def eliminar(nombre:str):
        cnx = eco_departamento.conectar()
        cursor=cnx.cursor()
        sql = 'select id_departamento from departamento where nombre=%s ;'
        valor = (nombre,)
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



if input('Desea ingresar algún valor? s/n: ').lower() == 's':
    nombre = input('Ingrese un nombre de departamento: ')
    gerente = int(input('Indique el id del gerente(si es que posee): '))
    eco_departamento.insertar(nombre, gerente)

if input('Desea ver algún dato? s/n: ').lower() == 's':
    eco_departamento.obtener()

if input('Desea modificar algún dato? s/n: ').lower() == 's':
    nombre = input('Ingrese un nombre de departamento a modificar: ')
    gerente = int(input('Indique el id del nuevo gerente: '))
    eco_departamento.modificar(nombre, gerente)

if input('Desea eliminar algún dato? s/n: ').lower() == 's':
    nombre = input('Ingrese un nombre de departamento a eliminar: ')
    eco_departamento.eliminar(nombre)