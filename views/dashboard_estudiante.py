import customtkinter as ctk


class DashboardEstudiante(ctk.CTkToplevel):

    def __init__(self, selector, estudiante):

        super().__init__()

        self.selector = selector
        self.estudiante = estudiante

        self.title("Dashboard Estudiante")
        self.geometry("1300x750")

        self.configure(fg_color="#0B1026")

        self.protocol(
            "WM_DELETE_WINDOW",
            self.volver
        )

        self.crear_interfaz()

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
            text="👨‍🎓 Estudiante",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=30)

        ctk.CTkButton(
            menu,
            text="← Volver",
            command=self.volver
        ).pack(pady=10)

        opciones = [
            "📤 Entrega de Tareas",
            "📋 Estado de Revisiones",
            "💬 Comentarios Recibidos",
            "📨 Comunicación Académica",
            "🔔 Notificaciones",
            "📚 Historial Académico"
        ]

        for opcion in opciones:

            ctk.CTkButton(
                menu,
                text=opcion,
                width=180
            ).pack(pady=8)

        # ===== CONTENIDO PRINCIPAL =====

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
            text=f"Bienvenido {self.estudiante['nombre']}",
            font=("Segoe UI", 30, "bold")
        ).pack(anchor="w", pady=(10, 5))

        ctk.CTkLabel(
            contenido,
            text=f"Código: {self.estudiante['codigo']}",
            font=("Segoe UI", 16)
        ).pack(anchor="w")

        # ===== VALIDACIÓN DE MATERIAS =====

        materias = self.estudiante.get("materias", [])

        if len(materias) > 0:

            mensaje = (
                f"✅ Habilitado en {len(materias)} materia(s)"
            )

        else:

            mensaje = (
                "❌ No se encuentra habilitado en ninguna materia"
            )

        ctk.CTkLabel(
            contenido,
            text=mensaje,
            font=("Segoe UI", 16, "bold")
        ).pack(anchor="w", pady=(10, 20))

        # ===== TARJETAS =====

        fila = ctk.CTkFrame(
            contenido,
            fg_color="transparent"
        )

        fila.pack(fill="x")

        datos = [
            ("Tareas", "0", "#7C3AED"),
            ("Revisiones", "0", "#2563EB"),
            ("Mensajes", "0", "#059669"),
            ("Notificaciones", "0", "#D97706")
        ]

        for titulo, valor, color in datos:

            tarjeta = ctk.CTkFrame(
                fila,
                width=220,
                height=120,
                fg_color=color,
                corner_radius=20
            )

            tarjeta.pack(side="left", padx=10)

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