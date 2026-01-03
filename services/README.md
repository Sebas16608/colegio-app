# Services – Colegio App ⚙️

Este directorio contiene los **microservicios** del sistema Colegio App.
Cada servicio está pensado para resolver una tarea específica y mantenerse
independiente del backend principal.

El backend en Django sigue siendo la **fuente de verdad**.
Estos servicios consumen su API y confían en él para autenticación y usuarios.

---

## 🧠 ¿Por qué microservicios?

- Separar responsabilidades
- Evitar sobrecargar Django con tareas específicas
- Poder escalar o cambiar servicios sin romper todo
- Practicar arquitectura real

No todos los servicios son críticos para que el sistema funcione.

---

## 🧱 Estructura general

```bash
services/
├── chat/
├── files/
└── notifications/ (futuro)
```

Cada servicio tiene:
- su propio `package.json`
- sus dependencias
- su lógica aislada

---

## 💬 Chat Service

Servicio para mensajería básica entre alumnos y docentes.

Responsabilidades:
- Enviar mensajes
- Recibir mensajes
- Marcar mensajes como leídos

Modelo lógico:
- sender_id (User.id)
- receiver_id (User.id)
- content
- created_at
- read

Notas:
- No maneja usuarios
- Solo usa los IDs que vienen del backend Django

---

## 📎 Files Service

Servicio para manejo de archivos.

Responsabilidades:
- Subir archivos
- Validar tipo y tamaño
- Guardar rutas
- Devolver URLs

Modelo lógico:
- owner_id (User.id)
- type (assignment / profile / other)
- file_path
- size
- uploaded_at

Notas:
- No guarda archivos en Django
- Django solo almacena la referencia (URL)

---

## 🔔 Notifications Service (futuro)

Servicio para notificaciones del sistema.

Posibles funciones:
- Notificar tareas nuevas
- Avisar cuando una tarea fue calificada
- Enviar correos o notificaciones push

Este servicio no es prioritario en la primera versión.

---

## 🔐 Autenticación

- Los servicios no autentican usuarios por sí mismos
- Validan tokens emitidos por el backend Django
- Django sigue siendo la autoridad del sistema

---

## 🚧 Estado del proyecto

🚧 En desarrollo  
Los servicios pueden cambiar, dividirse o eliminarse conforme el sistema
crezca y se use en un entorno real.

---

## 🎯 Objetivo

Mantener servicios simples, claros y desacoplados,
sin sobreingeniería innecesaria y con enfoque práctico.
