import json
import customtkinter as ctk

from views.dashboard_estudiante import DashboardEstudiante


class ListaEstudiantes(ctk.CTkToplevel):

    def __init__(self, selector):

        super().__init__()

        self.selector = selector

        self.title("Seleccionar Estudiante")
        self.geometry("900x650")

        self.configure(fg_color="#0B1026")

        self.protocol(
            "WM_DELETE_WINDOW",
            self.volver
        )

        self.crear_interfaz()

    def crear_interfaz(self):

        titulo = ctk.CTkLabel(
            self,
            text="Seleccionar Estudiante",
            font=("Segoe UI", 30, "bold")
        )

        titulo.pack(pady=20)

        contenedor = ctk.CTkScrollableFrame(
            self,
            width=750,
            height=450
        )

        contenedor.pack(pady=20)

        try:

            with open(
                "data/estudiantes.json",
                "r",
                encoding="utf-8"
            ) as archivo:

                estudiantes = json.load(archivo)

        except:

            estudiantes = []

        for estudiante in estudiantes:

            tarjeta = ctk.CTkFrame(
                contenedor,
                height=120
            )

            tarjeta.pack(
                fill="x",
                pady=10,
                padx=10
            )

            nombre = estudiante["nombre"]

            codigo = estudiante["codigo"]

            ctk.CTkLabel(
                tarjeta,
                text=nombre,
                font=("Segoe UI", 20, "bold")
            ).pack(pady=(10, 5))

            ctk.CTkLabel(
                tarjeta,
                text=f"Código: {codigo}"
            ).pack()

            ctk.CTkButton(
                tarjeta,
                text="Ingresar",
                command=lambda e=estudiante:
                self.ingresar_estudiante(e)
            ).pack(pady=10)

        ctk.CTkButton(
            self,
            text="← Volver",
            command=self.volver
        ).pack(pady=10)

    def ingresar_estudiante(self, estudiante):

        self.withdraw()

        DashboardEstudiante(
            self.selector,
            estudiante
        )

    def volver(self):

        self.destroy()

        self.selector.deiconify()