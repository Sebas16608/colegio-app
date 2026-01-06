# Backend – Colegio App 🏫

Backend principal del sistema escolar **Colegio App**.  
Este servicio está construido con **Django** y maneja toda la lógica central del sistema: usuarios, materias, tareas, entregas, notas, pagos y calendario de eventos.

La idea es mantener este backend como **el core del sistema**, mientras otros servicios (chat, notificaciones, microservicios) se conectan a él.

---

## 🧠 Rol del backend

Este backend se encarga de:

- Autenticación y roles (alumno, docente, admin)  
- Gestión de usuarios  
- Materias y asignaciones  
- Tareas y entregas  
- Registro de notas  
- Registro y validación de pagos por depósito bancario  
- Gestión de eventos y calendario escolar  
- Exponer API para frontend y microservicios  

> Django es la **fuente de verdad del sistema**.

---

## 🛠 Tecnologías

- Python  
- Django  
- Django REST Framework  
- SQLite (por ahora)  

---

## 🗂 Apps principales

| App | Función |
|-----|--------|
| `user` | Gestión de usuarios y roles (STUDENT, TEACHER, ADMIN) |
| `subject` | Materias impartidas por docentes |
| `enrollment` | Relación alumno → materias |
| `assignment` | Tareas asignadas a materias |
| `submission` | Entregas de tareas por parte de los alumnos |
| `grade` | Notas asignadas a entregas |
| `payments` | Registro y validación de pagos por depósito bancario |
| `events` | Calendario de eventos y actividades escolares |

---

## 🗃️ Modelos principales

### 👤 User
Usuarios del sistema.

**Campos principales:**
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

**Campos principales:**
- id (PK)  
- name  
- teacher_id (FK → User)  
- created_at  

**Relación:**  
- Un docente puede tener muchas materias.

---

### 📚 Enrollment
Relación entre alumnos y materias.

**Campos principales:**
- id (PK)  
- student_id (FK → User)  
- subject_id (FK → Subject)  
- created_at  

---

### 📝 Assignment (Tarea)
Tareas asignadas a una materia.

**Campos principales:**
- id (PK)  
- subject_id (FK → Subject)  
- title  
- description  
- due_date  
- created_at  

---

### 📤 Submission (Entrega)
Entregas de tareas por parte de los alumnos.

**Campos principales:**
- id (PK)  
- assignment_id (FK → Assignment)  
- student_id (FK → User)  
- file_url  
- submitted_at  

**Restricción:**  
- Un alumno solo puede entregar una vez por tarea.

---

### 📊 Grade (Nota)
Nota asignada a una entrega.

**Campos principales:**
- id (PK)  
- submission_id (FK → Submission)  
- grade (0–100)  
- feedback  
- graded_at  

---

### 💸 Payments (Pagos)
Registro de pagos por depósito bancario.

**Campos principales:**
- id (PK)  
- student (FK → User)  
- amount  
- month (ej: "2026-01")  
- reference_number  
- receipt (archivo / comprobante)  
- status (PENDING / APPROVED / REJECTED)  
- created_at  
- validated_by (FK → User)  

**Notas:**
- Solo admins/secretaría validan pagos  
- Los alumnos pueden subir comprobantes y ver sus pagos  

---

### 📅 Events (Calendario)
Eventos escolares, reuniones, exámenes y actividades.

**Campos principales:**
- id (PK)  
- title  
- description  
- start_date  
- end_date  
- created_by (FK → User)  
- target_role (ALL / TEACHERS / STUDENTS)  
- subject (FK opcional)  

---

### 🔐 Autenticación
- Se maneja en Django  
- Los tokens se generan aquí  
- Otros servicios confían en este backend para validar usuarios  

---

## 🚧 Estado del proyecto
- En desarrollo  
- La estructura y los modelos pueden cambiar conforme el proyecto crezca y se pruebe en un entorno real.  

---

## 🎯 Objetivo
Construir un backend **claro, mantenible y realista** para un sistema escolar, con posibilidad de **escalar** y conectar microservicios más adelante.
