# Sistema de Diagnóstico Vehicular Toyota Corolla 🚗

Sistema de diagnóstico basado en reglas para Toyota Corolla que utiliza un motor de inferencia para analizar descripciones de fallas y proporcionar diagnósticos preliminares.

> Este sistema de motor de inferencia necesita ser entrenado desde su algoritmo de origen, esta en modo de pruebas y test por ahora.

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
git clone https://github.com/cesarcastdj/toyota_inferencia.git
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

## Pruebas de Precisión y Comparación de Métodos 🧪

El archivo `precision_test.py` permite comparar la precisión del sistema de diagnóstico entre el **formulario guiado** y el **chat libre**.

### ¿Para qué sirve?
- Evalúa qué tan bien el motor de inferencia detecta y clasifica problemas según la forma de entrada.
- Compara puntuaciones, categorías detectadas y cobertura de diagnósticos entre ambos métodos.
- Ayuda a identificar limitaciones y oportunidades de mejora en el sistema.

### ¿Cómo se usa?

Ejecuta:
```bash
python precision_test.py
```

Verás una comparación de resultados para distintos casos de prueba, incluyendo:
- Problemas múltiples en una sola entrada
- Problemas específicos
- Texto vago o poco claro

### Recomendaciones de uso
- **Formulario guiado:** Ideal para usuarios que saben exactamente qué problema tienen y buscan un diagnóstico puntual y estructurado.
- **Chat libre:** Recomendado para usuarios que quieren describir varios síntomas, no están seguros del problema o prefieren expresarse de forma natural. Detecta múltiples problemas simultáneamente y es más flexible.

### Conclusión
El chat libre suele ofrecer mayor precisión y cobertura, especialmente cuando el usuario describe varios problemas a la vez. El formulario guiado es útil para diagnósticos específicos y rápidos.

---

## Ejemplo de salida de precision_test.py

```
🎯 COMPARACIÓN DE PRECISIÓN: FORMULARIO GUIADO vs CHAT LIBRE
======================================================================

🔍 CASO 1: MÚLTIPLES PROBLEMAS
----------------------------------------
📋 Formulario: 16 pts, ['frenos']
💬 Chat libre: 18 pts, ['frenos', 'motor']

🔍 CASO 2: PROBLEMA ESPECÍFICO
----------------------------------------
📋 Formulario: 3 pts, ['motor']
💬 Chat libre: 3 pts, ['motor']

🔍 CASO 3: TEXTO VAGO
----------------------------------------
📋 Formulario: 5 pts, ['motor']
💬 Chat libre: 5 pts, ['motor']

📊 ANÁLISIS FINAL:
----------------------------------------
📋 Formulario promedio: 8.0 puntos
💬 Chat libre promedio: 8.7 puntos
📋 Formulario categorías únicas: 2
💬 Chat libre categorías únicas: 2

🏆 CONCLUSIÓN FINAL:
----------------------------------------
   🥇 CHAT LIBRE es más preciso en general
   💡 Razones:
      • Detecta múltiples problemas simultáneamente
      • Mejor cobertura de categorías
      • Más flexible con diferentes formas de expresar problemas

📋 RECOMENDACIÓN DE USO:
----------------------------------------

## Cesar-Dev
