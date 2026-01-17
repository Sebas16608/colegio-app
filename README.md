# 🏫 Colegio APP

**Backend modular para una aplicación escolar**, organizado por roles: estudiante, maestro y admin.  
Incluye **microservicios** en TypeScript para mejorar escalabilidad y separar responsabilidades: Chat, Files y Notifications.

---

## 🛠️ Motivación

El proyecto nace de una **experiencia real** mientras **trabajo como maestro sustituto de computación**.  
Quería crear una app para:

- 📊 Llevar un registro completo de los datos de los estudiantes
- 💾 Evitar perder información importante
- 🏫 Gestionar roles de **estudiante, maestro y admin** de manera organizada
- ⚡ Mantener el backend principal liviano usando **microservicios** para funciones específicas


---

## ⚙️ Estructura del proyecto
El backend se organizó de manera **modular**:

- Cada app y microservicio tiene:
  - Modelos propios
  - Serializadores y validaciones
  - Vistas / APIs
  - Endpoints registrados en las rutas principales
- Esto permite agregar funcionalidades nuevas sin afectar el resto del sistema.

---

## 🧩 Microservicios en TypeScript

### 💬 Chat
- Servicio para conversaciones **estudiante → maestro** y **maestro → estudiante**.
- No implementa real-time por simplicidad y necesidad del proyecto.

### 📂 Files
- Servicio para que los estudiantes puedan **subir archivos** de cualquier tipo.
- Separado para **no sobrecargar el backend principal**.

### 🔔 Notifications
- Servicio para notificar a estudiantes y maestros sobre nuevos archivos o tareas subidas.
- Funcionamiento similar a Google Classroom.
- Se implementará **progresivamente**.

---

## 💻 Tecnologías

**Backend principal (Python/Django):**

```python
Python 3.14.2
Django 6.0
Django REST Framework 3.16.1
```
*Librerías instaladas:*
```bash
asgiref==3.11.0
attrs==25.4.0
Django==6.0
django-jazzmin==3.0.1
djangorestframework==3.16.1
drf-spectacular==0.29.0
inflection==0.5.1
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
PyYAML==6.0.3
referencing==0.37.0
rpds-py==0.30.0
sqlparse==0.5.5
uritemplate==4.2.0
```
*Microservicios TS/Node (en preparación):*
```typescript
TypeScript: 5.9.3
Node.js: v25.3.0
npm: 11.7.0
```
## 🔮 Mejoras futuras
- Implementación completa de Notifications
- Integración real-time para Chat
- Autenticación centralizada entre microservicios
- Optimización de almacenamiento de archivos
- Documentación con Swagger / OpenAPI para todos los servicios

## ✅ Conclusión
- Este proyecto demuestra:
- Diseño modular y escalable
- Separación de responsabilidades con microservicios
- Stack moderno con Python, Django y TypeScript
- Preparación para futuro crecimiento (más servicios, nuevas funcionalidades)