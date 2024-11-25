from datetime import date

class Departamento:
    def __init__(self, id_departamento:int, nombre : str, gerente : int) -> None:
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.gerente = gerente

class Proyecto:
    def __init__(self,id_proyecto:int, nombre: str, descripcion: str, fecha_inicio: date) -> None:
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio

class RegistroTiempo:
    def __init__(self, id_registro_tiempo:id, fecha: date, cantidad_horas: int, descripcion: str, id_empleado: int, id_proyecto: int) -> None:
        self.id_registro_tiempo = id_registro_tiempo
        self.fecha = fecha
        self.cantidad_horas = cantidad_horas
        self.descripcion = descripcion
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto

class Usuario:
    def __init__(self, id_usuario : int, nombre : str, contraseña : str, permiso : str, id_empleado: int):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.contraseña = contraseña
        self.permiso = permiso
        self.id_empleado = id_empleado

class Proyecto_empleado:
    def __init__(self, id_proyecto: int, id_empleado: int) -> None:
        self.id_proyecto = id_proyecto
        self.id_empleado = id_empleado

class Empleado:
    def __init__(self, id_empleado:int, nombre: str, direccion: str, telefono: str, correo: str, inicio_contrato: date, salario:int, id_departamento : int) -> None:
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.inicio_contrato = inicio_contrato
        self.salario = salario
        self.id_departamento = id_departamento


