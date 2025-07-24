# 📝 Blog con Django

Un blog moderno y elegante construido con Django y Tailwind CSS, que permite a los usuarios crear, editar y gestionar artículos con una interfaz intuitiva y responsive.

## ✨ Características

- **🎨 Diseño Moderno**: Interfaz elegante con Tailwind CSS
- **👤 Sistema de Usuarios**: Autenticación y gestión de usuarios
- **📝 CRUD Completo**: Crear, leer, actualizar y eliminar artículos
- **📱 Responsive**: Diseño adaptativo para todos los dispositivos
- **🔄 Estados de Artículos**: Borradores y artículos publicados
- **🔗 URLs Amigables**: Slugs únicos para SEO
- **📄 Paginación**: Navegación eficiente entre artículos
- **⚡ Performance**: Optimizado para velocidad

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.2
- **Frontend**: Tailwind CSS
- **Base de Datos**: SQLite
- **Iconos**: Font Awesome
- **Lenguaje**: Python 3.13

## 🚀 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd blog_basico
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor**
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - Blog: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 📁 Estructura del Proyecto

```
blog_basico/
├── blog/                    # Aplicación principal
│   ├── templates/          # Templates HTML
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Vistas de la aplicación
│   ├── urls.py            # Configuración de URLs
│   └── admin.py           # Configuración del admin
├── blog_basico/           # Configuración del proyecto
│   ├── settings.py        # Configuraciones
│   ├── urls.py            # URLs principales
│   └── wsgi.py            # Configuración WSGI
├── manage.py              # Script de gestión Django
├── requirements.txt       # Dependencias del proyecto
└── README.md             # Este archivo
```

## 🎯 Funcionalidades

### Para Usuarios Autenticados
- ✅ Crear nuevos artículos
- ✅ Editar artículos propios
- ✅ Eliminar artículos propios
- ✅ Gestionar estados (borrador/publicado)
- ✅ Acceso al panel de administración

### Para Visitantes
- ✅ Ver artículos publicados
- ✅ Navegar por el blog
- ✅ Ver información de autores y fechas

## 🎨 Diseño

El proyecto utiliza **Tailwind CSS** para un diseño moderno y responsive:

- **Colores**: Paleta azul moderna con grises
- **Tipografía**: Fuentes legibles y jerarquía clara
- **Componentes**: Cards, botones y formularios estilizados
- **Iconos**: Font Awesome para mejor UX
- **Responsive**: Adaptable a móviles, tablets y desktop

## 🔧 Configuración

### Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
DEBUG=True
SECRET_KEY=tu-clave-secreta-aqui
DATABASE_URL=sqlite:///db.sqlite3
```

### Configuración de Base de Datos

El proyecto viene configurado con SQLite por defecto. Para usar PostgreSQL o MySQL, modifica `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_db',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🚀 Despliegue

### Heroku

1. Crear archivo `Procfile`:
   ```
   web: gunicorn blog_basico.wsgi
   ```

2. Instalar gunicorn:
   ```bash
   pip install gunicorn
   ```

3. Configurar variables de entorno en Heroku

### VPS/DigitalOcean

1. Configurar servidor web (Nginx)
2. Configurar WSGI (Gunicorn)
3. Configurar SSL con Let's Encrypt

## 🤝 Contribuir

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Tu Nombre**
- LinkedIn: [Tu LinkedIn]
- GitHub: [Tu GitHub]
- Email: tu.email@ejemplo.com

## 🙏 Agradecimientos

- Django Documentation
- Tailwind CSS
- Font Awesome
- Comunidad de Python/Django

---

⭐ Si te gusta este proyecto, ¡dale una estrella en GitHub! 