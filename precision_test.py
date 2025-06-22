#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from inference_engine import diagnose_input

def test_precision_comparison():
    print("🎯 COMPARACIÓN DE PRECISIÓN: FORMULARIO GUIADO vs CHAT LIBRE")
    print("=" * 70)
    
    # Caso 1: Múltiples problemas (caso del usuario)
    print("\n🔍 CASO 1: MÚLTIPLES PROBLEMAS")
    print("-" * 40)
    
    user_text_1 = "Mi carro no está frenando bien, creo que necesita unas pastillas para los frenos, pero también, al motor le hace falta fuerza para subir colinas y vibra mucho al acelerar"
    
    # Simular formulario guiado (solo frenos)
    form_text_1 = "Problema en frenos: no frena bien. Síntomas: pedal suave, chirrido"
    
    form_result_1 = diagnose_input(form_text_1)
    chat_result_1 = diagnose_input(user_text_1)
    
    print(f"📋 Formulario: {form_result_1['puntuación']} pts, {form_result_1['categorías']}")
    print(f"💬 Chat libre: {chat_result_1['puntuación']} pts, {chat_result_1['categorías']}")
    
    # Caso 2: Problema específico
    print("\n🔍 CASO 2: PROBLEMA ESPECÍFICO")
    print("-" * 40)
    
    user_text_2 = "El motor hace un ruido extraño cuando acelero"
    
    # Simular formulario guiado (motor específico)
    form_text_2 = "Problema en motor: ruido extraño. Síntomas: ruido al acelerar"
    
    form_result_2 = diagnose_input(form_text_2)
    chat_result_2 = diagnose_input(user_text_2)
    
    print(f"📋 Formulario: {form_result_2['puntuación']} pts, {form_result_2['categorías']}")
    print(f"💬 Chat libre: {chat_result_2['puntuación']} pts, {chat_result_2['categorías']}")
    
    # Caso 3: Texto vago
    print("\n🔍 CASO 3: TEXTO VAGO")
    print("-" * 40)
    
    user_text_3 = "Mi carro no funciona bien"
    
    # Simular formulario guiado (sin información específica)
    form_text_3 = "Problema general: no funciona bien"
    
    form_result_3 = diagnose_input(form_text_3)
    chat_result_3 = diagnose_input(user_text_3)
    
    print(f"📋 Formulario: {form_result_3['puntuación']} pts, {form_result_3['categorías']}")
    print(f"💬 Chat libre: {chat_result_3['puntuación']} pts, {chat_result_3['categorías']}")
    
    # Análisis final
    print("\n📊 ANÁLISIS FINAL:")
    print("-" * 40)
    
    # Calcular promedios
    form_scores = [form_result_1['puntuación'], form_result_2['puntuación'], form_result_3['puntuación']]
    chat_scores = [chat_result_1['puntuación'], chat_result_2['puntuación'], chat_result_3['puntuación']]
    
    form_avg = sum(form_scores) / len(form_scores)
    chat_avg = sum(chat_scores) / len(chat_scores)
    
    print(f"📋 Formulario promedio: {form_avg:.1f} puntos")
    print(f"💬 Chat libre promedio: {chat_avg:.1f} puntos")
    
    # Contar categorías detectadas
    form_categories = len(set(form_result_1['categorías'] + form_result_2['categorías'] + form_result_3['categorías']))
    chat_categories = len(set(chat_result_1['categorías'] + chat_result_2['categorías'] + chat_result_3['categorías']))
    
    print(f"📋 Formulario categorías únicas: {form_categories}")
    print(f"💬 Chat libre categorías únicas: {chat_categories}")
    
    # Conclusión final
    print(f"\n🏆 CONCLUSIÓN FINAL:")
    print("-" * 40)
    
    if chat_avg > form_avg:
        print("   🥇 CHAT LIBRE es más preciso en general")
        print("   💡 Razones:")
        print("      • Detecta múltiples problemas simultáneamente")
        print("      • Mejor cobertura de categorías")
        print("      • Más flexible con diferentes formas de expresar problemas")
    elif form_avg > chat_avg:
        print("   🥇 FORMULARIO GUIADO es más preciso en general")
        print("   💡 Razones:")
        print("      • Información más estructurada")
        print("      • Menos ambigüedad")
        print("      • Mejor para problemas específicos")
    else:
        print("   🤝 AMBOS tienen precisión similar")
    
    print(f"\n📋 RECOMENDACIÓN DE USO:")
    print("-" * 40)
    print("🛑 FORMULARIO GUIADO: Para usuarios que saben exactamente qué problema tienen")
    print("💬 CHAT LIBRE: Para usuarios que quieren describir múltiples problemas o no están seguros")

if __name__ == "__main__":
    test_precision_comparison() 