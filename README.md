# Django Library Project

Este es un proyecto de ejemplo para gestionar una librería con Django y Django REST Framework.

## Requisitos

- Python 3.8+
- Django 5.2
- Django REST Framework

## Instrucciones

### 1. Clonar el repositorio

```bash
git clone https://github.com/Vania-0731/djangoApp05.git
cd https://github.com/Vania-0731/djangoApp05.git
```
2. Crear y activar el entorno virtual
```bash
python -m venv venv

# En Windows
.\venv\Scripts\activate
# En Linux/Mac
source venv/bin/activate
```
3. Instalar dependencias
```bash
pip install -r requirements.txt
```
4. Configurar la base de datos
Asegúrate de configurar la base de datos en settings.py. Si usas SQLite, no es necesario hacer nada extra.

5. Aplicar migraciones
```bash
python manage.py migrate
```
6. Crear un superusuario (opcional)
```bash
python manage.py createsuperuser
```
7. Levantar el servidor
```bash
python manage.py runserver
```
Accede a la API en http://localhost:8000/api/ y a las vistas basadas en templates en http://localhost:8000/library/.

URLs disponibles
API:

/api/categories/

/api/authors/

/api/books/


/library/categories/

/library/authors/

etc.
