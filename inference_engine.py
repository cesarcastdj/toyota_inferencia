# inference_engine.py

def diagnose_input(text):
    text = text.lower().strip()

    # Reglas organizadas por categorías - ESPECIALIZADAS PARA TOYOTA COROLLA
    reglas = {
        "motor": [
            {"clave": "ruido motor", "variantes": ["ruido del motor", "motor hace ruido", "sonido del motor", "golpeteo del motor", "knock del motor", "martilleo del motor"], 
             "respuesta": "Posible problema con el sistema de escape, válvulas, pistones o partes internas del motor. Verifica nivel de aceite y estado del sistema de escape.", "peso": 4},
            {"clave": "quemado motor", "variantes": ["motor quemado", "olor a quemado del motor", "humo del motor", "motor huele a quemado"], 
             "respuesta": "Posible sobrecalentamiento, problema eléctrico o fuga de aceite. Verifica nivel de refrigerante y temperatura del motor.", "peso": 5},
            {"clave": "vibración motor", "variantes": ["motor vibra", "vibración del motor", "motor tembla", "sacudida del motor"], 
             "respuesta": "Revisa los soportes del motor, ruedas desbalanceadas, problemas de RPM o desgaste de piezas internas.", "peso": 4},
            {"clave": "no arranca motor", "variantes": ["motor no arranca", "no enciende el motor", "motor no prende", "no da el motor"], 
             "respuesta": "Verifica batería, motor de arranque, sistema de combustible, bujías o sistema de ignición.", "peso": 6},
            {"clave": "sobrecalentamiento", "variantes": ["motor caliente", "sobrecalentamiento", "temperatura alta del motor", "motor muy caliente"], 
             "respuesta": "Revisa sistema de refrigeración, termostato, ventilador, nivel de refrigerante o posibles fugas.", "peso": 5},
            {"clave": "pérdida potencia", "variantes": ["motor sin fuerza", "motor no tira", "motor flojo", "pérdida de potencia del motor", "motor sin potencia"], 
             "respuesta": "Posible problema con filtros de aire/combustible, inyectores, compresión del motor o sistema de escape.", "peso": 4},
            {"clave": "consumo aceite", "variantes": ["motor consume aceite", "pérdida de aceite del motor", "aceite bajo del motor", "motor quema aceite"], 
             "respuesta": "Verifica sellos, juntas, desgaste de partes internas o posible fuga de aceite.", "peso": 4},
            {"clave": "escape", "variantes": ["escape del motor", "tubo de escape", "mofle", "silenciador del motor"], 
             "respuesta": "Posible rotura, desgaste o problema en el sistema de escape del motor.", "peso": 3},
        ],
        "frenos": [
            {"clave": "frenos", "variantes": ["frenos del auto", "sistema de frenos", "pedal de freno", "frenado del auto"], 
             "respuesta": "Posible desgaste de pastillas, fallo en el sistema hidráulico o aire en las líneas de freno.", "peso": 5},
            {"clave": "chirrido frenos", "variantes": ["chirrido de frenos", "frenos chirrían", "chirrido al frenar", "frenos hacen chirrido"], 
             "respuesta": "Las pastillas de freno pueden estar desgastadas o los discos dañados. Revisa estado de pastillas y discos.", "peso": 4},
            {"clave": "pedal suave", "variantes": ["pedal de freno suave", "pedal esponjoso", "pedal bajo", "pedal blando"], 
             "respuesta": "Posible aire en las líneas de freno o fuga de líquido de frenos. Verifica nivel de líquido y purga el sistema.", "peso": 5},
            {"clave": "vibración frenar", "variantes": ["vibración al frenar", "tembla al frenar", "vibra al frenar", "frenos vibran"], 
             "respuesta": "Los discos de freno pueden estar deformados o desgastados irregularmente. Revisa estado de discos.", "peso": 4},
            {"clave": "no frena", "variantes": ["no frena bien", "frenado deficiente", "no está frenando bien", "frenos no funcionan"], 
             "respuesta": "Verifica pastillas, discos, líquido de frenos y sistema hidráulico. Posible fallo en bomba de frenos.", "peso": 6},
            {"clave": "luz frenos", "variantes": ["luz de frenos", "testigo de frenos", "indicador de frenos", "luz de frenos encendida"], 
             "respuesta": "Verifica nivel de líquido de frenos, pastillas o sensores del sistema de frenos.", "peso": 3},
            {"clave": "pastillas", "variantes": ["pastillas de freno", "pastillas", "pastilla de freno", "pastillas desgastadas"], 
             "respuesta": "Las pastillas de freno pueden estar desgastadas y necesitan reemplazo.", "peso": 4},
            {"clave": "líquido frenos", "variantes": ["líquido de frenos", "líquido frenos", "nivel de líquido", "líquido bajo"], 
             "respuesta": "Verifica nivel de líquido de frenos y posibles fugas en el sistema hidráulico.", "peso": 4},
            {"clave": "sensores frenos", "variantes": ["sensores de frenos", "sensor de frenos", "sensores", "sensor"], 
             "respuesta": "Verifica funcionamiento de sensores del sistema de frenos y conexiones eléctricas.", "peso": 3},
        ],
        "transmisión": [
            {"clave": "cambio", "variantes": ["cambio de marchas", "marchas", "velocidades", "cambios de velocidad", "transmisión"], 
             "respuesta": "Posible problema en la transmisión, embrague o sincronizadores. Verifica líquido de transmisión.", "peso": 5},
            {"clave": "patina", "variantes": ["patina", "patinaje", "resbala", "patinado", "embrague patina"], 
             "respuesta": "El embrague puede estar desgastado o hay problemas de presión. Revisa desgaste del disco de embrague.", "peso": 5},
            {"clave": "ruidos transmisión", "variantes": ["ruido de transmisión", "ruido de cambios", "ruido de marchas", "transmisión hace ruido"], 
             "respuesta": "Posible desgaste de piezas internas, engranajes o sincronizadores de la transmisión.", "peso": 4},
            {"clave": "líquido transmisión", "variantes": ["líquido de transmisión", "aceite de transmisión", "fuga de transmisión", "nivel de líquido transmisión"], 
             "respuesta": "Verifica nivel, calidad del líquido o posibles fugas en sellos de la transmisión.", "peso": 4},
            {"clave": "embrague", "variantes": ["embrague", "clutch", "pedal de embrague", "embrague del auto"], 
             "respuesta": "Posible desgaste del disco de embrague, plato de presión o pieza de desgaste.", "peso": 5},
            {"clave": "automática", "variantes": ["transmisión automática", "automática", "cambio automático"], 
             "respuesta": "Verifica líquido de transmisión, sensores o válvulas de control de la transmisión automática.", "peso": 4},
        ],
        "suspensión": [
            {"clave": "golpe suspensión", "variantes": ["golpe en suspensión", "suspensión golpea", "golpeteo de suspensión", "golpes en suspensión"], 
             "respuesta": "Posible problema en amortiguadores, resortes o piezas de suspensión. Verifica desgaste de componentes.", "peso": 4},
            {"clave": "rebota", "variantes": ["suspensión rebota", "rebota", "rebote de suspensión", "auto rebota"], 
             "respuesta": "Los amortiguadores pueden estar desgastados o sin funcionamiento. Revisa estado de amortiguadores.", "peso": 4},
            {"clave": "ruidos suspensión", "variantes": ["ruido de suspensión", "ruido de amortiguadores", "crujido de suspensión"], 
             "respuesta": "Verifica piezas de suspensión, terminales de dirección o amortiguadores.", "peso": 3},
            {"clave": "inestable", "variantes": ["auto inestable", "tambalea", "se mueve", "flotante", "inestable"], 
             "respuesta": "Posible problema de alineación, balanceo, neumáticos o componentes de suspensión.", "peso": 4},
            {"clave": "amortiguadores", "variantes": ["amortiguadores", "amortiguador", "shocks", "amortiguadores del auto"], 
             "respuesta": "Verifica desgaste, fugas de aceite o funcionamiento de amortiguadores.", "peso": 4},
            {"clave": "resortes", "variantes": ["resortes", "resorte", "muelles", "resortes del auto"], 
             "respuesta": "Posible rotura, desgaste o debilitamiento de los resortes de suspensión.", "peso": 3},
        ],
        "eléctrico": [
            {"clave": "batería", "variantes": ["batería del auto", "bateria", "pila del auto", "acumulador"], 
             "respuesta": "Verifica carga, terminales, cables o posible reemplazo de batería. Revisa alternador.", "peso": 5},
            {"clave": "alternador", "variantes": ["alternador", "generador", "carga del auto", "alternador del auto"], 
             "respuesta": "Posible fallo en el alternador, regulador o sistema de carga. Verifica voltaje de carga.", "peso": 5},
            {"clave": "luces", "variantes": ["luces del auto", "luz del auto", "faros", "iluminación del auto"], 
             "respuesta": "Verifica bombillas, fusibles, interruptores o sistema eléctrico de iluminación.", "peso": 3},
            {"clave": "no arranca eléctrico", "variantes": ["no arranca el auto", "no prende el auto", "no da corriente", "auto no arranca"], 
             "respuesta": "Verifica batería, motor de arranque, cables o sistema de ignición.", "peso": 6},
            {"clave": "cortocircuito", "variantes": ["cortocircuito", "corto", "corto circuito", "problema eléctrico"], 
             "respuesta": "Posible problema en cables, conectores o componentes eléctricos del auto.", "peso": 5},
            {"clave": "fusibles", "variantes": ["fusibles", "fusible", "fuse", "fusibles del auto"], 
             "respuesta": "Verifica fusibles quemados o problemas en el sistema eléctrico del auto.", "peso": 3},
            {"clave": "sensores eléctricos", "variantes": ["sensores eléctricos", "sensor eléctrico", "sensores del motor"], 
             "respuesta": "Verifica funcionamiento de sensores del motor y sistema eléctrico.", "peso": 4},
        ],
        "combustible": [
            {"clave": "combustible", "variantes": ["combustible", "gasolina", "gas", "nafta", "sistema de combustible"], 
             "respuesta": "Verifica nivel, calidad del combustible o sistema de inyección del auto.", "peso": 4},
            {"clave": "bomba combustible", "variantes": ["bomba de combustible", "bomba de gasolina", "bomba de gas", "bomba combustible"], 
             "respuesta": "Posible fallo en la bomba de combustible o filtro. Verifica presión de combustible.", "peso": 5},
            {"clave": "inyectores", "variantes": ["inyectores", "inyector", "inyección", "inyectores del motor"], 
             "respuesta": "Verifica limpieza, funcionamiento o reemplazo de inyectores del motor.", "peso": 4},
            {"clave": "filtro combustible", "variantes": ["filtro de combustible", "filtro de gasolina", "filtro de gas", "filtro combustible"], 
             "respuesta": "Posible obstrucción o reemplazo necesario del filtro de combustible.", "peso": 4},
            {"clave": "consumo alto", "variantes": ["consumo alto", "gasta mucho combustible", "alto consumo", "gasta mucha gasolina"], 
             "respuesta": "Verifica inyectores, filtros, sensores o sistema de inyección para optimizar consumo.", "peso": 4},
            {"clave": "olor gasolina", "variantes": ["olor a gasolina", "huele a gasolina", "olor de gasolina", "huele gasolina"], 
             "respuesta": "Posible fuga en líneas, tanque o sistema de combustible. Verifica posibles fugas.", "peso": 5},
            {"clave": "nivel combustible", "variantes": ["nivel de combustible", "combustible bajo", "tanque bajo"], 
             "respuesta": "Verifica nivel de combustible y funcionamiento del indicador de nivel.", "peso": 3},
        ],
        "refrigeración": [
            {"clave": "refrigerante", "variantes": ["refrigerante", "anticongelante", "coolant", "líquido refrigerante"], 
             "respuesta": "Verifica nivel, calidad o posibles fugas del refrigerante del motor.", "peso": 4},
            {"clave": "termostato", "variantes": ["termostato", "termostato del motor", "termostato del auto"], 
             "respuesta": "Posible fallo en el termostato que regula la temperatura del motor.", "peso": 4},
            {"clave": "ventilador", "variantes": ["ventilador", "fan", "ventilador del motor", "ventilador del auto"], 
             "respuesta": "Verifica funcionamiento del ventilador de refrigeración del motor.", "peso": 3},
            {"clave": "radiador", "variantes": ["radiador", "radiator", "radiador del auto"], 
             "respuesta": "Posible obstrucción, fuga o daño en el radiador del sistema de refrigeración.", "peso": 4},
            {"clave": "nivel refrigerante", "variantes": ["nivel de refrigerante", "refrigerante bajo", "líquido bajo"], 
             "respuesta": "Verifica nivel de refrigerante y posibles fugas en el sistema de refrigeración.", "peso": 4},
        ],
        "dirección": [
            {"clave": "dirección", "variantes": ["dirección del auto", "volante", "steering", "sistema de dirección"], 
             "respuesta": "Verifica sistema de dirección, líquido o componentes de dirección.", "peso": 4},
            {"clave": "alineación", "variantes": ["alineación", "alinear", "desalineado", "alineación del auto"], 
             "respuesta": "Necesita alineación de las ruedas delanteras del auto.", "peso": 4},
            {"clave": "balanceo", "variantes": ["balanceo", "balancear", "desbalanceado", "balanceo de ruedas"], 
             "respuesta": "Necesita balanceo de las ruedas del auto.", "peso": 3},
            {"clave": "líquido dirección", "variantes": ["líquido de dirección", "líquido dirección", "nivel dirección"], 
             "respuesta": "Verifica nivel de líquido de dirección y posibles fugas.", "peso": 3},
        ],
        "neumáticos": [
            {"clave": "neumáticos", "variantes": ["neumáticos", "llantas", "ruedas", "tires", "neumáticos del auto"], 
             "respuesta": "Verifica presión, desgaste o daños en los neumáticos del auto.", "peso": 3},
            {"clave": "presión", "variantes": ["presión de neumáticos", "aire de neumáticos", "inflado", "presión de llantas"], 
             "respuesta": "Verifica y ajusta la presión de los neumáticos del auto.", "peso": 3},
            {"clave": "desgaste", "variantes": ["desgaste de neumáticos", "neumáticos gastados", "lisos", "neumáticos lisos"], 
             "respuesta": "Los neumáticos pueden necesitar reemplazo por desgaste.", "peso": 4},
        ]
    }

    resultados = []
    puntuación_total = 0
    categorías_detectadas = set()
    síntomas_por_categoría = {}  # Para acumular síntomas por categoría

    # Función para verificar contexto relevante (muy simplificada)
    def es_contexto_relevante(texto, palabra_clave, categoria):
        # Si el texto es muy corto (menos de 3 palabras), ser permisivo
        palabras = texto.split()
        if len(palabras) < 3:
            return True
        
        # Si contiene la palabra clave específica, es relevante
        if palabra_clave in texto:
            return True
        
        # Si contiene palabras relacionadas con problemas específicos, es relevante
        palabras_problema_especifico = [
            "ruido", "sonido", "vibración", "olor", "humo", "calor", "necesita", "falta", 
            "chirrido", "golpe", "rebota", "patina", "arranca", "prende", "funciona", 
            "nivel", "bajo", "alto", "desgastado", "desgastada", "problema", "falla",
            "no", "mal", "daño", "roto", "suave", "duro", "débil", "fuerte"
        ]
        
        for palabra in palabras_problema_especifico:
            if palabra in texto:
                return True
        
        return False

    # Analizar el texto para cada categoría con verificación de contexto
    for categoría, reglas_cat in reglas.items():
        síntomas_categoría = []
        peso_categoría = 0
        
        for regla in reglas_cat:
            # Verificar todas las variantes de la palabra clave
            for variante in regla["variantes"]:
                if variante in text:
                    # Verificar si el contexto es relevante para el vehículo
                    if es_contexto_relevante(text, variante, categoría):
                        peso_categoría += regla["peso"]
                        síntomas_categoría.append(regla["respuesta"])
                        break  # Si encontramos una variante, no necesitamos verificar las demás
        
        # Si se detectaron síntomas en esta categoría, agregarlos
        if síntomas_categoría:
            categorías_detectadas.add(categoría)
            síntomas_por_categoría[categoría] = {
                "síntomas": síntomas_categoría,
                "peso_total": peso_categoría
            }
            puntuación_total += peso_categoría

    # Filtrar resultados por relevancia y coherencia
    if len(categorías_detectadas) > 3:
        # Si hay demasiadas categorías, mantener solo las más relevantes
        categorías_ordenadas = sorted(síntomas_por_categoría.items(), key=lambda x: x[1]["peso_total"], reverse=True)
        categorías_detectadas = set(cat[0] for cat in categorías_ordenadas[:3])
        síntomas_por_categoría = {cat: datos for cat, datos in categorías_ordenadas[:3]}
        puntuación_total = sum(datos["peso_total"] for datos in síntomas_por_categoría.values())

    if not síntomas_por_categoría:
        return {
            "diagnóstico": "La descripción es muy general o no específica para problemas mecánicos de Toyota Corolla. Por favor, proporciona más detalles específicos como: ¿qué ruidos hace el motor? ¿cuándo ocurre el problema? ¿qué síntomas específicos notas en el auto? Esto me ayudará a dar un diagnóstico más preciso.",
            "puntuación": 0,
            "categorías": [],
            "recomendación_general": "Para obtener un diagnóstico preciso de tu Toyota Corolla, describe síntomas específicos del vehículo como ruidos, vibraciones, luces del tablero, problemas de rendimiento, etc."
        }

    # Generar diagnósticos compuestos por categoría
    diagnósticos_compuestos = []
    for categoría, datos in síntomas_por_categoría.items():
        if len(datos["síntomas"]) > 1:
            # Si hay múltiples síntomas en la misma categoría, crear diagnóstico compuesto
            diagnóstico_compuesto = f"Problemas múltiples en {categoría}: {' '.join(datos['síntomas'])}"
            diagnósticos_compuestos.append(diagnóstico_compuesto)
        else:
            # Si solo hay un síntoma, usar el diagnóstico original
            diagnósticos_compuestos.extend(datos["síntomas"])

    # Generar recomendación general basada en las categorías detectadas
    recomendación_general = ""
    if len(categorías_detectadas) > 2:
        recomendación_general = f"Se detectaron múltiples problemas en tu Toyota Corolla: {', '.join(categorías_detectadas)}. Se recomienda una revisión completa del vehículo por un técnico especializado en Toyota."
    elif len(categorías_detectadas) > 1:
        recomendación_general = f"Se detectaron problemas en diferentes sistemas de tu Toyota Corolla: {', '.join(categorías_detectadas)}. Se recomienda una revisión integral del vehículo."
    elif "motor" in categorías_detectadas:
        recomendación_general = "Se recomienda una revisión del motor de tu Toyota Corolla lo antes posible para evitar daños mayores."
    elif "frenos" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar el sistema de frenos de tu Toyota Corolla inmediatamente por seguridad."
    elif "transmisión" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar la transmisión de tu Toyota Corolla para evitar daños mayores y costos elevados."
    elif "suspensión" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar la suspensión de tu Toyota Corolla para mejorar el manejo y seguridad del vehículo."
    elif "eléctrico" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar el sistema eléctrico de tu Toyota Corolla para evitar fallas inesperadas."
    elif "combustible" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar el sistema de combustible de tu Toyota Corolla para optimizar el rendimiento."
    elif "refrigeración" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar el sistema de refrigeración de tu Toyota Corolla para evitar sobrecalentamiento."
    elif "dirección" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar el sistema de dirección de tu Toyota Corolla para mantener el control del vehículo."
    elif "neumáticos" in categorías_detectadas:
        recomendación_general = "Se recomienda revisar los neumáticos de tu Toyota Corolla para garantizar la seguridad en la conducción."

    return {
        "diagnóstico": diagnósticos_compuestos,
        "puntuación": puntuación_total,
        "categorías": list(categorías_detectadas),
        "recomendación_general": recomendación_general,
        "síntomas_detectados": síntomas_por_categoría  # Información adicional para debugging
    } 