#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from inference_engine import diagnose_input

def test_categorias():
    # Casos de prueba mejorados
    casos_prueba = [
        # Casos específicos de Toyota Corolla (deberían funcionar bien)
        "el motor de mi toyota corolla hace ruido extraño",
        "los frenos de mi corolla chirrían al frenar",
        "la transmisión de mi toyota patina",
        "la suspensión de mi corolla rebota",
        "la batería de mi toyota está descargada",
        "el combustible de mi corolla huele mal",
        "el refrigerante de mi toyota está bajo",
        "la dirección de mi corolla está dura",
        "los neumáticos de mi toyota están lisos",
        
        # Casos vagos (deberían ser rechazados o dar diagnósticos generales)
        "problema general del carro",
        "no funciona nada",
        "el auto está mal",
        "tiene problemas",
        
        # Casos irrelevantes (deberían ser rechazados)
        "me duele la cabeza",
        "tengo fiebre",
        "mi casa tiene problemas",
        "mi computadora no funciona",
        "necesito ir al médico",
        "mi teléfono está roto",
        
        # Casos específicos pero sin contexto de vehículo
        "hace ruido",
        "no funciona",
        "está roto",
    ]
    
    print("=== PRUEBAS DEL MOTOR DE INFERENCIA MEJORADO ===\n")
    print("Motor especializado para Toyota Corolla - Detección de fallas mecánicas\n")
    
    for i, caso in enumerate(casos_prueba, 1):
        print(f"Prueba {i}: '{caso}'")
        resultado = diagnose_input(caso)
        
        print(f"  - Puntuación: {resultado['puntuación']}")
        print(f"  - Categorías detectadas: {resultado['categorías']}")
        print(f"  - Número de categorías: {len(resultado['categorías'])}")
        
        if resultado['categorías']:
            print(f"  - ✅ Categorías específicas: {', '.join(resultado['categorías'])}")
        else:
            print(f"  - ⚠️  NO SE DETECTARON CATEGORÍAS")
        
        print(f"  - Diagnóstico: {resultado['diagnóstico']}")
        print(f"  - Recomendación: {resultado['recomendación_general']}")
        print("-" * 60)

def test_formulario_guiado():
    print("\n" + "="*80)
    print("PRUEBAS ESPECÍFICAS PARA FORMULARIO GUIADO")
    print("Simulando múltiples síntomas seleccionados por el usuario")
    print("="*80 + "\n")
    
    # Casos de formulario guiado con múltiples síntomas
    casos_formulario = [
        # Frenos con múltiples síntomas
        "problemas en frenos: nivel de líquido bajo, pastillas desgastadas, sensores fallando",
        "sistema de frenos: pedal suave, chirrido al frenar, luz de frenos encendida",
        "frenos del auto: no frena bien, vibración al frenar, pastillas de freno",
        
        # Motor con múltiples síntomas
        "motor del auto: ruido extraño, vibración, pérdida de potencia",
        "problemas motor: sobrecalentamiento, consumo de aceite, humo",
        "motor toyota: no arranca, batería descargada, alternador fallando",
        
        # Transmisión con múltiples síntomas
        "transmisión: patina, ruidos, líquido bajo",
        "cambio de marchas: problemas, embrague desgastado, automática",
        
        # Eléctrico con múltiples síntomas
        "sistema eléctrico: batería, alternador, luces, sensores",
        "problemas eléctricos: no arranca, cortocircuito, fusibles",
        
        # Combustible con múltiples síntomas
        "combustible: nivel bajo, olor a gasolina, inyectores, filtro",
        "sistema combustible: bomba, consumo alto, calidad",
        
        # Refrigeración con múltiples síntomas
        "refrigeración: nivel bajo, termostato, ventilador, radiador",
        "sistema refrigeración: refrigerante, temperatura alta, fuga",
        
        # Suspensión con múltiples síntomas
        "suspensión: rebota, golpes, amortiguadores, resortes",
        "sistema suspensión: inestable, ruidos, desgaste",
        
        # Dirección con múltiples síntomas
        "dirección: dura, alineación, balanceo, líquido",
        "sistema dirección: volante, desalineado, desbalanceado",
        
        # Neumáticos con múltiples síntomas
        "neumáticos: presión, desgaste, lisos, daños",
        "llantas: aire, inflado, gastadas, reemplazo",
    ]
    
    for i, caso in enumerate(casos_formulario, 1):
        print(f"Formulario {i}: '{caso}'")
        resultado = diagnose_input(caso)
        
        print(f"  - Puntuación: {resultado['puntuación']}")
        print(f"  - Categorías detectadas: {resultado['categorías']}")
        print(f"  - Número de categorías: {len(resultado['categorías'])}")
        
        if resultado['categorías']:
            print(f"  - ✅ Categorías específicas: {', '.join(resultado['categorías'])}")
            if 'síntomas_detectados' in resultado:
                print(f"  - 📊 Síntomas por categoría:")
                for cat, datos in resultado['síntomas_detectados'].items():
                    print(f"    • {cat}: {len(datos['síntomas'])} síntomas (peso: {datos['peso_total']})")
        else:
            print(f"  - ⚠️  NO SE DETECTARON CATEGORÍAS")
        
        print(f"  - Diagnóstico: {resultado['diagnóstico']}")
        print(f"  - Recomendación: {resultado['recomendación_general']}")
        print("-" * 60)

if __name__ == "__main__":
    test_categorias()
    test_formulario_guiado() 