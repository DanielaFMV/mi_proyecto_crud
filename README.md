# Sistema de Gestión de Clientes — CRUD con Django

Aplicación web para crear, listar, editar y eliminar clientes. Desarrollada con Django como parte del Módulo 7 del bootcamp de Python.

## Tecnologías

- Python 3
- Django 6
- SQLite
- Bootstrap 5

## Instalación y ejecución

```bash
# 1. Clonar el repositorio
git clone https://github.com/DanielaFMV/mi_proyecto_crud.git
cd mi_proyecto_crud

# 2. Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install django

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear superusuario (para el panel admin)
python manage.py createsuperuser

# 6. Iniciar el servidor
python manage.py runserver
```

## URLs disponibles

| URL | Descripción |
|-----|-------------|
| `/clientes/` | Lista de clientes |
| `/clientes/nuevo/` | Crear cliente |
| `/clientes/<id>/` | Detalle de cliente |
| `/clientes/editar/<id>/` | Editar cliente |
| `/clientes/eliminar/<id>/` | Eliminar cliente |
| `/admin/` | Panel de administración |
