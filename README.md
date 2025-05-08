# task_manager_inlab

### Estructura del Proyecto
El proyecto `task_manager_inlab` está estructurado de la siguiente manera:

```bash
task_manager_inlab/
├── manage.py
├── task_manager_inlab/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── accounts/         ← app para autenticación
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── validators.py
│   ├── forms_factory.py
│   └── forms.py
├── projects/         ← app para proyectos
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── services.py
│   ├── forms_factory.py
│   └── forms.py
├── tasks/            ← app para tareas
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── services.py
│   ├── forms_factory.py
│   └── forms.py
├── templates/
│   ├── base.html
│   ├── accounts/
│   │   ├── login.html
│   │   └── register.html
│   ├── projects/
│   │   ├── project_confirm_delete.html
│   │   ├── project_form.html
│   │   └── project_list.html
│   └── tasks/
└── static/
    └── css, js, fonts, etc.
```

### Explicación breve de decisiones técnicas

1. Se decide utilizar APIView y TemplateHTMLRenderer, JSONRenderer para que se comporte la vista como API o que renderice html, mo se utiliza
ViewSet para que también se renderice html.
2. Se decide utilizar la librería django-widget-tweaks para personalizar de forma más flexible y limpia los formularios 
en las plantillas de Django, sin tener que modificar los formularios directamente en Python.
3. Se decide emplear JQuery en las plantillas de Django para mejorar la experiencia del usuario en el frontend 
sin necesidad de herramientas más pesadas como React o Vue. Además para la validación del lado del cliente (sin recargar la página).
Se validan formularios antes de enviarlos al servidor. Además se usa JQuery para interacción con el DOM
fácilmente:  Mostrar/ocultar elementos, cambiar clases, modificar contenido sin recargar.
4. Se decide crear archivos de validación empleando JQuery fuera de los plantillas de Django para mantener la lógica de validación 
separada de la lógica de presentación.
5. Se decide emplear Bootstrap para el diseño responsivo y moderno de la interfaz de usuario.
6. Se decide no utilizar serializadores por la sencilles de la lógica de negocio y la estructura de los modelos. 
Y además con las clases form se validan los formularios.
7. Se decide utilizar el sistema de autenticación de Django para gestionar el registro y la autenticación de usuarios,
8. Se decide utilizar el sistema de plantillas de Django para renderizar las vistas y separar la lógica de presentación de la lógica de negocio.
9. Se decide utilizar el sistema de URL de Django para gestionar las rutas y vistas del proyecto,
10. Se decide utilizar el sistema de archivos estáticos de Django para gestionar los archivos estáticos del proyecto (CSS, JS, imágenes, etc.).
11. Se decide utilizar el sistema de migraciones de Django para gestionar la base de datos y los cambios en los modelos.
12. Se decide utilizar el sistema de gestión de errores de Django para gestionar los errores y excepciones del proyecto.
13. Se decide utilizar el sistema de gestión de sesiones de Django para gestionar las sesiones de los usuarios.
14. Se decide utilizar el sistema de gestión de mensajes de Django para gestionar los mensajes de éxito y error del proyecto.
15. Se decide utilizar como base de datos el SQLite de Django para facilitar el desarrollo y las pruebas del proyecto ya que no es proyecto real y facilidad para el despliegue.
16. Utilizar librerías locales en el proyecto para evitar llamadas innecesarias a la red y mejorar el rendimiento.

### Patrones de diseños aplicados

1. **MVC (Modelo-Vista-Controlador)**: 
   - Separa la lógica de negocio (Modelos), la lógica de presentación (Vistas) y la lógica de control (Controladores).
   - Django sigue este patrón, donde los modelos representan la base de datos, las vistas manejan la lógica y los controladores son las funciones que responden a las solicitudes del usuario.

2. **Singleton**:
   - Se utiliza en la configuración de Django para asegurar que solo haya una instancia de la configuración del proyecto.
     - Esto es útil para evitar conflictos y garantizar que todas las partes del proyecto utilicen la misma configuración.
     
3. **Factory**: 
   - Se utiliza en la creación de formularios y vistas para generar instancias de objetos de manera flexible.
   - Permite crear diferentes tipos de formularios o vistas sin necesidad de conocer la clase exacta que se va a instanciar. 
   - Mejora la escalabilidad si necesitas lógica compleja para elegir el formulario. Facilita pruebas y reutilización.
   - Facilita pruebas y reutilización.
   
4. **DRY (Don't Repeat Yourself)**:
   - Se aplica en la estructura del proyecto y en la reutilización de código.
   - Se evita la duplicación de código al crear funciones y clases reutilizables, lo que facilita el mantenimiento y la escalabilidad del proyecto. 
   Uso de formularios (forms.Form, ModelForm), mixins, clases base para vistas, etc. Reutilización de componentes con includes en templates y widgets.

5. **Template Method**:
   - Se utiliza en la creación de vistas y formularios para definir un esqueleto de algoritmo en una clase base y permitir que las subclases implementen pasos específicos.
   - Permite personalizar el comportamiento de las vistas y formularios sin modificar la lógica general.
   - Facilita la reutilización de código y la extensión de funcionalidades.
   
6. Inyección de Dependencias:
   - Facilita la prueba y el mantenimiento del código al permitir cambiar fácilmente las dependencias sin modificar el código existente. Hace tu código más mantenible y extensible.

7. Capa de Servicio (Service Layer Pattern)
   - Se utiliza para encapsular la lógica de negocio y las operaciones relacionadas con los modelos.
   - Permite separar la lógica de negocio de las vistas y los controladores, lo que facilita el mantenimiento y la reutilización del código.
   - Mejora la legibilidad y la organización del proyecto al agrupar la lógica relacionada en una sola clase.

8. Patrón de Decorador
  - Se utiliza para agregar funcionalidad adicional para crear la tarea asíncron con @django_rq.job.

### Instalación y Ejecución local
1. Clona el repositorio:
   ```bash
   git clone
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd task_manager
    ```
3. Crea un entorno virtual:
    ```bash
    python -m venv env
    ```
4. Activa el entorno virtual:
5. Para Windows:
    ```bash
    env\Scripts\activate
    ```
   Para Linux/Mac:
    ```bash
    source env/bin/activate
    ```
6. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
7. Realiza las migraciones:
    ```bash
      python manage.py migrate
      ```
8. Ejecuta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```
