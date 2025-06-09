# Sistema de Diagnóstico Vehicular Toyota Corolla 🚗

Sistema de diagnóstico basado en reglas para Toyota Corolla que utiliza un motor de inferencia para analizar descripciones de fallas y proporcionar diagnósticos preliminares.

## Características Actuales ✨

- Motor de inferencia basado en reglas con sistema de puntuación
- Interfaz web intuitiva y responsiva
- Sistema de categorización de fallas
- Retroalimentación del usuario
- Notificaciones en tiempo real
- Almacenamiento de retroalimentación para análisis futuro

## Requisitos del Sistema 📋

- Python 3.13 o superior
- Flask
- Navegador web moderno

## Instalación 🛠️

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/toyota_inferencia.git
cd toyota_inferencia
```

2. Crear y activar entorno virtual:
```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install flask
```

4. Iniciar la aplicación:
```bash
python app.py
```

5. Abrir en el navegador:
```
http://localhost:5000
```

## Estructura del Proyecto 📁

```
toyota_inferencia/
├── app.py                 # Aplicación principal Flask
├── inference_engine.py    # Motor de inferencia
├── templates/
│   └── index.html        # Interfaz de usuario
├── env/                  # Entorno virtual
└── feedback.json         # Almacenamiento de retroalimentación
```

## Características Implementadas ✅

1. **Motor de Inferencia**
   - Sistema de reglas por categorías
   - Puntuación basada en pesos
   - Detección de múltiples problemas
   - Variantes de palabras clave

2. **Interfaz de Usuario**
   - Diseño responsivo
   - Formulario de entrada intuitivo
   - Visualización clara de diagnósticos
   - Sistema de notificaciones

3. **Sistema de Retroalimentación**
   - Almacenamiento de respuestas
   - Notificaciones de éxito/error
   - Interfaz de calificación

## Próximas Mejoras 🚀

1. **Motor de Inferencia**
   - [ ] Implementar aprendizaje automático básico
   - [ ] Agregar más reglas y categorías
   - [ ] Mejorar el sistema de puntuación
   - [ ] Añadir diagnóstico específico por modelo

2. **Interfaz de Usuario**
   - [ ] Modo oscuro
   - [ ] Historial de diagnósticos
   - [ ] Exportación de resultados
   - [ ] Interfaz para técnicos

3. **Base de Datos**
   - [ ] Migrar a base de datos SQL
   - [ ] Implementar autenticación
   - [ ] Historial de usuarios
   - [ ] Estadísticas de uso

4. **Características Adicionales**
   - [ ] API REST para integración
   - [ ] Soporte para imágenes
   - [ ] Chat en vivo con técnicos
   - [ ] Sistema de citas para servicio

## Contribuir 🤝

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia 📄

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles.

## Contacto 📧

Tu Nombre - [@tutwitter](https://twitter.com/tutwitter) - email@ejemplo.com

Link del Proyecto: [https://github.com/tu-usuario/toyota_inferencia](https://github.com/tu-usuario/toyota_inferencia) 