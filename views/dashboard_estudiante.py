import customtkinter as ctk


class DashboardEstudiante(ctk.CTkToplevel):

    def __init__(self, selector):

        super().__init__()

        self.selector = selector

        self.title("Dashboard Estudiante")
        self.geometry("1300x750")

        self.configure(fg_color="#0B1026")

        self.protocol(
            "WM_DELETE_WINDOW",
            self.volver
        )

        self.crear_interfaz()

    def crear_interfaz(self):

        menu = ctk.CTkFrame(
            self,
            width=220,
            fg_color="#111827",
            corner_radius=0
        )

        menu.pack(side="left", fill="y")

        ctk.CTkLabel(
            menu,
            text="👨‍🎓 Estudiante",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=30)

        ctk.CTkButton(
            menu,
            text="← Volver",
            command=self.volver
        ).pack(pady=10)

        opciones = [
            "Tareas",
            "Estado de Revisiones",
            "Comentarios Recibidos",
            "Comunicación Académica",
            "Notificaciones",
            "Historial Académico",
            
        ]

        for opcion in opciones:

            ctk.CTkButton(
                menu,
                text=opcion,
                width=180
            ).pack(pady=8)

        contenido = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        contenido.pack(fill="both", expand=True)

        ctk.CTkLabel(
            contenido,
            text="Dashboard Estudiante",
            font=("Segoe UI", 30, "bold")
        ).pack(pady=30)

    def volver(self):

        self.destroy()

        self.selector.deiconify()