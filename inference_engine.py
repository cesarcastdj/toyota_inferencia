# inference_engine.py

def diagnose_input(text):
    text = text.lower()

    # Reglas organizadas por categorías
    reglas = {
        "motor": [
            {"clave": "ruido", "variantes": ["ruido", "sonido", "golpeteo", "tac tac"], 
             "respuesta": "Posible problema con el sistema de escape o motor.", "peso": 2},
            {"clave": "quemado", "variantes": ["quemado", "humo", "olor a quemado"], 
             "respuesta": "Posible sobrecalentamiento o problema eléctrico.", "peso": 3},
            {"clave": "vibración", "variantes": ["vibración", "vibra", "temblor"], 
             "respuesta": "Revisa los soportes del motor o ruedas desbalanceadas.", "peso": 2},
            {"clave": "no enciende", "variantes": ["no enciende", "no arranca", "no prende"], 
             "respuesta": "Verifica la batería, el motor de arranque o el sistema de combustible.", "peso": 4},
        ],
        "frenos": [
            {"clave": "frenos", "variantes": ["frenos", "freno", "pedal de freno"], 
             "respuesta": "Posible desgaste de pastillas o fallo en el sistema hidráulico.", "peso": 3},
            {"clave": "chirrido", "variantes": ["chirrido", "chirriar", "chirriado"], 
             "respuesta": "Las pastillas de freno pueden estar desgastadas.", "peso": 2},
        ],
        "transmisión": [
            {"clave": "cambio", "variantes": ["cambio", "marcha", "velocidad"], 
             "respuesta": "Posible problema en la transmisión o embrague.", "peso": 3},
            {"clave": "patina", "variantes": ["patina", "patinaje", "resbala"], 
             "respuesta": "El embrague puede estar desgastado.", "peso": 2},
        ],
        "suspensión": [
            {"clave": "golpe", "variantes": ["golpe", "golpea", "golpeteo"], 
             "respuesta": "Posible problema en la suspensión o amortiguadores.", "peso": 2},
            {"clave": "rebota", "variantes": ["rebota", "rebote", "rebotar"], 
             "respuesta": "Los amortiguadores pueden estar desgastados.", "peso": 2},
        ]
    }

    resultados = []
    puntuación_total = 0
    categorías_detectadas = set()

    # Analizar el texto para cada categoría
    for categoría, reglas_cat in reglas.items():
        for regla in reglas_cat:
            # Verificar todas las variantes de la palabra clave
            for variante in regla["variantes"]:
                if variante in text:
                    puntuación_total += regla["peso"]
                    categorías_detectadas.add(categoría)
                    resultados.append({
                        "respuesta": regla["respuesta"],
                        "peso": regla["peso"],
                        "categoría": categoría
                    })
                    break  # Si encontramos una variante, no necesitamos verificar las demás

    if not resultados:
        return {
            "diagnóstico": "No se detectaron fallas conocidas. Intenta describir el problema con más detalle.",
            "puntuación": 0,
            "categorías": []
        }

    # Ordenar resultados por peso
    resultados.sort(key=lambda x: x["peso"], reverse=True)

    # Generar recomendación general basada en las categorías detectadas
    recomendación_general = ""
    if len(categorías_detectadas) > 1:
        recomendación_general = "Se detectaron múltiples problemas. Se recomienda una revisión completa del vehículo."
    elif "motor" in categorías_detectadas:
        recomendación_general = "Se recomienda una revisión del motor lo antes posible."
    elif "frenos" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar el sistema de frenos inmediatamente por seguridad."
    elif "transmisión" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar la transmisión para evitar daños mayores."
    elif "suspensión" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar la suspensión para mejorar el manejo del vehículo."

    return {
        "diagnóstico": [r["respuesta"] for r in resultados],
        "puntuación": puntuación_total,
        "categorías": list(categorías_detectadas),
        "recomendación_general": recomendación_general
    } 