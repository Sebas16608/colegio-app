# Backend – Colegio App 🏫

Backend principal del sistema escolar **Colegio App**.  
Este servicio está construido con **Django** y es el encargado de toda la
lógica central del sistema: usuarios, materias, tareas y notas.

La idea es mantener este backend como el **core** del sistema y que otros
servicios se conecten a él.

---

## 🧠 Rol del backend

Este backend se encarga de:

- Autenticación y roles (alumno, docente, admin)
- Gestión de usuarios
- Materias y asignaciones
- Tareas y entregas
- Registro de notas
- Exponer una API para frontend y microservicios

👉 Django es la **fuente de verdad** del sistema.

---

## 🛠 Tecnologías

- Python
- Django
- Django REST Framework
- SQLite (por ahora)

---

## 🗃️ Modelos principales

### 👤 User
Usuarios del sistema.

Campos principales:
- id (PK)
- username (único)
- email (único)
- password
- role (STUDENT / TEACHER / ADMIN)
- is_active
- created_at

---

### 🏫 Subject (Materia)
Materias impartidas por un docente.

Campos:
- id (PK)
- name
- teacher_id (FK → User)
- created_at

Relación:
- Un docente puede tener muchas materias.

---

### 📚 Enrollment
Relación entre alumnos y materias.

Campos:
- id (PK)
- student_id (FK → User)
- subject_id (FK → Subject)
- created_at

Notas:
- Un alumno puede estar en varias materias.
- Una materia tiene varios alumnos.

---

### 📝 Assignment (Tarea)
Tareas asignadas a una materia.

Campos:
- id (PK)
- subject_id (FK → Subject)
- title
- description
- due_date
- created_at

---

### 📤 Submission (Entrega)
Entregas de tareas por parte de los alumnos.

Campos:
- id (PK)
- assignment_id (FK → Assignment)
- student_id (FK → User)
- file_url (archivo almacenado en otro servicio)
- submitted_at

Restricción:
- Un alumno solo puede entregar una vez por tarea.

---

### 📊 Grade (Nota)
Nota asignada a una entrega.

Campos:
- id (PK)
- submission_id (FK → Submission)
- grade (0–100)
- feedback
- graded_at

Relación:
- Una entrega tiene una sola nota.

---

## 🔐 Autenticación

- La autenticación se maneja en Django
- Los tokens se generan aquí
- Otros servicios confían en este backend para validar usuarios

---

## 🚧 Estado del proyecto

🚧 En desarrollo  
La estructura y los modelos pueden cambiar conforme el proyecto crezca
y se pruebe en un entorno real.

---

## 🎯 Objetivo

Construir un backend claro, mantenible y realista para un sistema escolar,
sin sobreingeniería y con posibilidad de escalar más adelante.
