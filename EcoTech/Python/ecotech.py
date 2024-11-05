from eco_empleado import CrudEmpleado, Empleado
from eco_usuario import CrudUsuario, Usuario
from eco_departamento import CrudDepartamento, Departamento 
from eco_proyecto import CrudProyecto, Proyecto 
from eco_registro_tiempo import CrudRegistroTiempo, RegistroTiempo
from eco_proyecto_empleado import CrudProyectoEmpleado, Proyecto_empleado
import tkinter as tk
import config
from tkinter.ttk import Treeview
from tkinter import messagebox
from datetime import datetime

class Aplicacion():
    def __init__(self, root:tk.Tk) -> None:
        self.root = root
        self.root.title('Eco Tech')
        self.root.geometry('1280x720')
        self.usuariohud = None
        self.empleadohud = None
        self.departamentohud = None
        self.proyectohud = None
        self.registrotiempohud = None
        self.proyectoempleadohud = None
        self.ver_usuario_frame = None
        self.nuevo_usuario_frame = None
        self.ver_empleado_frame = None
        self.nuevo_empleado_frame = None
        self.ver_departamento_frame = None
        self.nuevo_departamento_frame = None
        self.ver_proyecto_frame = None
        self.nuevo_proyecto_frame = None
        self.ver_registrotiempo_frame = None
        self.nuevo_registrotiempo_frame = None
        self.ver_proyectoempleado_frame = None
        self.nuevo_proyectoempleado_frame = None
        self.frames()
        self.upperbar_controls()
        self.sidebar_controls()

    def frames(self):
        self.upperbar = tk.Frame(self.root, bg= config.color2, height=50)
        self.upperbar.pack(side=tk.TOP, fill='both')

        self.sidebar = tk.Frame(self.root, bg= config.color3, width=150)
        self.sidebar.pack(side=tk.LEFT, fill='both', expand=False)

        self.center = tk.Frame(self.root, bg= config.color5)
        self.center.pack(side=tk.RIGHT, fill='both', expand=True)

    def upperbar_controls(self):
        self.titulo = tk.Label(self.upperbar, text="Eco Tech")
        self.titulo.config(fg="white", font=("Roboto", 15), bg=config.color2, pady=10, width=16)
        self.titulo.pack(side=tk.LEFT)

        self.buttonsidebar = tk.Button(self.upperbar, text="O", 
                                       bd=0, bg = config.color2, fg="white", command=self.buttonupperbar)
        self.buttonsidebar.pack(side=tk.LEFT)

    def buttonupperbar(self):
        if self.sidebar.winfo_ismapped():
            self.sidebar.pack_forget()
        else:
            self.sidebar.pack(side=tk.LEFT, fill='y')

    def sidebar_controls(self):
        #boton usuario
        self.usuariobutton = tk.Button(self.sidebar, text="Usuario", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.usuario_frame)
        self.usuariobutton.place(x=25, y=25, width=100, height=50)
        #boton empleado
        self.empleadobutton = tk.Button(self.sidebar, text="Empleado", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.empleado_frame)
        self.empleadobutton.place(x=25, y=100, width=100, height=50)
        #boton departamento
        self.departamentobutton = tk.Button(self.sidebar, text="departamento", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.departamento_frame)
        self.departamentobutton.place(x=25, y=175, width=100, height=50)
        #boton proyecto
        self.proyectobutton = tk.Button(self.sidebar, text="proyecto", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.proyecto_frame)
        self.proyectobutton.place(x=25, y=250, width=100, height=50)
        #boton registrotiempo
        self.registrotiempobutton = tk.Button(self.sidebar, text="registro de tiempo", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.registrotiempo_frame)
        self.registrotiempobutton.place(x=25, y=325, width=100, height=50)
        #boton proyectoempleado
        self.proyectoempleadobutton = tk.Button(self.sidebar, text="proyecto-empleado", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.proyectoempleado_frame)
        self.proyectoempleadobutton.place(x=25, y=400, width=100, height=50)
    
    def clear_current_frame(self):
        if self.usuariohud is not None:
            self.usuariohud.destroy()
        if self.empleadohud is not None:
            self.empleadohud.destroy()
        if self.departamentohud is not None:
            self.departamentohud.destroy()
        if self.proyectohud is not None:
            self.proyectohud.destroy()
        if self.registrotiempohud is not None:
            self.registrotiempohud.destroy()
        if self.proyectoempleadohud is not None:
            self.proyectoempleadohud.destroy()

    def usuario_frame(self):
        self.clear_current_frame()
        self.usuariohud= tk.Frame(self.center, bg= config.color4)
        self.usuariohud.pack(side=tk.RIGHT, fill='both', expand=True)
        #boton ver
        self.verbutton = tk.Button(self.usuariohud, text="Ver", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.ver_usuario)
        self.verbutton.place(x=25, y=25, width=100, height=50)
        #boton nuevo
        self.nuevobutton = tk.Button(self.usuariohud, text="Nuevo", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.nuevo_usuario)
        self.nuevobutton.place(x=25, y=100, width=100, height=50)

    def empleado_frame(self):
        self.clear_current_frame()
        self.empleadohud= tk.Frame(self.center, bg= config.color4)
        self.empleadohud.pack(side=tk.RIGHT, fill='both', expand=True)
        self.verbutton = tk.Button(self.empleadohud, text="Ver", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.ver_empleado)
        self.verbutton.place(x=25, y=25, width=100, height=50)
        #boton nuevo
        self.nuevobutton = tk.Button(self.empleadohud, text="Nuevo", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.nuevo_empleado)
        self.nuevobutton.place(x=25, y=100, width=100, height=50)

    def departamento_frame(self):
        self.clear_current_frame()
        self.departamentohud= tk.Frame(self.center, bg= config.color4)
        self.departamentohud.pack(side=tk.RIGHT, fill='both', expand=True)
        self.verbutton = tk.Button(self.departamentohud, text="Ver", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.ver_departamento)
        self.verbutton.place(x=25, y=25, width=100, height=50)
        #boton nuevo
        self.nuevobutton = tk.Button(self.departamentohud, text="Nuevo", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.nuevo_departamento)
        self.nuevobutton.place(x=25, y=100, width=100, height=50)

    def proyecto_frame(self):
        self.clear_current_frame()
        self.proyectohud= tk.Frame(self.center, bg= config.color4)
        self.proyectohud.pack(side=tk.RIGHT, fill='both', expand=True)
        self.verbutton = tk.Button(self.proyectohud, text="Ver", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.ver_proyecto)
        self.verbutton.place(x=25, y=25, width=100, height=50)
        #boton nuevo
        self.nuevobutton = tk.Button(self.proyectohud, text="Nuevo", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.nuevo_proyecto)
        self.nuevobutton.place(x=25, y=100, width=100, height=50)

    def registrotiempo_frame(self):
        self.clear_current_frame()
        self.registrotiempohud= tk.Frame(self.center, bg= config.color4)
        self.registrotiempohud.pack(side=tk.RIGHT, fill='both', expand=True)
        self.verbutton = tk.Button(self.registrotiempohud, text="Ver", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.ver_registrotiempo)
        self.verbutton.place(x=25, y=25, width=100, height=50)
        #boton nuevo
        self.nuevobutton = tk.Button(self.registrotiempohud, text="Nuevo", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.nuevo_registrotiempo)
        self.nuevobutton.place(x=25, y=100, width=100, height=50)

    def proyectoempleado_frame(self):
        self.clear_current_frame()
        self.proyectoempleadohud= tk.Frame(self.center, bg= config.color4)
        self.proyectoempleadohud.pack(side=tk.RIGHT, fill='both', expand=True)
        self.verbutton = tk.Button(self.proyectoempleadohud, text="Ver", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.ver_proyectoempleado)
        self.verbutton.place(x=25, y=25, width=100, height=50)
        #boton nuevo
        self.nuevobutton = tk.Button(self.proyectoempleadohud, text="Nuevo", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.nuevo_proyectoempleado)
        self.nuevobutton.place(x=25, y=100, width=100, height=50)

    def clear_current_frame_app(self):
        if self.ver_usuario_frame is not None:
            self.ver_usuario_frame.destroy()
        if self.nuevo_usuario_frame is not None:
            self.nuevo_usuario_frame.destroy()

        if self.ver_empleado_frame is not None:
            self.ver_empleado_frame.destroy()
        if self.nuevo_empleado_frame is not None:
            self.nuevo_empleado_frame.destroy()

        if self.ver_departamento_frame is not None:
            self.ver_departamento_frame.destroy()
        if self.nuevo_departamento_frame is not None:
            self.nuevo_departamento_frame.destroy()

        if self.ver_proyecto_frame is not None:
            self.ver_proyecto_frame.destroy()
        if self.nuevo_proyecto_frame is not None:
            self.nuevo_proyecto_frame.destroy()

        if self.ver_registrotiempo_frame is not None:
            self.ver_registrotiempo_frame.destroy()
        if self.nuevo_registrotiempo_frame is not None:
            self.nuevo_registrotiempo_frame.destroy()

        if self.ver_proyectoempleado_frame is not None:
            self.ver_proyectoempleado_frame.destroy()
        if self.nuevo_proyectoempleado_frame is not None:
            self.nuevo_proyectoempleado_frame.destroy()

    def ver_usuario(self):
        self.clear_current_frame_app()
        self.ver_usuario_frame = tk.Frame(self.usuariohud, bg= config.color5)
        self.ver_usuario_frame.place(x=150, y= 25, width=900, height=600)
        self.usuarios_tbl = Treeview(self.ver_usuario_frame, columns=("nombre", "permiso", "id_empleado"), show="headings")
        self.usuarios_tbl.heading("nombre", text="Nombre")
        self.usuarios_tbl.heading("permiso", text="permiso")
        self.usuarios_tbl.heading("id_empleado", text="id_empleado") 
        self.usuarios_tbl.grid(row=0, column=0, padx=20, pady=20)
        self.actualizar_usuarios()
            
    def actualizar_usuarios(self) -> None:
        for item in self.usuarios_tbl.get_children():
            self.usuarios_tbl.delete(item) 
        # Obtener la lista de usuarios desde el CRUD y agregar al Treeview
        usuarios = CrudUsuario().obtener()
        for usuario in usuarios:
            self.usuarios_tbl.insert("", "end", values=(usuario.nombre, usuario.permiso, usuario.id_empleado))

    def nuevo_usuario(self):
        self.clear_current_frame_app()
        self.nuevo_usuario_frame = tk.Frame(self.usuariohud, bg= config.color5)
        self.nuevo_usuario_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.nuevo_usuario_frame, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        self.nombre_ety = tk.Entry(self.nuevo_usuario_frame)
        self.nombre_ety.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_usuario_frame, text="Contraseña").grid(row=1, column=0, padx=10, pady=10)
        self.contraseña_ety = tk.Entry(self.nuevo_usuario_frame)
        self.contraseña_ety.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_usuario_frame, text="Permiso").grid(row=2, column=0, padx=10, pady=10)
        self.permiso_ety = tk.Entry(self.nuevo_usuario_frame)
        self.permiso_ety.grid(row=2, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_usuario_frame, text="ID empleado").grid(row=3, column=0, padx=10, pady=10)
        self.id_empleado_ety = tk.Entry(self.nuevo_usuario_frame)
        self.id_empleado_ety.grid(row=3, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.ingresar_btn = tk.Button(self.nuevo_usuario_frame, text="Ingresar", command=self.ingresarusuario)
        self.ingresar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    def ingresarusuario(self):
        try:
            nombre = self.nombre_ety.get()
            contraseña = self.contraseña_ety.get()
            permiso = self.permiso_ety.get()
            id_empleado = self.id_empleado_ety
            try:
                id_empleado = int(id_empleado)
            except ValueError:
                messagebox.showerror("Error", "Salario y Departamento deben ser números.")
                return
            nuevo= Usuario(nombre, contraseña, permiso, id_empleado)
            CrudUsuario().insertar(nuevo)
            messagebox.showinfo("Nuevo mecánico", "Ingreso exitoso")
        except:
            messagebox.showerror("Nuevo mecánico", "Error en ingreso")

    def ver_empleado(self):
        self.clear_current_frame_app()
        self.ver_empleado_frame = tk.Frame(self.empleadohud, bg= config.color5)
        self.ver_empleado_frame.place(x=150, y= 25, width=900, height=600)
        self.empleados_tbl = Treeview(self.ver_empleado_frame, columns=("nombre", "direccion", "telefono", "correo", "inicio_contrato", "salario", "departamento"), 
                              show="headings", height=10)
        self.empleados_tbl.heading("nombre", text="Nombre")
        self.empleados_tbl.column("nombre", width=100)
        self.empleados_tbl.heading("direccion", text="Direccion")
        self.empleados_tbl.column("direccion", width=150)
        self.empleados_tbl.heading("telefono", text="Telefono")
        self.empleados_tbl.column("telefono", width=100)
        self.empleados_tbl.heading("correo", text="Correo")
        self.empleados_tbl.column("correo", width=150)
        self.empleados_tbl.heading("inicio_contrato", text="Inicio Contrato")
        self.empleados_tbl.column("inicio_contrato", width=120) 
        self.empleados_tbl.heading("salario", text="Salario")
        self.empleados_tbl.column("salario", width=80)
        self.empleados_tbl.heading("departamento", text="Departamento")
        self.empleados_tbl.column("departamento", width=100)
        self.empleados_tbl.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.actualizar_empleados()
            
    def actualizar_empleados(self) -> None:
        for item in self.empleados_tbl.get_children():
            self.empleados_tbl.delete(item) 
        empleados = CrudEmpleado().obtener()
        for empleado in empleados:
            self.empleados_tbl.insert("", "end", values=(empleado.nombre, empleado.direccion, empleado.telefono, empleado.correo, empleado.inicio_contrato, empleado.salario, empleado.departamento_id_departamento))

    def nuevo_empleado(self):
        self.clear_current_frame_app()
        self.nuevo_empleado_frame = tk.Frame(self.empleadohud, bg= config.color5)
        self.nuevo_empleado_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.nuevo_empleado_frame, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        self.nombre_ety = tk.Entry(self.nuevo_empleado_frame)
        self.nombre_ety.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_empleado_frame, text="Direccion").grid(row=1, column=0, padx=10, pady=10)
        self.direccion_ety = tk.Entry(self.nuevo_empleado_frame)
        self.direccion_ety.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_empleado_frame, text="Telefono").grid(row=2, column=0, padx=10, pady=10)
        self.telefono_ety = tk.Entry(self.nuevo_empleado_frame)
        self.telefono_ety.grid(row=2, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_empleado_frame, text="Correo").grid(row=3, column=0, padx=10, pady=10)
        self.correo_ety = tk.Entry(self.nuevo_empleado_frame)
        self.correo_ety.grid(row=3, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_empleado_frame, text="Inicio Contrato").grid(row=4, column=0, padx=10, pady=10)
        self.inicio_contrato_ety = tk.Entry(self.nuevo_empleado_frame)
        self.inicio_contrato_ety.grid(row=4, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_empleado_frame, text="Salario").grid(row=5, column=0, padx=10, pady=10)
        self.salario_ety = tk.Entry(self.nuevo_empleado_frame)
        self.salario_ety.grid(row=5, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_empleado_frame, text="Departamento").grid(row=6, column=0, padx=10, pady=10)
        self.departamento_ety = tk.Entry(self.nuevo_empleado_frame)
        self.departamento_ety.grid(row=6, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.ingresar_btn = tk.Button(self.nuevo_empleado_frame, text="Ingresar", command=self.ingresarempleado)
        self.ingresar_btn.grid(row=7, column=0, columnspan=2, padx=20, pady=20)

    def ingresarempleado(self):
        try:
            nombre = self.nombre_ety.get()
            direccion = self.direccion_ety.get()
            telefono = self.telefono_ety.get()
            correo = self.correo_ety.get()
            inicio_contrato = self.inicio_contrato_ety.get()
            salario = self.salario_ety.get()
            departamento = self.departamento_ety.get()
            
            if not nombre or not direccion or not telefono or not correo or not inicio_contrato or not salario or not departamento:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return
            
            try:
                inicio_contrato = datetime.strptime(inicio_contrato, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Fecha de inicio de contrato inválida. Use el formato YYYY-MM-DD.")
                return

            try:
                salario = int(salario)
                departamento = int(departamento)
            except ValueError:
                messagebox.showerror("Error", "Salario y Departamento deben ser números.")
                return
            
            nuevo_empleado = Empleado(nombre, direccion, telefono, correo, inicio_contrato, salario, departamento)
            CrudEmpleado().insertar(nuevo_empleado)
            messagebox.showinfo("Nuevo empleado", "Ingreso exitoso")
            
            self.nombre_ety.delete(0, tk.END)
            self.direccion_ety.delete(0, tk.END)
            self.telefono_ety.delete(0, tk.END)
            self.correo_ety.delete(0, tk.END)
            self.inicio_contrato_ety.delete(0, tk.END)
            self.salario_ety.delete(0, tk.END)
            self.departamento_ety.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Nuevo empleado", f"Error en ingreso: {e}")

    def ver_departamento(self):
        self.clear_current_frame_app()
        self.ver_departamento_frame = tk.Frame(self.departamentohud, bg= config.color5)
        self.ver_departamento_frame.place(x=150, y= 25, width=900, height=600)
        self.departamento_tbl = Treeview(self.ver_departamento_frame, columns=("nombre", "gerente"), show="headings", height=10)
        self.departamento_tbl.heading("nombre", text="Nombre")
        self.departamento_tbl.column("nombre", width=100)
        self.departamento_tbl.heading("gerente", text="Gerente")
        self.departamento_tbl.column("gerente", width=150)
        self.departamento_tbl.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.actualizar_departamento()

    def actualizar_departamento(self):
        for item in self.departamento_tbl.get_children():
            self.departamento_tbl.delete(item) 
        # Obtener la lista de usuarios desde el CRUD y agregar al Treeview
        departamentos = CrudDepartamento().obtener()
        for departamento in departamentos:
            self.departamento_tbl.insert("", "end", values=(departamento.nombre, departamento.gerente))

    def nuevo_departamento(self):
        self.clear_current_frame_app()
        self.nuevo_departamento_frame = tk.Frame(self.departamentohud, bg= config.color5)
        self.nuevo_departamento_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.nuevo_departamento_frame, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        self.nombre_ety = tk.Entry(self.nuevo_departamento_frame)
        self.nombre_ety.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_departamento_frame, text="Gerente").grid(row=1, column=0, padx=10, pady=10)
        self.gerente_ety = tk.Entry(self.nuevo_departamento_frame)
        self.gerente_ety.grid(row=1, column=1, padx=10, pady=10)
        self.ingresar_btn = tk.Button(self.nuevo_departamento_frame, text="Ingresar", command=self.ingresar_departamento)
        self.ingresar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    def ingresar_departamento(self):
        try:
            nombre = self.nombre_ety.get()
            gerente = int(self.gerente_ety.get())
            nuevo= Departamento(nombre, gerente)
            CrudDepartamento().insertar(nuevo)
            messagebox.showinfo("Nuevo Departamento", "Ingreso exitoso")
            self.nombre_ety.delete(0, tk.END)
            self.gerente_ety.delete(0, tk.END)
        except:
            messagebox.showerror("Nuevo Departamento", "Error en ingreso")

    def ver_proyecto(self):
        self.clear_current_frame_app()
        self.ver_proyecto_frame = tk.Frame(self.proyectohud, bg= config.color5)
        self.ver_proyecto_frame.place(x=150, y= 25, width=900, height=600)
        self.proyecto_tbl = Treeview(self.ver_proyecto_frame, columns=("nombre", "gerente"), show="headings", height=10)
        self.proyecto_tbl.heading("nombre", text="Nombre")
        self.proyecto_tbl.column("nombre", width=100)
        self.proyecto_tbl.heading("gerente", text="Gerente")
        self.proyecto_tbl.column("gerente", width=150)
        self.proyecto_tbl.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.actualizar_proyecto()

    def actualizar_proyecto(self):
        for item in self.proyecto_tbl.get_children():
            self.proyecto_tbl.delete(item) 
        # Obtener la lista de usuarios desde el CRUD y agregar al Treeview
        proyectos = CrudProyecto().obtener()
        for proyecto in proyectos:
            self.proyecto_tbl.insert("", "end", values=(proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio))

    def nuevo_proyecto(self):
        self.clear_current_frame_app()
        self.nuevo_proyecto_frame = tk.Frame(self.proyectohud, bg= config.color5)
        self.nuevo_proyecto_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.nuevo_proyecto_frame, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        self.nombre_ety = tk.Entry(self.nuevo_proyecto_frame)
        self.nombre_ety.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_proyecto_frame, text="Descripcion").grid(row=1, column=0, padx=10, pady=10)
        self.descripcion_ety = tk.Entry(self.nuevo_proyecto_frame)
        self.descripcion_ety.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_proyecto_frame, text="Fecha Inicio").grid(row=2, column=0, padx=10, pady=10)
        self.fecha_inicio_ety = tk.Entry(self.nuevo_proyecto_frame)
        self.fecha_inicio_ety.grid(row=2, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.ingresar_btn = tk.Button(self.nuevo_proyecto_frame, text="Ingresar", command=self.ingresar_proyecto)
        self.ingresar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    def ingresar_proyecto(self):
        try:
            nombre = self.nombre_ety.get()
            descripcion = self.descripcion_ety.get()
            fecha_inicio = self.fecha_inicio_ety.get()
            
            try:
                fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Fecha de inicio inválida. Use el formato YYYY-MM-DD.")
                return

            nuevo= Proyecto(nombre, descripcion, fecha_inicio)
            CrudProyecto().insertar(nuevo)
            messagebox.showinfo("Nuevo Proyecto", "Ingreso exitoso")

            self.nombre_ety.delete(0, tk.END)
            self.descripcion_ety.delete(0, tk.END)
            self.fecha_inicio_ety.delete(0, tk.END)
        except:
            messagebox.showerror("Nuevo Proyecto", "Error en ingreso")
    
    def ver_registrotiempo(self):
        self.clear_current_frame_app()
        self.ver_registrotiempo_frame = tk.Frame(self.registrotiempohud, bg= config.color5)
        self.ver_registrotiempo_frame.place(x=150, y= 25, width=900, height=600)

        self.registrotiempo_tbl = Treeview(self.ver_registrotiempo_frame, columns=("fecha", "cantidad_horas", "descripcion", "id_empleado", "id_proyecto"), 
                              show="headings", height=10)
        self.registrotiempo_tbl.heading("fecha", text="Fecha")
        self.registrotiempo_tbl.column("fecha", width=100)
        self.registrotiempo_tbl.heading("cantidad_horas", text="Cantidad Horas")
        self.registrotiempo_tbl.column("cantidad_horas", width=150)
        self.registrotiempo_tbl.heading("descripcion", text="Descripcion")
        self.registrotiempo_tbl.column("descripcion", width=100)
        self.registrotiempo_tbl.heading("id_empleado", text="ID empleado")
        self.registrotiempo_tbl.column("id_empleado", width=150)
        self.registrotiempo_tbl.heading("id_proyecto", text="ID proyecto")
        self.registrotiempo_tbl.column("id_proyecto", width=120) 
        self.registrotiempo_tbl.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.actualizar_registro_tiempo()

    def actualizar_registro_tiempo(self):
        for item in self.registrotiempo_tbl.get_children():
            self.registrotiempo_tbl.delete(item) 
        registrotiempos = CrudRegistroTiempo().obtener()
        for registrotiempo in registrotiempos:
            self.registrotiempo_tbl.insert("", "end", values=(registrotiempo.fecha, registrotiempo.cantidad_horas, registrotiempo.descripcion,
                                                               registrotiempo.id_empleado, registrotiempo.id_proyecto))
            
    def nuevo_registrotiempo(self):
        self.clear_current_frame_app()
        self.nuevo_registrotiempo_frame = tk.Frame(self.registrotiempohud, bg= config.color5)
        self.nuevo_registrotiempo_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.nuevo_registrotiempo_frame, text="Fecha").grid(row=0, column=0, padx=10, pady=10)
        self.fecha_ety = tk.Entry(self.nuevo_registrotiempo_frame)
        self.fecha_ety.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_registrotiempo_frame, text="Cantidad de horas").grid(row=1, column=0, padx=10, pady=10)
        self.cantidad_horas_ety = tk.Entry(self.nuevo_registrotiempo_frame)
        self.cantidad_horas_ety.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_registrotiempo_frame, text="Descripcion").grid(row=2, column=0, padx=10, pady=10)
        self.descripcion_ety = tk.Entry(self.nuevo_registrotiempo_frame)
        self.descripcion_ety.grid(row=2, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_registrotiempo_frame, text="ID Empleado").grid(row=3, column=0, padx=10, pady=10)
        self.id_empleado_ety = tk.Entry(self.nuevo_registrotiempo_frame)
        self.id_empleado_ety.grid(row=3, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_registrotiempo_frame, text="ID Proyecto").grid(row=4, column=0, padx=10, pady=10)
        self.id_proyecto_ety = tk.Entry(self.nuevo_registrotiempo_frame)
        self.id_proyecto_ety.grid(row=4, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.ingresar_btn = tk.Button(self.nuevo_registrotiempo_frame, text="Ingresar", command=self.ingresar_registro_tiempo)
        self.ingresar_btn.grid(row=7, column=0, columnspan=2, padx=20, pady=20)

    def ingresar_registro_tiempo(self):
        try:
            fecha = self.fecha_ety.get()
            cantidad_horas = self.cantidad_horas_ety.get()
            descripcion = self.descripcion_ety.get()
            id_empleado = self.id_empleado_ety.get()
            id_proyecto = self.id_proyecto_ety.get()
            
            if not fecha or not cantidad_horas or not descripcion or not id_empleado or not id_empleado or not id_proyecto:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return
            
            try:
                fecha = datetime.strptime(fecha, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Fecha de inicio de contrato inválida. Use el formato YYYY-MM-DD.")
                return
            
            try:
                cantidad_horas = int(cantidad_horas)

            except ValueError:
                messagebox.showerror("Error", "Cantidad de horas debe ser número.")
                return
            
            nuevo_empleado = RegistroTiempo(fecha, cantidad_horas, descripcion, id_empleado, id_proyecto)
            CrudRegistroTiempo().insertar(nuevo_empleado)
            messagebox.showinfo("Nuevo Registro de tiempo", "Ingreso exitoso")
            
            self.fecha_ety.delete(0, tk.END)
            self.cantidad_horas_ety.delete(0, tk.END)
            self.descripcion_ety.delete(0, tk.END)
            self.id_empleado_ety.delete(0, tk.END)
            self.id_proyecto_ety.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Nuevo Registro de tiempo", f"Error en ingreso: {e}")

    def ver_proyectoempleado(self):
        self.clear_current_frame_app()
        self.ver_proyectoempleado_frame = tk.Frame(self.proyectoempleadohud, bg= config.color5)
        self.ver_proyectoempleado_frame.place(x=150, y= 25, width=900, height=600)

        self.proyecto_empleado_tbl = Treeview(self.ver_proyectoempleado_frame, columns=( "id_proyecto", "id_empleado"), show="headings", height=10)
        self.proyecto_empleado_tbl.heading("id_proyecto", text="ID PROYECTO")
        self.proyecto_empleado_tbl.column("id_proyecto", width=150)
        self.proyecto_empleado_tbl.heading("id_empleado", text="ID EMPLEADO")
        self.proyecto_empleado_tbl.column("id_empleado", width=100)
        self.proyecto_empleado_tbl.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.actualizar_proyecto_empleado()

    def actualizar_proyecto_empleado(self):
        for item in self.proyecto_empleado_tbl.get_children():
            self.proyecto_empleado_tbl.delete(item) 
        # Obtener la lista de usuarios desde el CRUD y agregar al Treeview
        proyecto_empleados = CrudProyectoEmpleado().obtener()
        for proyecto_empleado in proyecto_empleados:
            self.proyecto_empleado_tbl.insert("", "end", values=(proyecto_empleado.id_proyecto, proyecto_empleado.id_empleado))

    def nuevo_proyectoempleado(self):
        self.clear_current_frame_app()
        self.nuevo_proyectoempleado_frame = tk.Frame(self.proyectoempleadohud, bg= config.color5)
        self.nuevo_proyectoempleado_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.nuevo_proyectoempleado_frame, text="ID Proyecto").grid(row=0, column=0, padx=10, pady=10)
        self.id_proyecto_ety = tk.Entry(self.nuevo_proyectoempleado_frame)
        self.id_proyecto_ety.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.nuevo_proyectoempleado_frame, text="ID Empleado").grid(row=1, column=0, padx=10, pady=10)
        self.id_empleado_ety = tk.Entry(self.nuevo_proyectoempleado_frame)
        self.id_empleado_ety.grid(row=1, column=1, padx=10, pady=10)
        self.ingresar_btn = tk.Button(self.nuevo_proyectoempleado_frame, text="Ingresar", command=self.ingresar_proyecto_empleado)
        self.ingresar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    def ingresar_proyecto_empleado(self):
        try:
            id_proyecto = self.id_proyecto_ety.get()
            id_empleado = int(self.id_empleado_ety.get())
            nuevo= Proyecto_empleado(id_proyecto, id_empleado)
            try:
                id_proyecto = int(id_proyecto)
                id_empleado = int(id_empleado)

            except ValueError:
                messagebox.showerror("Error", "Cantidad de horas debe ser número.")
                return

            CrudProyectoEmpleado().insertar(nuevo)
            messagebox.showinfo("Nuevo Departamento", "Ingreso exitoso")
            self.id_proyecto_ety.delete(0, tk.END)
            self.id_empleado_ety.delete(0, tk.END)

        except:
            messagebox.showerror("Nuevo Departamento", "Error en ingreso")
root = tk.Tk()
app = Aplicacion(root)
root.mainloop()