import customtkinter as ctk

from views.dashboard_docente import DashboardDocente
from views.dashboard_estudiante import DashboardEstudiante
from views.lista_estudiantes import ListaEstudiantes


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SeleccionRol(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Sistema Académico")
        self.geometry("1200x700")
        self.resizable(False, False)

        self.configure(fg_color="#0B1026")

        self.crear_interfaz()

    def crear_interfaz(self):

        titulo = ctk.CTkLabel(
            self,
            text="Sistema Inteligente de\nSeguimiento Académico",
            font=("Segoe UI", 34, "bold")
        )

        titulo.pack(pady=(60, 10))

        subtitulo = ctk.CTkLabel(
            self,
            text="Seleccione su perfil académico para continuar",
            font=("Segoe UI", 16)
        )

        subtitulo.pack()

        contenedor = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        contenedor.pack(pady=60)

        self.crear_tarjeta_docente(contenedor)
        self.crear_tarjeta_estudiante(contenedor)

    def crear_tarjeta_docente(self, parent):

        tarjeta = ctk.CTkFrame(
            parent,
            width=350,
            height=260,
            corner_radius=25,
            fg_color="#6D28D9"
        )

        tarjeta.pack(side="left", padx=25)
        tarjeta.pack_propagate(False)

        ctk.CTkLabel(
            tarjeta,
            text="DOCENTE",
            font=("Segoe UI", 28, "bold")
        ).pack(pady=(40, 10))

        ctk.CTkLabel(
            tarjeta,
            text="Gestione tareas, revisiones,\nhistorial y comunicación",
            font=("Segoe UI", 14)
        ).pack()

        ctk.CTkButton(
            tarjeta,
            text="Acceder",
            width=180,
            height=40,
            command=self.abrir_docente
        ).pack(pady=35)

    def crear_tarjeta_estudiante(self, parent):

        tarjeta = ctk.CTkFrame(
            parent,
            width=350,
            height=260,
            corner_radius=25,
            fg_color="#2563EB"
        )

        tarjeta.pack(side="left", padx=25)
        tarjeta.pack_propagate(False)

        ctk.CTkLabel(
            tarjeta,
            text="ESTUDIANTE",
            font=("Segoe UI", 28, "bold")
        ).pack(pady=(40, 10))

        ctk.CTkLabel(
            tarjeta,
            text="Consulte tareas, revisiones,\nhistorial y comunicación",
            font=("Segoe UI", 14)
        ).pack()

        ctk.CTkButton(
            tarjeta,
            text="Acceder",
            width=180,
            height=40,
            command=self.abrir_estudiante
        ).pack(pady=35)

    def abrir_docente(self):

        self.withdraw()

        DashboardDocente(self)

    def abrir_estudiante(self):

        self.withdraw()

        ListaEstudiantes(self)