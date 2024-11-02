import eco_empleado
import eco_usuario
import eco_departamento
import eco_proyecto
import eco_registro_tiempo
import eco_proyecto_empleado
import tkinter as tk
import config

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
        self.frames()
        self.upperbar_controls()
        self.sidebar_controls()

    def frames(self):
        self.upperbar = tk.Frame(self.root, bg= config.color2, height=50)
        self.upperbar.pack(side=tk.TOP, fill='both')

        self.sidebar = tk.Frame(self.root, bg= config.color2, width=150)
        self.sidebar.pack(side=tk.LEFT, fill='both', expand=False)

        self.center = tk.Frame(self.root, bg= config.color5)
        self.center.pack(side=tk.RIGHT, fill='both', expand=True)

    def upperbar_controls(self):
        self.titulo = tk.Label(self.upperbar, text="Eco Tech")
        self.titulo.config(fg="white", font=("Roboto", 15), bg=config.color2, pady=10, width=16)
        self.titulo.pack(side=tk.LEFT)

        self.buttonsidebar = tk.Button(self.upperbar, text="O", 
                                       bd=0, bg = config.color2, fg="white")
        self.buttonsidebar.pack(side=tk.LEFT)

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
        self.usuariohud= tk.Frame(self.center, bg= config.color3)
        self.usuariohud.pack(side=tk.RIGHT, fill='both', expand=True)

    def empleado_frame(self):
        self.clear_current_frame()
        self.empleadohud= tk.Frame(self.center, bg= config.color4)
        self.empleadohud.pack(side=tk.RIGHT, fill='both', expand=True)

    def departamento_frame(self):
        self.clear_current_frame()
        self.departamentohud= tk.Frame(self.center, bg= config.color1)
        self.departamentohud.pack(side=tk.RIGHT, fill='both', expand=True)

    def proyecto_frame(self):
        self.clear_current_frame()
        self.proyectohud= tk.Frame(self.center, bg= config.color2)
        self.proyectohud.pack(side=tk.RIGHT, fill='both', expand=True)

    def registrotiempo_frame(self):
        self.clear_current_frame()
        self.registrotiempohud= tk.Frame(self.center, bg= config.color4)
        self.registrotiempohud.pack(side=tk.RIGHT, fill='both', expand=True)

    def proyectoempleado_frame(self):
        self.clear_current_frame()
        self.proyectoempleadohud= tk.Frame(self.center, bg= config.color1)
        self.proyectoempleadohud.pack(side=tk.RIGHT, fill='both', expand=True)


root = tk.Tk()
app = Aplicacion(root)
root.mainloop()