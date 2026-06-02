import customtkinter as ctk
import json
import os
from datetime import datetime


class TareasAcademicas(ctk.CTkToplevel):

    def __init__(self):

        super().__init__()

        self.title("Tareas Académicas")
        self.geometry("1100x700")

        self.configure(
            fg_color="#0B1026"
        )

        self.lift()
        self.focus_force()

        self.attributes(
            "-topmost",
            True
        )

        self.after(
            100,
            lambda: self.attributes(
                "-topmost",
                False
            )
        )

        self.crear_interfaz()

        self.cargar_tareas()

    def crear_interfaz(self):

        ctk.CTkLabel(
            self,
            text="📝 Gestión de Tareas Académicas",
            font=("Segoe UI", 30, "bold"),
            text_color="white"
        ).pack(
            pady=(20, 10)
        )

        principal = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        principal.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        formulario = ctk.CTkFrame(
            principal,
            fg_color="#111827",
            corner_radius=20
        )

        formulario.pack(
            fill="x",
            pady=10
        )

        ctk.CTkLabel(
            formulario,
            text="Nueva Tarea",
            font=("Segoe UI", 22, "bold")
        ).pack(
            pady=(15, 10)
        )

        self.titulo_entry = ctk.CTkEntry(
            formulario,
            width=500,
            height=40,
            placeholder_text="Título de la tarea",
            fg_color="#1F2937",
            border_color="#2563EB"
        )

        self.titulo_entry.pack(pady=8)

        self.descripcion_entry = ctk.CTkEntry(
            formulario,
            width=500,
            height=40,
            placeholder_text="Descripción",
            fg_color="#1F2937",
            border_color="#2563EB"
        )

        self.descripcion_entry.pack(pady=8)

        self.fecha_entry = ctk.CTkEntry(
            formulario,
            width=500,
            height=40,
            placeholder_text="Fecha Entrega (AAAA-MM-DD)",
            fg_color="#1F2937",
            border_color="#2563EB"
        )

        self.fecha_entry.pack(pady=8)

        self.tipo_entry = ctk.CTkEntry(
            formulario,
            width=500,
            height=40,
            placeholder_text="Tipo Archivo Permitido (PDF, DOCX, ZIP...)",
            fg_color="#1F2937",
            border_color="#2563EB"
        )

        self.tipo_entry.pack(pady=8)

        self.mensaje = ctk.CTkLabel(
            formulario,
            text="",
            text_color="green"
        )

        self.mensaje.pack()

        ctk.CTkButton(
            formulario,
            text="Crear Tarea",
            width=220,
            height=40,
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            command=self.crear_tarea
        ).pack(
            pady=(15, 20)
        )

        tabla = ctk.CTkFrame(
            principal,
            fg_color="#111827",
            corner_radius=20
        )

        tabla.pack(
            fill="both",
            expand=True,
            pady=15
        )

        ctk.CTkLabel(
            tabla,
            text="📋 Tareas Registradas",
            font=("Segoe UI", 22, "bold")
        ).pack(
            pady=15
        )

        encabezados = ctk.CTkFrame(
            tabla,
            fg_color="#1F2937"
        )

        encabezados.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            encabezados,
            text="Título",
            width=250
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkLabel(
            encabezados,
            text="Fecha",
            width=150
        ).pack(
            side="left"
        )

        ctk.CTkLabel(
            encabezados,
            text="Estado",
            width=150
        ).pack(
            side="left"
        )

        ctk.CTkLabel(
            encabezados,
            text="Archivo",
            width=150
        ).pack(
            side="left"
        )

        self.lista_tareas = ctk.CTkScrollableFrame(
            tabla,
            fg_color="#111827"
        )

        self.lista_tareas.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

    def crear_tarea(self):

        titulo = self.titulo_entry.get().strip()
        descripcion = self.descripcion_entry.get().strip()
        fecha = self.fecha_entry.get().strip()
        tipo = self.tipo_entry.get().strip()

        if not titulo or not descripcion or not fecha or not tipo:

            self.mensaje.configure(
                text="Todos los campos son obligatorios",
                text_color="red"
            )

            return

        try:

            datetime.strptime(
                fecha,
                "%Y-%m-%d"
            )

        except ValueError:

            self.mensaje.configure(
                text="Fecha inválida. Use AAAA-MM-DD",
                text_color="red"
            )

            return

        tareas = self.leer_tareas()

        nuevo_id = len(tareas) + 1

        tarea = {
            "idTarea": nuevo_id,
            "titulo": titulo,
            "descripcion": descripcion,
            "fechaEntrega": fecha,
            "estado": "Pendiente",
            "tipoArchivoPermitido": tipo
        }

        tareas.append(tarea)

        with open(
            "data/tareas.json",
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                tareas,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        self.mensaje.configure(
            text="Tarea creada correctamente",
            text_color="green"
        )

        self.titulo_entry.delete(0, "end")
        self.descripcion_entry.delete(0, "end")
        self.fecha_entry.delete(0, "end")
        self.tipo_entry.delete(0, "end")

        self.cargar_tareas()

    def leer_tareas(self):

        if not os.path.exists(
            "data/tareas.json"
        ):

            return []

        try:

            with open(
                "data/tareas.json",
                "r",
                encoding="utf-8"
            ) as archivo:

                return json.load(archivo)

        except:

            return []

    def cargar_tareas(self):
        print("CARGANDO TAREAS...")
        print(self.leer_tareas())

        for widget in self.lista_tareas.winfo_children():

            widget.destroy()

        tareas = self.leer_tareas()

        if not tareas:

            ctk.CTkLabel(
                self.lista_tareas,
                text="No existen tareas registradas"
            ).pack(
                pady=10
            )

            return

        for tarea in tareas:

            fila = ctk.CTkFrame(
                self.lista_tareas,
                fg_color="#1F2937"
            )

            fila.pack(
                fill="x",
                pady=5
            )

            ctk.CTkLabel(
                fila,
                text=tarea["titulo"],
                width=250
            ).pack(
                side="left",
                padx=10
            )

            ctk.CTkLabel(
                fila,
                text=tarea["fechaEntrega"],
                width=150
            ).pack(
                side="left"
            )

            ctk.CTkLabel(
                fila,
                text=tarea["estado"],
                width=150
            ).pack(
                side="left"
            )

            ctk.CTkLabel(
                fila,
                text=tarea["tipoArchivoPermitido"],
                width=150
            ).pack(
                side="left"
            )