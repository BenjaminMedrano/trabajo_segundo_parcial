import json
import customtkinter as ctk

from views.tareas_academicas import TareasAcademicas


class DashboardDocente(ctk.CTkToplevel):

    def __init__(self, selector):

        super().__init__()

        self.selector = selector

        self.docente = self.cargar_docente()

        self.title("Dashboard Docente")
        self.geometry("1300x750")

        self.configure(fg_color="#0B1026")

        self.protocol(
            "WM_DELETE_WINDOW",
            self.volver
        )

        self.crear_interfaz()

    def cargar_docente(self):

        try:

            with open(
                "data/docentes.json",
                "r",
                encoding="utf-8"
            ) as archivo:

                docentes = json.load(archivo)

            return docentes[0]

        except:

            return {
                "nombre": "Docente",
                "materias": []
            }

    def abrir_tareas(self):

        TareasAcademicas()

    def crear_interfaz(self):

        # ===== MENÚ LATERAL =====

        menu = ctk.CTkFrame(
            self,
            width=220,
            fg_color="#111827",
            corner_radius=0
        )

        menu.pack(side="left", fill="y")

        ctk.CTkLabel(
            menu,
            text="👨‍🏫 Docente",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=30)

        ctk.CTkButton(
            menu,
            text="← Volver",
            command=self.volver
        ).pack(pady=10)

        opciones = [
            "📝 Tareas Académicas",
            "📋 Revisiones",
            "💬 Comentarios",
            "📨 Comunicación",
            "📊 Reportes Académicos",
            "📚 Historial de Cambios"
        ]

        for opcion in opciones:

            if opcion == "📝 Tareas Académicas":

                ctk.CTkButton(
                    menu,
                    text=opcion,
                    width=180,
                    command=self.abrir_tareas
                ).pack(pady=8)

            else:

                ctk.CTkButton(
                    menu,
                    text=opcion,
                    width=180
                ).pack(pady=8)

        # ===== CONTENIDO =====

        contenido = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        contenido.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        ctk.CTkLabel(
            contenido,
            text=f"Bienvenido {self.docente['nombre']}",
            font=("Segoe UI", 30, "bold")
        ).pack(anchor="w", pady=(10, 5))

        materia_nombre = "Sin materia asignada"
        cantidad_estudiantes = 0

        try:

            with open(
                "data/materias.json",
                "r",
                encoding="utf-8"
            ) as archivo:

                materias = json.load(archivo)

            if self.docente["materias"]:

                materia_id = self.docente["materias"][0]

                for materia in materias:

                    if materia["idMateria"] == materia_id:

                        materia_nombre = (
                            f"{materia['sigla']} - "
                            f"{materia['nombre']}"
                        )

                        cantidad_estudiantes = len(
                            materia["estudiantes"]
                        )

                        break

        except:

            pass

        ctk.CTkLabel(
            contenido,
            text=f"Materia: {materia_nombre}",
            font=("Segoe UI", 18)
        ).pack(anchor="w")

        ctk.CTkLabel(
            contenido,
            text=f"Estudiantes inscritos: {cantidad_estudiantes}",
            font=("Segoe UI", 18)
        ).pack(anchor="w", pady=(0, 20))

        # ===== TARJETAS =====

        fila = ctk.CTkFrame(
            contenido,
            fg_color="transparent"
        )

        fila.pack(fill="x")

        try:

            with open(
                "data/tareas.json",
                "r",
                encoding="utf-8"
            ) as archivo:

             tareas = json.load(archivo)

            total_tareas = len(tareas)

        except:

           total_tareas = 0

        datos = [
        ("Tareas", str(total_tareas), "#7C3AED"),
        ("Revisiones", "0", "#2563EB"),
        ("Mensajes", "0", "#059669"),
        ("Reportes", "0", "#D97706")
        ]

        for titulo, valor, color in datos:

            tarjeta = ctk.CTkFrame(
                fila,
                width=220,
                height=120,
                fg_color=color,
                corner_radius=20
            )

            tarjeta.pack(
                side="left",
                padx=10
            )

            tarjeta.pack_propagate(False)

            ctk.CTkLabel(
                tarjeta,
                text=titulo,
                font=("Segoe UI", 18)
            ).pack(pady=(20, 5))

            ctk.CTkLabel(
                tarjeta,
                text=valor,
                font=("Segoe UI", 32, "bold")
            ).pack()

    def volver(self):

        self.destroy()

        self.selector.deiconify()