# inference_engine.py

def diagnose_input(text):
    text = text.lower()

    # Reglas organizadas por categorías - EXPANDIDAS
    reglas = {
        "motor": [
            {"clave": "ruido", "variantes": ["ruido", "sonido", "golpeteo", "tac tac", "knock", "golpe", "martilleo", "repiqueteo"], 
             "respuesta": "Posible problema con el sistema de escape, válvulas o partes internas del motor.", "peso": 3},
            {"clave": "quemado", "variantes": ["quemado", "humo", "olor a quemado", "huele a quemado", "olor quemado"], 
             "respuesta": "Posible sobrecalentamiento, problema eléctrico o fuga de aceite.", "peso": 4},
            {"clave": "vibración", "variantes": ["vibración", "vibra", "temblor", "tembla", "sacudida"], 
             "respuesta": "Revisa los soportes del motor, ruedas desbalanceadas o problemas de RPM.", "peso": 3},
            {"clave": "no enciende", "variantes": ["no enciende", "no arranca", "no prende", "no funciona", "no da"], 
             "respuesta": "Verifica la batería, el motor de arranque, el sistema de combustible o las bujías.", "peso": 5},
            {"clave": "sobrecalentamiento", "variantes": ["sobrecalentamiento", "caliente", "temperatura alta", "calor excesivo"], 
             "respuesta": "Revisa el sistema de refrigeración, termostato, ventilador o nivel de refrigerante.", "peso": 4},
            {"clave": "pérdida potencia", "variantes": ["pérdida de potencia", "sin fuerza", "no tira", "flojo", "sin potencia", "le hace falta fuerza", "falta fuerza", "no tiene fuerza"], 
             "respuesta": "Posible problema con filtros de aire/combustible, inyectores o compresión del motor.", "peso": 3},
            {"clave": "consumo aceite", "variantes": ["consume aceite", "pérdida de aceite", "aceite bajo", "quema aceite"], 
             "respuesta": "Verifica sellos, juntas o desgaste de partes internas del motor.", "peso": 3},
            {"clave": "escape", "variantes": ["escape", "tubo de escape", "mofle", "silenciador"], 
             "respuesta": "Posible rotura, desgaste o problema en el sistema de escape.", "peso": 2},
        ],
        "frenos": [
            {"clave": "frenos", "variantes": ["frenos", "freno", "pedal de freno", "frenado", "frenando"], 
             "respuesta": "Posible desgaste de pastillas, fallo en el sistema hidráulico o aire en las líneas.", "peso": 4},
            {"clave": "chirrido", "variantes": ["chirrido", "chirriar", "chirriado", "chirrido al frenar"], 
             "respuesta": "Las pastillas de freno pueden estar desgastadas o los discos dañados.", "peso": 3},
            {"clave": "pedal suave", "variantes": ["pedal suave", "pedal esponjoso", "pedal bajo", "pedal blando"], 
             "respuesta": "Posible aire en las líneas de freno o fuga de líquido de frenos.", "peso": 4},
            {"clave": "vibración frenar", "variantes": ["vibración al frenar", "tembla al frenar", "vibra al frenar"], 
             "respuesta": "Los discos de freno pueden estar deformados o desgastados irregularmente.", "peso": 3},
            {"clave": "no frena", "variantes": ["no frena", "no frena bien", "frenado deficiente", "no está frenando bien"], 
             "respuesta": "Verifica pastillas, discos, líquido de frenos y sistema hidráulico.", "peso": 5},
            {"clave": "luz frenos", "variantes": ["luz de frenos", "testigo frenos", "indicador frenos"], 
             "respuesta": "Verifica nivel de líquido de frenos, pastillas o sensores.", "peso": 2},
            {"clave": "pastillas", "variantes": ["pastillas", "pastilla", "pastillas de freno"], 
             "respuesta": "Las pastillas de freno pueden estar desgastadas y necesitan reemplazo.", "peso": 3},
        ],
        "transmisión": [
            {"clave": "cambio", "variantes": ["cambio", "marcha", "velocidad", "cambios", "cambiar"], 
             "respuesta": "Posible problema en la transmisión, embrague o sincronizadores.", "peso": 4},
            {"clave": "patina", "variantes": ["patina", "patinaje", "resbala", "patinado"], 
             "respuesta": "El embrague puede estar desgastado o hay problemas de presión.", "peso": 4},
            {"clave": "ruidos transmisión", "variantes": ["ruido transmisión", "ruido cambios", "ruido marchas"], 
             "respuesta": "Posible desgaste de piezas internas, engranajes o sincronizadores.", "peso": 3},
            {"clave": "líquido transmisión", "variantes": ["líquido transmisión", "aceite transmisión", "fuga transmisión"], 
             "respuesta": "Verifica nivel, calidad del líquido o posibles fugas en sellos.", "peso": 3},
            {"clave": "embrague", "variantes": ["embrague", "clutch", "pedal embrague"], 
             "respuesta": "Posible desgaste del disco de embrague, plato de presión o pieza de desgaste.", "peso": 4},
            {"clave": "automática", "variantes": ["automática", "automático", "cambio automático"], 
             "respuesta": "Verifica líquido de transmisión, sensores o válvulas de control.", "peso": 3},
        ],
        "suspensión": [
            {"clave": "golpe", "variantes": ["golpe", "golpea", "golpeteo", "golpes"], 
             "respuesta": "Posible problema en amortiguadores, resortes o piezas de suspensión.", "peso": 3},
            {"clave": "rebota", "variantes": ["rebota", "rebote", "rebotar", "rebotes"], 
             "respuesta": "Los amortiguadores pueden estar desgastados o sin funcionamiento.", "peso": 3},
            {"clave": "ruidos suspensión", "variantes": ["ruido suspensión", "ruido amortiguadores", "crujido"], 
             "respuesta": "Verifica piezas de suspensión, terminales de dirección o amortiguadores.", "peso": 2},
            {"clave": "inestable", "variantes": ["inestable", "tambalea", "se mueve", "flotante"], 
             "respuesta": "Posible problema de alineación, balanceo o neumáticos.", "peso": 3},
            {"clave": "amortiguadores", "variantes": ["amortiguadores", "amortiguador", "shocks"], 
             "respuesta": "Verifica desgaste, fugas de aceite o funcionamiento de amortiguadores.", "peso": 3},
            {"clave": "resortes", "variantes": ["resortes", "resorte", "muelles"], 
             "respuesta": "Posible rotura, desgaste o debilitamiento de los resortes.", "peso": 2},
        ],
        "eléctrico": [
            {"clave": "batería", "variantes": ["batería", "bateria", "pila", "acumulador"], 
             "respuesta": "Verifica carga, terminales, cables o posible reemplazo de batería.", "peso": 4},
            {"clave": "alternador", "variantes": ["alternador", "generador", "carga"], 
             "respuesta": "Posible fallo en el alternador, regulador o sistema de carga.", "peso": 4},
            {"clave": "luces", "variantes": ["luces", "luz", "faros", "iluminación"], 
             "respuesta": "Verifica bombillas, fusibles, interruptores o sistema eléctrico.", "peso": 2},
            {"clave": "no arranca", "variantes": ["no arranca", "no prende", "no da corriente"], 
             "respuesta": "Verifica batería, motor de arranque, cables o sistema de ignición.", "peso": 5},
            {"clave": "cortocircuito", "variantes": ["cortocircuito", "corto", "corto circuito"], 
             "respuesta": "Posible problema en cables, conectores o componentes eléctricos.", "peso": 4},
            {"clave": "fusibles", "variantes": ["fusibles", "fusible", "fuse"], 
             "respuesta": "Verifica fusibles quemados o problemas en el sistema eléctrico.", "peso": 2},
        ],
        "combustible": [
            {"clave": "combustible", "variantes": ["combustible", "gasolina", "gas", "nafta"], 
             "respuesta": "Verifica nivel, calidad del combustible o sistema de inyección.", "peso": 3},
            {"clave": "bomba combustible", "variantes": ["bomba combustible", "bomba gasolina", "bomba gas"], 
             "respuesta": "Posible fallo en la bomba de combustible o filtro.", "peso": 4},
            {"clave": "inyectores", "variantes": ["inyectores", "inyector", "inyección"], 
             "respuesta": "Verifica limpieza, funcionamiento o reemplazo de inyectores.", "peso": 3},
            {"clave": "filtro combustible", "variantes": ["filtro combustible", "filtro gasolina", "filtro gas"], 
             "respuesta": "Posible obstrucción o reemplazo necesario del filtro de combustible.", "peso": 3},
            {"clave": "consumo alto", "variantes": ["consumo alto", "gasta mucho", "alto consumo"], 
             "respuesta": "Verifica inyectores, filtros, sensores o sistema de inyección.", "peso": 3},
            {"clave": "olor gasolina", "variantes": ["olor gasolina", "huele a gasolina", "olor gas"], 
             "respuesta": "Posible fuga en líneas, tanque o sistema de combustible.", "peso": 4},
        ],
        "refrigeración": [
            {"clave": "refrigerante", "variantes": ["refrigerante", "anticongelante", "coolant", "líquido refrigerante"], 
             "respuesta": "Verifica nivel, calidad o posibles fugas del refrigerante.", "peso": 3},
            {"clave": "termostato", "variantes": ["termostato", "termostato motor"], 
             "respuesta": "Posible fallo en el termostato que regula la temperatura.", "peso": 3},
            {"clave": "ventilador", "variantes": ["ventilador", "fan", "ventilador motor"], 
             "respuesta": "Verifica funcionamiento del ventilador de refrigeración.", "peso": 2},
            {"clave": "radiador", "variantes": ["radiador", "radiator"], 
             "respuesta": "Posible obstrucción, fuga o daño en el radiador.", "peso": 3},
        ],
        "dirección": [
            {"clave": "dirección", "variantes": ["dirección", "volante", "steering"], 
             "respuesta": "Verifica sistema de dirección, líquido o componentes.", "peso": 3},
            {"clave": "alineación", "variantes": ["alineación", "alinear", "desalineado"], 
             "respuesta": "Necesita alineación de las ruedas delanteras.", "peso": 3},
            {"clave": "balanceo", "variantes": ["balanceo", "balancear", "desbalanceado"], 
             "respuesta": "Necesita balanceo de las ruedas.", "peso": 2},
        ],
        "neumáticos": [
            {"clave": "neumáticos", "variantes": ["neumáticos", "llantas", "ruedas", "tires"], 
             "respuesta": "Verifica presión, desgaste o daños en los neumáticos.", "peso": 2},
            {"clave": "presión", "variantes": ["presión", "aire", "inflado"], 
             "respuesta": "Verifica y ajusta la presión de los neumáticos.", "peso": 2},
            {"clave": "desgaste", "variantes": ["desgaste", "gastado", "liso"], 
             "respuesta": "Los neumáticos pueden necesitar reemplazo por desgaste.", "peso": 3},
        ]
    }

    resultados = []
    puntuación_total = 0
    categorías_detectadas = set()

    # Función para verificar contexto relevante
    def es_contexto_relevante(texto, palabra_clave, categoria):
        # Palabras que indican que el problema es del vehículo
        indicadores_vehiculo = [
            "motor", "carro", "auto", "vehículo", "coche", "toyota", "corolla",
            "frenos", "transmisión", "suspensión", "eléctrico", "combustible",
            "refrigeración", "dirección", "neumáticos", "ruedas", "llantas",
            "pedal", "volante", "tablero", "luces", "batería", "aceite",
            "gasolina", "gas", "nafta", "refrigerante", "líquido", "filtro",
            "hace", "tiene", "problema", "falla", "daño", "mal", "no", "no funciona",
            "ruido", "sonido", "vibración", "temblor", "olor", "humo", "calor",
            "enciende", "arranca", "prende", "funciona", "tira", "fuerza",
            "frenando", "frena", "pastillas", "colinas", "acelerar", "acelera",
            "potencia", "fuerza", "subir", "necesita", "falta"
        ]
        
        # Palabras que indican texto vago o muy general
        palabras_vagas = [
            "problemas", "problema", "mal", "no funciona", "no funciona bien",
            "tiene problemas", "está mal", "no anda", "no sirve"
        ]
        
        # Si el texto es muy corto (menos de 5 palabras), ser más permisivo
        palabras = texto.split()
        if len(palabras) < 5:
            # Verificar si solo contiene palabras vagas
            palabras_vagas_en_texto = [p for p in palabras if p in palabras_vagas]
            if len(palabras_vagas_en_texto) >= len(palabras) * 0.7:  # Si 70% son vagas
                return False
            return True
        
        # Verificar si hay indicadores de vehículo cerca de la palabra clave
        try:
            indice = palabras.index(palabra_clave)
            # Buscar indicadores en un rango de 8 palabras antes y después
            inicio = max(0, indice - 8)
            fin = min(len(palabras), indice + 9)
            
            for i in range(inicio, fin):
                if palabras[i] in indicadores_vehiculo:
                    return True
        except ValueError:
            pass
        
        # Si no encuentra contexto específico, verificar si hay palabras relacionadas con problemas específicos
        palabras_problema_especifico = ["ruido", "sonido", "vibración", "olor", "humo", "calor", "necesita", "falta", "chirrido", "golpe", "rebota", "patina"]
        for palabra in palabras_problema_especifico:
            if palabra in texto:
                return True
        
        # Si solo contiene palabras vagas, rechazar
        palabras_vagas_en_texto = [p for p in palabras if p in palabras_vagas]
        if len(palabras_vagas_en_texto) >= len(palabras) * 0.6:  # Si 60% son vagas
            return False
        
        return False

    # Analizar el texto para cada categoría con verificación de contexto
    for categoría, reglas_cat in reglas.items():
        for regla in reglas_cat:
            # Verificar todas las variantes de la palabra clave
            for variante in regla["variantes"]:
                if variante in text:
                    # Verificar si el contexto es relevante para el vehículo
                    if es_contexto_relevante(text, variante, categoría):
                        puntuación_total += regla["peso"]
                        categorías_detectadas.add(categoría)
                        resultados.append({
                            "respuesta": regla["respuesta"],
                            "peso": regla["peso"],
                            "categoría": categoría
                        })
                        break  # Si encontramos una variante, no necesitamos verificar las demás

    # Filtrar resultados por relevancia y coherencia
    if len(categorías_detectadas) > 3:
        # Si hay demasiadas categorías, mantener solo las más relevantes
        resultados_ordenados = sorted(resultados, key=lambda x: x["peso"], reverse=True)
        resultados = resultados_ordenados[:3]  # Mantener solo los 3 más relevantes
        categorías_detectadas = set(r["categoría"] for r in resultados)
        puntuación_total = sum(r["peso"] for r in resultados)

    if not resultados:
        return {
            "diagnóstico": "La descripción es muy general. Por favor, proporciona más detalles específicos como: ¿qué ruidos hace? ¿cuándo ocurre el problema? ¿qué síntomas específicos notas? Esto me ayudará a dar un diagnóstico más preciso.",
            "puntuación": 0,
            "categorías": []
        }

    # Ordenar resultados por peso
    resultados.sort(key=lambda x: x["peso"], reverse=True)

    # Generar recomendación general basada en las categorías detectadas
    recomendación_general = ""
    if len(categorías_detectadas) > 2:
        recomendación_general = "Se detectaron múltiples problemas. Se recomienda una revisión completa del vehículo por un técnico especializado."
    elif len(categorías_detectadas) > 1:
        recomendación_general = "Se detectaron problemas en diferentes sistemas. Se recomienda una revisión integral del vehículo."
    elif "motor" in categorías_detectadas:
        recomendación_general = "Se recomienda una revisión del motor lo antes posible para evitar daños mayores."
    elif "frenos" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar el sistema de frenos inmediatamente por seguridad."
    elif "transmisión" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar la transmisión para evitar daños mayores y costos elevados."
    elif "suspensión" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar la suspensión para mejorar el manejo y seguridad del vehículo."
    elif "eléctrico" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar el sistema eléctrico para evitar fallas inesperadas."
    elif "combustible" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar el sistema de combustible para optimizar el rendimiento."
    elif "refrigeración" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar el sistema de refrigeración para evitar sobrecalentamiento."
    elif "dirección" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar el sistema de dirección para mantener el control del vehículo."
    elif "neumáticos" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar los neumáticos para garantizar la seguridad en la conducción."

    return {
        "diagnóstico": [r["respuesta"] for r in resultados],
        "puntuación": puntuación_total,
        "categorías": list(categorías_detectadas),
        "recomendación_general": recomendación_general
    } 