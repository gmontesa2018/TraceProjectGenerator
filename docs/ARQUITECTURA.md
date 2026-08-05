# Arquitectura del Proyecto

## Objetivo

Separar la lógica de negocio de la generación de proyectos.

---

# Componentes

## Configurador

Obtiene toda la información de la obra.

↓

## Builder

Construye automáticamente la estructura del proyecto.

↓

## Biblioteca Técnica

Define procedimientos reutilizables.

↓

## ClickUp

Genera tareas, subtareas y documentación.

---

# Estructura de una obra

Proyecto

├── Gestión

├── Comunicaciones

├── Sectores

│   ├── Torres

│   │   ├── Torre 01
│   │   ├── Torre 02
│   │   └── ...

│   └── Áreas Comunes

├── Accesibilidad

├── Seguridad Perimetral

├── Seguridad Interna

├── Puesta en Marcha

├── Capacitación

└── Entrega

---

# Biblioteca

Cada categoría dispone de su propia biblioteca.

- Infraestructura
- Comunicaciones
- Porteros
- Accesos
- CCTV
- Seguridad Perimetral
- Automatismos

El Builder solamente consume estas bibliotecas.