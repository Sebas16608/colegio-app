# 🧩 Microservicios — Colegio APP

Esta carpeta contiene los **microservicios** del backend modular de Colegio APP, implementados en **TypeScript** para separar responsabilidades y mejorar escalabilidad.

Actualmente hay tres servicios:

* 💬 **Chat**
* 📂 **Files**
* 🔔 **Notifications**

---

## ⚙️ Propósito de los servicios

* **Chat:** Permite conversaciones entre estudiante → maestro y maestro → estudiante.
* **Files:** Gestiona la subida de archivos de cualquier tipo por parte de los estudiantes.
* **Notifications:** Servicio de notificaciones para alertar sobre nuevas tareas o archivos subidos. Funciona de manera similar a Google Classroom y se implementará progresivamente.

> Cada microservicio está diseñado para ser independiente, con **sus propios modelos, endpoints y lógica de negocio**, lo que permite **no sobrecargar el backend principal** y facilitar escalabilidad futura.

---

## 💻 Tecnologías y versiones

* **TypeScript:** 5.9.3
* **Node.js:** v25.3.0
* **npm:** 11.7.0

> Cada microservicio todavía no tiene librerías adicionales instaladas, se instalarán según sus necesidades.

---

## 📂 Estructura de la carpeta `services`

```bash
services/
├── chat/
├── files/
└── notifications/
```

Cada microservicio tendrá su propio **package.json, tsconfig.json y rutas** cuando se empiece a implementar la lógica.

---

## 🔮 Mejoras y próximos pasos

* Instalación y configuración de dependencias para cada servicio
* Integración de base de datos si es necesaria
* Implementación de endpoints y lógica interna
* Pruebas unitarias y documentación
* Comunicación entre microservicios y backend principal

---

## ✅ Conclusión

Estos microservicios permiten:

* Separar funcionalidades críticas del backend principal
* Facilitar mantenimiento y escalabilidad
* Implementar servicios independientes para Chat, Files y Notifications
