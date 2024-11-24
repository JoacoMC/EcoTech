from datos import CrudDepartamento,CrudEmpleado,CrudProyecto,CrudProyectoEmpleado,CrudRegistroTiempo,CrudUsuario
from modelo import Proyecto, Proyecto_empleado, Usuario, Departamento, Empleado, RegistroTiempo
import tkinter as tk
import config
from tkinter.ttk import Treeview, Combobox
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
        self.modificar_usuario_frame = None
        self.eliminar_usuario_frame = None
        self.modificar_empleado_frame = None
        self.eliminar_empleado_frame = None
        self.modificar_departamento_frame = None
        self.eliminar_departamento_frame = None
        self.modificar_proyecto_frame = None
        self.eliminar_proyecto_frame = None
        self.modificar_registrotiempo_frame = None
        self.eliminar_registrotiempo_frame = None
        self.modificar_proyectoempleado_frame = None
        self.eliminar_proyectoempleado_frame = None
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
        #boton modificar
        self.modificarbutton = tk.Button(self.usuariohud, text="Modificar", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.modificar_usuario)
        self.modificarbutton.place(x=25, y=175, width=100, height=50)
        #boton eliminar
        self.eliminarbutton = tk.Button(self.usuariohud, text="Eliminar", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.eliminar_usuario)
        self.eliminarbutton.place(x=25, y=250, width=100, height=50)

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
        #boton modificar
        self.modificarbutton = tk.Button(self.empleadohud, text="Modificar", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.modificar_empleado)
        self.modificarbutton.place(x=25, y=175, width=100, height=50)
        #boton eliminar
        self.eliminarbutton = tk.Button(self.empleadohud, text="Eliminar", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.eliminar_empleado)
        self.eliminarbutton.place(x=25, y=250, width=100, height=50)

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
        #boton modificar
        self.nuevobutton = tk.Button(self.departamentohud, text="Modificar", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.modificar_departamento)
        self.nuevobutton.place(x=25, y=175, width=100, height=50)
        #boton eliminar
        self.nuevobutton = tk.Button(self.departamentohud, text="Eliminar", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.eliminar_departamento)
        self.nuevobutton.place(x=25, y=250, width=100, height=50)

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
        #boton modificar
        self.modificarbutton = tk.Button(self.proyectohud, text="Modificar", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.modificar_proyecto)
        self.modificarbutton.place(x=25, y=175, width=100, height=50)
        #boton eliminar
        self.eliminarbutton = tk.Button(self.proyectohud, text="Eliminar", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.eliminar_proyecto)
        self.eliminarbutton.place(x=25, y=250, width=100, height=50)

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
        #boton modificar
        self.modificarbutton = tk.Button(self.registrotiempohud, text="Modificar", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.modificar_registrotiempo)
        self.modificarbutton.place(x=25, y=175, width=100, height=50)
        #boton eliminar
        self.eliminarbutton = tk.Button(self.registrotiempohud, text="Eliminar", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.eliminar_registrotiempo)
        self.eliminarbutton.place(x=25, y=250, width=100, height=50)

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
        #boton modificar
        self.nuevobutton = tk.Button(self.proyectoempleadohud, text="Modificar", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.modificar_proyectoempleado)
        self.nuevobutton.place(x=25, y=175, width=100, height=50)
        #boton eliminar
        self.nuevobutton = tk.Button(self.proyectoempleadohud, text="Eliminar", 
                                       bd=0, bg = config.color2, fg=config.color5, 
                                       activebackground=config.color3, activeforeground=config.color5, command=self.eliminar_proyectoempleado)
        self.nuevobutton.place(x=25, y=250, width=100, height=50)

    def clear_current_frame_app(self):
        if self.ver_usuario_frame is not None:
            self.ver_usuario_frame.destroy()
        if self.nuevo_usuario_frame is not None:
            self.nuevo_usuario_frame.destroy()
        if self.modificar_usuario_frame is not None:
            self.modificar_usuario_frame.destroy()
        if self.eliminar_usuario_frame is not None:
            self.eliminar_usuario_frame.destroy()

        if self.ver_empleado_frame is not None:
            self.ver_empleado_frame.destroy()
        if self.nuevo_empleado_frame is not None:
            self.nuevo_empleado_frame.destroy()
        if self.modificar_empleado_frame is not None:
            self.modificar_empleado_frame.destroy()
        if self.eliminar_empleado_frame is not None:
            self.eliminar_empleado_frame.destroy()

        if self.ver_departamento_frame is not None:
            self.ver_departamento_frame.destroy()
        if self.nuevo_departamento_frame is not None:
            self.nuevo_departamento_frame.destroy()
        if self.modificar_departamento_frame is not None:
            self.modificar_departamento_frame.destroy()
        if self.eliminar_departamento_frame is not None:
            self.eliminar_departamento_frame.destroy()

        if self.ver_proyecto_frame is not None:
            self.ver_proyecto_frame.destroy()
        if self.nuevo_proyecto_frame is not None:
            self.nuevo_proyecto_frame.destroy()
        if self.modificar_proyecto_frame is not None:
            self.modificar_proyecto_frame.destroy()
        if self.eliminar_proyecto_frame is not None:
            self.eliminar_proyecto_frame.destroy()

        if self.ver_registrotiempo_frame is not None:
            self.ver_registrotiempo_frame.destroy()
        if self.nuevo_registrotiempo_frame is not None:
            self.nuevo_registrotiempo_frame.destroy()
        if self.modificar_registrotiempo_frame is not None:
            self.modificar_registrotiempo_frame.destroy()
        if self.eliminar_registrotiempo_frame is not None:
            self.eliminar_registrotiempo_frame.destroy()

        if self.ver_proyectoempleado_frame is not None:
            self.ver_proyectoempleado_frame.destroy()
        if self.nuevo_proyectoempleado_frame is not None:
            self.nuevo_proyectoempleado_frame.destroy()
        if self.modificar_proyectoempleado_frame is not None:
            self.modificar_proyectoempleado_frame.destroy()
        if self.eliminar_proyectoempleado_frame is not None:
            self.eliminar_proyectoempleado_frame.destroy()

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

    def modificar_usuario(self):
        self.clear_current_frame_app()
        self.modificar_usuario_frame = tk.Frame(self.usuariohud, bg= config.color5)
        self.modificar_usuario_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.modificar_usuario_frame, text="Usuarios").grid(row=4, column=0, padx=10, pady=10)
        self.usuario_cmb = Combobox(self.modificar_usuario_frame, state="readonly")
        self.usuario_cmb.grid(row=4, column=1, padx=10, pady=10)
        self.cargar_usuarios()
        self.buscar_btn = tk.Button(self.modificar_usuario_frame, text="Buscar", command=self.buscar_usuario)
        self.buscar_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=20)

    def cargar_usuarios(self):
        usuarios = CrudUsuario().obtener()
        values = [] # valores de la lista desplegable del Combobox
        for c in usuarios:
            values.append("{}".format(c.nombre))
        self.usuario_cmb['values'] = values   

    def buscar_usuario(self):
        try:
            id_buscar = self.id_usuario_ety.get()
            try:
                id_buscar = int(id_buscar)
            except ValueError:
                messagebox.showerror("Error", "La ID debe ser un número.")
                return
            usuario = CrudUsuario().buscar(id_buscar)
            if usuario is None:
                messagebox.showinfo("Buscar Usuario", "Usuario no encontrado.")
            else:
                messagebox.showinfo("Buscar Usuario", "Búsqueda exitosa. Usuario encontrado.")

                # Crear un nuevo Frame para mostrar los detalles del usuario
                self.detalle_usuario_frame = tk.Frame(self.usuariohud, bg=config.color5)
                self.detalle_usuario_frame.place(x=150, y=300, width=900, height=200)

                # Agregar etiquetas y entradas para mostrar los detalles del usuario
                tk.Label(self.detalle_usuario_frame, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
                self.nombre_ety = tk.Entry(self.detalle_usuario_frame)
                self.nombre_ety.grid(row=0, column=1, padx=10, pady=10)
                tk.Label(self.detalle_usuario_frame, text="Contraseña").grid(row=1, column=0, padx=10, pady=10)
                self.contraseña_ety = tk.Entry(self.detalle_usuario_frame)
                self.contraseña_ety.grid(row=1, column=1, padx=10, pady=10)
                tk.Label(self.detalle_usuario_frame, text="Permiso").grid(row=2, column=0, padx=10, pady=10)
                self.permiso_ety = tk.Entry(self.detalle_usuario_frame)
                self.permiso_ety.grid(row=2, column=1, padx=10, pady=10)
                # Botón de ingresos
                self.ingresar_btn = tk.Button(self.detalle_usuario_frame, text="Modificar", command=self.update_usuario)
                self.ingresar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)     

        except Exception as e:
            messagebox.showerror("Buscar Usuario", f"Error en la búsqueda: {str(e)}")
        
    def update_usuario(self):
        try:
            nombre = self.nombre_ety.get()
            contraseña = self.contraseña_ety.get()
            permiso = self.permiso_ety.get()
            
            # Convertir `id_usuario` a entero
            id_usuario = int(self.id_usuario_ety.get())
            
            CrudUsuario().modificar(nombre, contraseña, permiso, id_usuario)
            messagebox.showinfo("Modificar usuario", "Modificación exitosa")
        except Exception as e:
            messagebox.showerror("Modificar usuario", f"Error en modificación: {str(e)}")

    def eliminar_usuario(self):
        self.clear_current_frame_app()
        self.eliminar_usuario_frame = tk.Frame(self.usuariohud, bg= config.color5)
        self.eliminar_usuario_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.eliminar_usuario_frame, text="ID Usuario").grid(row=0, column=0, padx=10, pady=10)
        self.id_usuario_ety = tk.Entry(self.eliminar_usuario_frame)
        self.id_usuario_ety.grid(row=0, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.buscar_btn = tk.Button(self.eliminar_usuario_frame, text="Buscar", command=self.delete_usuario)
        self.buscar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    def delete_usuario(self):
        try:
            id_buscar = self.id_usuario_ety.get()
            try:
                id_buscar = int(id_buscar)
            except ValueError:
                messagebox.showerror("Error", "La ID debe ser un número.")
                return
            usuario = CrudUsuario().eliminar(id_buscar)
            if usuario is None:
                messagebox.showinfo("Eliminar Usuario", "Usuario no encontrado.")
            else:
                messagebox.showinfo("Eliminar Usuario", "Eliminacion exitosa!.")

        except Exception as e:
            messagebox.showerror("Eliminar Usuario", f"Error en la búsqueda: {str(e)}")

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

    def modificar_empleado(self):
        self.clear_current_frame_app()
        self.modificar_empleado_frame = tk.Frame(self.empleadohud, bg= config.color5)
        self.modificar_empleado_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.modificar_empleado_frame, text="ID Empleado").grid(row=0, column=0, padx=10, pady=10)
        self.id_empleado_ety = tk.Entry(self.modificar_empleado_frame)
        self.id_empleado_ety.grid(row=0, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.buscar_btn = tk.Button(self.modificar_empleado_frame, text="Buscar", command=self.buscar_empleado)
        self.buscar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    def buscar_empleado(self):
        try:
            id_buscar = self.id_empleado_ety.get()
            
            # Validar que la ID sea un número
            try:
                id_buscar = int(id_buscar)
            except ValueError:
                messagebox.showerror("Error", "La ID debe ser un número.")
                return
            
            # Buscar el empleado en la base de datos
            empleado = CrudEmpleado().buscar(id_buscar)
            
            if empleado is None:
                messagebox.showinfo("Buscar Empleado", "Empleado no encontrado.")
            else:
                messagebox.showinfo("Buscar Empleado", "Búsqueda exitosa. Empleado encontrado.")

                # Crear un nuevo Frame para mostrar los detalles del empleado
                self.detalle_empleado_frame = tk.Frame(self.empleadohud, bg=config.color5)
                self.detalle_empleado_frame.place(x=150, y=225, width=900, height=600)

                # Crear campos de entrada y poblarlos con datos del empleado
                tk.Label(self.detalle_empleado_frame, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
                self.nombre_ety = tk.Entry(self.detalle_empleado_frame)
                self.nombre_ety.grid(row=0, column=1, padx=10, pady=10)
                

                tk.Label(self.detalle_empleado_frame, text="Dirección").grid(row=1, column=0, padx=10, pady=10)
                self.direccion_ety = tk.Entry(self.detalle_empleado_frame)
                self.direccion_ety.grid(row=1, column=1, padx=10, pady=10)
                

                tk.Label(self.detalle_empleado_frame, text="Teléfono").grid(row=2, column=0, padx=10, pady=10)
                self.telefono_ety = tk.Entry(self.detalle_empleado_frame)
                self.telefono_ety.grid(row=2, column=1, padx=10, pady=10)
                

                tk.Label(self.detalle_empleado_frame, text="Correo").grid(row=3, column=0, padx=10, pady=10)
                self.correo_ety = tk.Entry(self.detalle_empleado_frame)
                self.correo_ety.grid(row=3, column=1, padx=10, pady=10)
                

                tk.Label(self.detalle_empleado_frame, text="Inicio Contrato").grid(row=4, column=0, padx=10, pady=10)
                self.inicio_contrato_ety = tk.Entry(self.detalle_empleado_frame)
                self.inicio_contrato_ety.grid(row=4, column=1, padx=10, pady=10)
                

                tk.Label(self.detalle_empleado_frame, text="Salario").grid(row=5, column=0, padx=10, pady=10)
                self.salario_ety = tk.Entry(self.detalle_empleado_frame)
                self.salario_ety.grid(row=5, column=1, padx=10, pady=10)
                

                tk.Label(self.detalle_empleado_frame, text="Departamento").grid(row=6, column=0, padx=10, pady=10)
                self.departamento_ety = tk.Entry(self.detalle_empleado_frame)
                self.departamento_ety.grid(row=6, column=1, padx=10, pady=10)

                # Botón de modificación
                self.modificar_btn = tk.Button(self.detalle_empleado_frame, text="Modificar", command=self.update_empleado)
                self.modificar_btn.grid(row=7, column=1, columnspan=2, padx=20, pady=20)
    
        except Exception as e:
            messagebox.showerror("Buscar Empleado", f"Error en la búsqueda: {str(e)}")

    def update_empleado(self):
        try:
            nombre = self.nombre_ety.get()
            direccion = self.direccion_ety.get()
            telefono = self.telefono_ety.get()
            correo = self.correo_ety.get()
            inicio_contrato = self.inicio_contrato_ety.get()
            salario = self.salario_ety.get()
            departamento = self.departamento_ety.get()
            id_buscar = int(self.id_empleado_ety.get())
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
            success, message = CrudEmpleado().modificar(nuevo_empleado, id_buscar)
            
            if success:
                messagebox.showinfo("Modificar Empleado", message)
            else:
                messagebox.showerror("Modificar Empleado", message)
    
            self.nombre_ety.delete(0, tk.END)
            self.direccion_ety.delete(0, tk.END)
            self.telefono_ety.delete(0, tk.END)
            self.correo_ety.delete(0, tk.END)
            self.inicio_contrato_ety.delete(0, tk.END)
            self.salario_ety.delete(0, tk.END)
            self.departamento_ety.delete(0, tk.END)
        
        except Exception as e:
            messagebox.showerror("Modificar Empleado", f"Error inesperado: {str(e)}")

    def eliminar_empleado(self):
        self.clear_current_frame_app()
        self.eliminar_empleado_frame = tk.Frame(self.empleadohud, bg= config.color5)
        self.eliminar_empleado_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.eliminar_empleado_frame, text="ID Empleado").grid(row=0, column=0, padx=10, pady=10)
        self.id_empleado_ety = tk.Entry(self.eliminar_empleado_frame)
        self.id_empleado_ety.grid(row=0, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.buscar_btn = tk.Button(self.eliminar_empleado_frame, text="Buscar", command=self.delete_empleado)
        self.buscar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    def delete_empleado(self):
        try:
            id_buscar = self.id_empleado_ety.get()
            try:
                id_buscar = int(id_buscar)
            except ValueError:
                messagebox.showerror("Error", "La ID debe ser un número.")
                return
            usuario = CrudEmpleado().eliminar(id_buscar)
            if usuario is None:
                messagebox.showinfo("Eliminar Empleado", "Empleado no encontrado.")
            else:
                messagebox.showinfo("Eliminar Empleado", "Eliminacion exitosa!.")

        except Exception as e:
            messagebox.showerror("Eliminar Empleado", f"Error en la búsqueda: {str(e)}")
        
    def ver_departamento(self):
        self.clear_current_frame_app()
        self.ver_departamento_frame = tk.Frame(self.departamentohud, bg= config.color5)
        self.ver_departamento_frame.place(x=150, y= 25, width=900, height=600)
        self.departamento_tbl = Treeview(self.ver_departamento_frame, columns=("nombre", "gerente"), show="headings", height=10)
        self.departamento_tbl.heading("nombre", text="Nombre")
        self.departamento_tbl.column("nombre", width=200)
        self.departamento_tbl.heading("gerente", text="Gerente")
        self.departamento_tbl.column("gerente", width=150)
        self.departamento_tbl.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.actualizar_departamento()

    def actualizar_departamento(self):
        for item in self.departamento_tbl.get_children():
            self.departamento_tbl.delete(item) 
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

    def modificar_departamento(self):
        self.clear_current_frame_app()
        self.modificar_departamento_frame = tk.Frame(self.departamentohud, bg= config.color5)
        self.modificar_departamento_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.modificar_departamento_frame, text="ID deparmento").grid(row=0, column=0, padx=10, pady=10)
        self.id_departamento_ety = tk.Entry(self.modificar_departamento_frame)
        self.id_departamento_ety.grid(row=0, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.buscar_btn = tk.Button(self.modificar_departamento_frame, text="Buscar", command=self.buscar_departamento)
        self.buscar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)
    
    def buscar_departamento(self):
        try:
            id_buscar = self.id_departamento_ety.get()
            try:
                id_buscar = int(id_buscar)
            except ValueError:
                messagebox.showerror("Error", "La ID debe ser un número.")
                return
            departamento = CrudDepartamento().buscar(id_buscar)
            if departamento is None:
                messagebox.showinfo("Buscar Departamento", "Departamento no encontrado.")
            else:
                messagebox.showinfo("Buscar Departamento", "Búsqueda exitosa. Departamento encontrado.")

                # Crear un nuevo Frame para mostrar los detalles del departamento
                self.detalle_departamento_frame = tk.Frame(self.departamentohud, bg=config.color5)
                self.detalle_departamento_frame.place(x=150, y=300, width=900, height=200)

                # Agregar etiquetas y entradas para mostrar los detalles del usuario
                tk.Label(self.detalle_departamento_frame, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
                self.nombre_ety = tk.Entry(self.detalle_departamento_frame)
                self.nombre_ety.grid(row=0, column=1, padx=10, pady=10)
                tk.Label(self.detalle_departamento_frame, text="Gerente").grid(row=1, column=0, padx=10, pady=10)
                self.gerente_ety = tk.Entry(self.detalle_departamento_frame)
                self.gerente_ety.grid(row=1, column=1, padx=10, pady=10)
                
                # Botón de ingresos
                self.ingresar_btn = tk.Button(self.detalle_departamento_frame, text="Ingresar", command=self.update_departamento)
                self.ingresar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)    

        except Exception as e:
            messagebox.showerror("Buscar Departamento", f"Error en la búsqueda: {str(e)}")

    def update_departamento(self):
        try:
            nombre = self.nombre_ety.get()
            gerente = self.gerente_ety.get()
            
            # Convertir `id_usuario` a entero
            id_departamento = int(self.id_departamento_ety.get())
            gerente = int(self.gerente_ety.get())
            
            CrudDepartamento().modificar(nombre, gerente, id_departamento)
            messagebox.showinfo("Modificar departamento", "Modificación exitosa")
        except Exception as e:
            messagebox.showerror("Modificar departamento", f"Error en modificación: {str(e)}")

    def eliminar_departamento(self):
        self.clear_current_frame_app()
        self.eliminar_departamento_frame = tk.Frame(self.departamentohud, bg= config.color5)
        self.eliminar_departamento_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.eliminar_departamento_frame, text="ID Departamento").grid(row=0, column=0, padx=10, pady=10)
        self.id_departamento_ety = tk.Entry(self.eliminar_departamento_frame)
        self.id_departamento_ety.grid(row=0, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.buscar_btn = tk.Button(self.eliminar_departamento_frame, text="Buscar", command=self.delete_departamento)
        self.buscar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    def delete_departamento(self):
        try:
            id_buscar = self.id_departamento_ety.get()
            try:
                id_buscar = int(id_buscar)
            except ValueError:
                messagebox.showerror("Error", "La ID debe ser un número.")
                return
            departamento = CrudDepartamento().eliminar(id_buscar)
            if departamento is None:
                messagebox.showinfo("Eliminar Departamento", "Departamento no encontrado.")
            else:
                messagebox.showinfo("Eliminar Departamento", "Eliminacion exitosa!.")

        except Exception as e:
            messagebox.showerror("Eliminar Departamento", f"Error en la búsqueda: {str(e)}")

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
            
    def buscar_proyecto(self):
        try:
            id_buscar = self.id_proyecto_ety.get()
            try:
                id_buscar = int(id_buscar)
            except ValueError:
                messagebox.showerror("Error", "La ID debe ser un número.")
                return
            proyecto = CrudProyecto().buscar(id_buscar)
            if proyecto is None:
                messagebox.showinfo("Buscar Proyecto", "Proyecto no encontrado.")
            else:
                messagebox.showinfo("Buscar Proyecto", "Búsqueda exitosa. Proyecto encontrado.")

                # Crear un nuevo Frame para mostrar los detalles del usuario
                self.detalle_proyecto_frame = tk.Frame(self.proyectohud, bg=config.color5)
                self.detalle_proyecto_frame.place(x=150, y=300, width=900, height=200)

                # Agregar etiquetas y entradas para mostrar los detalles del usuario
                tk.Label(self.detalle_proyecto_frame, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
                self.nombre_ety = tk.Entry(self.detalle_proyecto_frame)
                self.nombre_ety.grid(row=0, column=1, padx=10, pady=10)
                tk.Label(self.detalle_proyecto_frame, text="Descipción").grid(row=1, column=0, padx=10, pady=10)
                self.descripcion_ety = tk.Entry(self.detalle_proyecto_frame)
                self.descripcion_ety.grid(row=1, column=1, padx=10, pady=10)
                tk.Label(self.detalle_proyecto_frame, text="Fecha inicio").grid(row=2, column=0, padx=10, pady=10)
                self.fecha_inicio_ety = tk.Entry(self.detalle_proyecto_frame)
                self.fecha_inicio_ety.grid(row=2, column=1, padx=10, pady=10)
                
                # Botón de ingresos
                self.ingresar_btn = tk.Button(self.detalle_proyecto_frame, text="Ingresar", command=self.update_proyecto)
                self.ingresar_btn.grid(row=7, column=0, columnspan=2, padx=20, pady=20)    

        except Exception as e:
            messagebox.showerror("Buscar Proyecto", f"Error en la búsqueda: {str(e)}")

    def update_proyecto(self):
        try:
            nombre = self.nombre_ety.get()
            descripcion = self.descripcion_ety.get()
            fecha_inicio = self.fecha_inicio_ety.get()
            
            # Convertir `id_usuario` a entero
            id_proyecto = int(self.id_proyecto_ety.get())
            
            CrudProyecto().modificar(nombre, descripcion, fecha_inicio, id_proyecto)
            messagebox.showinfo("Modificar proyecto", "Modificación exitosa")
        except Exception as e:
            messagebox.showerror("Modificar proyecto", f"Error en modificación: {str(e)}")

    def eliminar_proyecto(self):
        self.clear_current_frame_app()
        self.eliminar_proyecto_frame = tk.Frame(self.proyectohud, bg= config.color5)
        self.eliminar_proyecto_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.eliminar_proyecto_frame, text="ID Proyecto").grid(row=0, column=0, padx=10, pady=10)
        self.id_proyecto_ety = tk.Entry(self.eliminar_proyecto_frame)
        self.id_proyecto_ety.grid(row=0, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.buscar_btn = tk.Button(self.eliminar_proyecto_frame, text="Buscar", command=self.delete_proyecto)
        self.buscar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)
        
    def modificar_proyecto(self):
        self.clear_current_frame_app()
        self.modificar_proyecto_frame = tk.Frame(self.proyectohud, bg= config.color5)
        self.modificar_proyecto_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.modificar_proyecto_frame, text="ID Proyecto").grid(row=0, column=0, padx=10, pady=10)
        self.id_proyecto_ety = tk.Entry(self.modificar_proyecto_frame)
        self.id_proyecto_ety.grid(row=0, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.buscar_btn = tk.Button(self.modificar_proyecto_frame, text="Buscar", command=self.buscar_proyecto)
        self.buscar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)
    
    def delete_proyecto(self):
        try:
            id_buscar = self.id_proyecto_ety.get()
            try:
                id_buscar = int(id_buscar)
            except ValueError:
                messagebox.showerror("Error", "La ID debe ser un número.")
                return
            proyecto = CrudProyecto().eliminar(id_buscar)
            if proyecto is None:
                messagebox.showinfo("Eliminar proyecto", "proyecto no encontrado.")
            else:
                messagebox.showinfo("Eliminar proyecto", "Eliminacion exitosa!.")

        except Exception as e:
            messagebox.showerror("Eliminar proyecto", f"Error en la búsqueda: {str(e)}")
    
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
        self.actualizar_registrotiempo()

    def actualizar_registrotiempo(self):
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
        self.ingresar_btn = tk.Button(self.nuevo_registrotiempo_frame, text="Ingresar", command=self.ingresar_registrotiempo)
        self.ingresar_btn.grid(row=7, column=0, columnspan=2, padx=20, pady=20)

    def buscar_registrotiempo(self):
        try:
            id_buscar = self.id_registro_tiempo_ety.get()
            try:
                id_buscar = int(id_buscar)
            except ValueError:
                messagebox.showerror("Error", "La ID debe ser un número.")
                return
            registro_tiempo = CrudRegistroTiempo().buscar(id_buscar)
            if registro_tiempo is None:
                messagebox.showinfo("Buscar Registro Tiempo", "Registro Tiempo no encontrado.")
            else:
                messagebox.showinfo("Buscar Registro", "Búsqueda exitosa. Registro Tiempo encontrado.")

                # Crear un nuevo Frame para mostrar los detalles del usuario
                self.detalle_registro_tiempo_frame = tk.Frame(self.registrotiempohud, bg=config.color5)
                self.detalle_registro_tiempo_frame.place(x=150, y=250, width=900, height=600)

                # Agregar etiquetas y entradas para mostrar los detalles del usuario
                tk.Label(self.detalle_registro_tiempo_frame, text="Fecha").grid(row=0, column=0, padx=10, pady=10)
                self.fecha_ety = tk.Entry(self.detalle_registro_tiempo_frame)
                self.fecha_ety.grid(row=0, column=1, padx=10, pady=10)
                tk.Label(self.detalle_registro_tiempo_frame, text="Cantidad horas").grid(row=1, column=0, padx=10, pady=10)
                self.cantidad_horas_ety = tk.Entry(self.detalle_registro_tiempo_frame)
                self.cantidad_horas_ety.grid(row=1,column=1,padx=10,pady=10)
                tk.Label(self.detalle_registro_tiempo_frame, text="Descripcion").grid(row=2, column=0, padx=10, pady=10)
                self.descripcion_ety = tk.Entry(self.detalle_registro_tiempo_frame)
                self.descripcion_ety.grid(row=2, column=1, padx=10, pady=10)
                tk.Label(self.detalle_registro_tiempo_frame, text="ID Empleado").grid(row=3, column=0, padx=10, pady=10)
                self.id_empleado_ety = tk.Entry(self.detalle_registro_tiempo_frame)
                self.id_empleado_ety.grid(row=3, column=1, padx=10, pady=10)
                tk.Label(self.detalle_registro_tiempo_frame, text="ID proyecto").grid(row=4, column=0, padx=10, pady=10)
                self.id_proyecto_ety = tk.Entry(self.detalle_registro_tiempo_frame)
                self.id_proyecto_ety.grid(row=4, column=1, padx=10, pady=10)
                # Botón de ingresos
                self.ingresar_btn = tk.Button(self.detalle_registro_tiempo_frame, text="Ingresar", command=self.update_registrotiempo)
                self.ingresar_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=20)
                
        except Exception as e:
            messagebox.showerror("Buscar Registro Tiempo", f"Error en la búsqueda: {str(e)}")

    def ingresar_registrotiempo(self):
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

    def modificar_registrotiempo(self):
        self.clear_current_frame_app()
        self.modificar_registro_tiempo_frame = tk.Frame(self.registrotiempohud, bg= config.color5)
        self.modificar_registro_tiempo_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.modificar_registro_tiempo_frame, text="ID Registro Tiempo").grid(row=0, column=0, padx=10, pady=10)
        self.id_registro_tiempo_ety = tk.Entry(self.modificar_registro_tiempo_frame)
        self.id_registro_tiempo_ety.grid(row=0, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.buscar_btn = tk.Button(self.modificar_registro_tiempo_frame, text="Buscar", command=self.buscar_registrotiempo)
        self.buscar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)
        
    def update_registrotiempo(self):
        try:
            fecha = self.fecha_ety.get()
            cantidad_horas = self.cantidad_horas_ety.get()
            descripcion = self.descripcion_ety.get()
            id_empleado = self.id_empleado_ety.get()
            id_proyecto = int(self.id_proyecto_ety.get())
            id_registro = int(self.id_registro_tiempo_ety.get())
            
            CrudRegistroTiempo().modificar(id_registro, fecha, cantidad_horas, descripcion, id_empleado, id_proyecto)
            messagebox.showinfo("Modificar Registro Tiempo", "Modificación exitosa")
        except Exception as e:
            messagebox.showerror("Modificar Registro Tiempo", f"Error en modificación: {str(e)}")

    def eliminar_registrotiempo(self):
        self.clear_current_frame_app()
        self.eliminar_registro_tiempo_frame = tk.Frame(self.registrotiempohud, bg= config.color5)
        self.eliminar_registro_tiempo_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.eliminar_registro_tiempo_frame, text="ID Registro Tiempo").grid(row=0, column=0, padx=10, pady=10)
        self.id_proyecto_ety = tk.Entry(self.eliminar_registro_tiempo_frame)
        self.id_proyecto_ety.grid(row=0, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.buscar_btn = tk.Button(self.eliminar_registro_tiempo_frame, text="Buscar", command=self.delete_registrotiempo)
        self.buscar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    def delete_registrotiempo(self):
        try:
            id_buscar = self.id_registro_tiempo_ety.get()
            try:
                id_buscar = int(id_buscar)
            except ValueError:
                messagebox.showerror("Error", "La ID debe ser un número.")
                return
            proyecto = CrudRegistroTiempo().eliminar(id_buscar)
            if proyecto is None:
                messagebox.showinfo("Eliminar Registro Tiempo", "Proyecto no encontrado.")
            else:
                messagebox.showinfo("Eliminar Registro Tiempo", "Eliminacion exitosa!.")

        except Exception as e:
            messagebox.showerror("Eliminar Registro Tiempo", f"Error en la búsqueda: {str(e)}")

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

    def modificar_proyectoempleado(self):
        self.clear_current_frame_app()
        self.modificar_proyecto_empleado_frame = tk.Frame(self.proyectoempleadohud, bg= config.color5)
        self.modificar_proyecto_empleado_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.modificar_proyecto_empleado_frame, text="ID Proyecto Empleado").grid(row=0, column=0, padx=10, pady=10)
        self.id_proyecto_empleado_ety = tk.Entry(self.modificar_proyecto_empleado_frame)
        self.id_proyecto_empleado_ety.grid(row=0, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.buscar_btn = tk.Button(self.modificar_proyecto_empleado_frame, text="Buscar", command=self.buscar_proyecto_empleado)
        self.buscar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    def buscar_proyecto_empleado(self):
        try:
            id_buscar = self.id_proyecto_empleado_ety.get()
            try:
                id_buscar = int(id_buscar)
            except ValueError:
                messagebox.showerror("Error", "La ID debe ser un número.")
                return
            proyecto_empleado = CrudProyectoEmpleado().buscar(id_buscar)
            if proyecto_empleado is None:
                messagebox.showinfo("Buscar Proyecto Empleado", "Proyecto Empleado no encontrado.")
            else:
                messagebox.showinfo("Buscar Proyecto", "Búsqueda exitosa. Proyecto Empleado encontrado.")

                # Crear un nuevo Frame para mostrar los detalles del usuario
                self.detalle_proyecto_empleado_frame = tk.Frame(self.proyectoempleadohud, bg=config.color5)
                self.detalle_proyecto_empleado_frame.place(x=150, y=300, width=900, height=200)

                # Agregar etiquetas y entradas para mostrar los detalles del usuario
                tk.Label(self.detalle_proyecto_empleado_frame, text="ID proyecto").grid(row=0, column=0, padx=10, pady=10)
                self.id_proyecto_ety = tk.Entry(self.detalle_proyecto_empleado_frame)
                self.id_proyecto_ety.grid(row=0, column=1, padx=10, pady=10)
                tk.Label(self.detalle_proyecto_empleado_frame, text="ID empleado").grid(row=1, column=0, padx=10, pady=10)
                self.id_empleado_ety = tk.Entry(self.detalle_proyecto_empleado_frame)
                self.id_empleado_ety.grid(row=1, column=1, padx=10, pady=10)
                
                # Botón de ingresos
                self.ingresar_btn = tk.Button(self.detalle_proyecto_empleado_frame, text="Ingresar", command=self.update_proyecto_empleado)
                self.ingresar_btn.grid(row=7, column=0, columnspan=2, padx=20, pady=20) 
        except Exception as e:
            messagebox.showerror("Buscar Proyecto Empleado", f"Error en la búsqueda: {str(e)}")

    def update_proyecto_empleado(self):
        try:
            id_proyecto = self.id_proyecto_ety.get()
            id_empleado = self.id_empleado_ety.get()
            
            # Convertir `id_usuario` a entero
            id_proyecto = int(self.id_proyecto_ety.get())
            id_empleado = int(self.id_empleado_ety.get())
            
            CrudProyectoEmpleado().modificar(id_empleado, id_proyecto)
            messagebox.showinfo("Modificar Proyecto Empleado", "Modificación exitosa")
        except Exception as e:
            messagebox.showerror("Modificar Proyecto Empleado", f"Error en modificación: {str(e)}")

    def eliminar_proyectoempleado(self):
        self.clear_current_frame_app()
        self.eliminar_proyecto_empleado_frame = tk.Frame(self.proyectoempleadohud, bg= config.color5)
        self.eliminar_proyecto_empleado_frame.place(x=150, y= 25, width=900, height=600)

        tk.Label(self.eliminar_proyecto_empleado_frame, text="ID Proyecto").grid(row=0, column=0, padx=10, pady=10)
        self.id_proyecto_empleado_ety = tk.Entry(self.eliminar_proyecto_empleado_frame)
        self.id_proyecto_empleado_ety.grid(row=0, column=1, padx=10, pady=10)
        # Botón de ingresos
        self.buscar_btn = tk.Button(self.eliminar_proyecto_empleado_frame, text="Buscar", command=self.delete_proyecto_empleado)
        self.buscar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    def delete_proyecto_empleado(self):
        try:
            id_buscar = self.id_proyecto_empleado_ety.get()
            try:
                id_buscar = int(id_buscar)
            except ValueError:
                messagebox.showerror("Error", "La ID debe ser un número.")
                return
            proyecto_empleado = CrudProyectoEmpleado().eliminar(id_buscar)
            if proyecto_empleado is None:
                messagebox.showinfo("Eliminar Proyecto Empleado", "Proyecto no encontrado.")
            else:
                messagebox.showinfo("Eliminar Proyecto Empleado", "Eliminacion exitosa!.")

        except Exception as e:
            messagebox.showerror("Eliminar Proyecto Empleado", f"Error en la búsqueda: {str(e)}")

root = tk.Tk()
app = Aplicacion(root)
root.mainloop()