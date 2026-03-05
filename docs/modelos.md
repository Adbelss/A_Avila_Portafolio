# Modelos y Relaciones (Semana 2)

Este documento describe los modelos principales del portafolio, sus relaciones, campos clave y consideraciones de ORM (constraints/índices/managers).

---

## Apps y responsabilidades

- `apps/projects`: Proyectos, tecnologías y galería (CMS de portafolio).
- `apps/services`: Catálogo de servicios ofrecidos.
- `apps/contact`: Captura de leads desde el formulario de contacto.

---

## 1) Projects

### 1.1 Project
**Propósito:** Representa un caso/proyecto del portafolio (tipo “case study”).

**Campos principales:**
- `title`: título del proyecto.
- `slug`: slug único para URLs.
- `summary`: resumen corto.
- `problem`, `solution`, `responsibilities`: contenido del caso.
- `stack_summary`: stack resumido.
- `status`: `draft` | `published` (filtro principal).
- `start_date`, `end_date`: fechas (opcional).
- `is_featured`: destacado para home.
- `order`: orden editorial.
- `github_url`, `demo_url`: enlaces.

**Relaciones:**
- ManyToMany con `Technology` (`technologies`).
- OneToMany con `ProjectImage` (`images`).

**ORM profesional:**
- Constraint: slug único.
- Índices: combinaciones para filtros/orden (`status`, `is_featured`, `order`, `created_at`).
- Manager/QuerySet:
  - `published()`
  - `featured()`
  - `with_related()` (prefetch de technologies/images para evitar N+1)

---

### 1.2 ProjectImage
**Propósito:** Galería ordenada por proyecto.

**Campos:**
- `project` (FK)
- `image`
- `alt_text`
- `order`

**ORM:**
- Índice por `project, order` para ordenar eficientemente en la galería.

---

### 1.3 Technology
**Propósito:** Tecnologías asociables a proyectos.

**Campos:**
- `name`
- `slug` (único)
- `category` (backend/frontend/db/devops/other)
- `icon` (opcional)
- `order`

**ORM:**
- Constraint: slug único.
- Índices por `category, order` para filtros y ordenamiento.
- Manager/QuerySet:
  - `ordered()`

---

## 2) Services

### 2.1 Service
**Propósito:** Servicios ofrecidos (enfocado a conversión/venta).

**Campos:**
- `name`
- `slug` (único)
- `description`
- `deliverables` (opcional)
- `price_hint` (opcional)
- `order`
- `is_active`
- `created_at`

**ORM:**
- Constraint: slug único.
- Índice por `is_active, order` para listar servicios activos eficientemente.
- Manager/QuerySet:
  - `active()`

---

## 3) Contact

### 3.1 Lead
**Propósito:** Persistencia de solicitudes enviadas desde el formulario (captación real).

**Campos:**
- `name`
- `email`
- `phone` (opcional)
- `message`
- `source` (por ejemplo `web`)
- `created_at`
- `is_read`
- `notes` (seguimiento interno)

**ORM:**
- Índices por `created_at`, `is_read`, `source` para manejo tipo bandeja (CRM básico).

---

## Criterios de calidad (DoD Semana 2)

- Admin permite crear/editar:
  - Proyectos, tecnologías, servicios, leads.
- Se pueden:
  - asociar tecnologías a proyectos,
  - subir y ordenar imágenes en un proyecto (inline),
  - filtrar y buscar en admin.
- Modelos con:
  - constraints e índices,
  - managers/querysets base para evitar N+1.
