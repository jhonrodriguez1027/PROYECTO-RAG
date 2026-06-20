#!/usr/bin/env python3
"""
examples.py
Ejemplos de cómo usar la API del chatbot desde Python.
"""

import requests
import json
import time

# URL base de la aplicación
BASE_URL = "http://localhost:5000"

def ejemplo_1_informacion():
    """Ejemplo 1: Obtener información del asistente"""
    print("\n" + "="*60)
    print("EJEMPLO 1: Obtener información del asistente")
    print("="*60)
    
    try:
        respuesta = requests.get(f"{BASE_URL}/api/info")
        datos = respuesta.json()
        
        print(f"\n✅ Información del asistente:")
        print(f"   Nombre: {datos['nombre']}")
        print(f"   Rol: {datos['rol']}")
        print(f"   Embeddings: {'Locales' if datos['embeddings_locales'] else 'Google'}")
        print(f"   Modelo: {datos['modelo_embedding']}")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def ejemplo_2_hacer_pregunta(pregunta):
    """Ejemplo 2: Hacer una pregunta al chatbot"""
    print("\n" + "="*60)
    print("EJEMPLO 2: Hacer una pregunta")
    print("="*60)
    
    try:
        print(f"\n❓ Pregunta: {pregunta}")
        
        # Hacer petición POST
        respuesta = requests.post(
            f"{BASE_URL}/api/chat",
            json={"mensaje": pregunta}
        )
        
        if respuesta.status_code == 200:
            datos = respuesta.json()
            print(f"\n✅ Respuesta del asistente:")
            print(f"\n{datos['respuesta']}")
            print(f"\n📊 Documentos consultados: {datos['documentos_consultados']}")
            return True
        else:
            error = respuesta.json()
            print(f"❌ Error: {error['error']}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def ejemplo_3_conversacion():
    """Ejemplo 3: Mantener una conversación"""
    print("\n" + "="*60)
    print("EJEMPLO 3: Conversación con múltiples preguntas")
    print("="*60)
    
    preguntas = [
        "¿Cuál es el objeto del RETIE?",
        "¿Qué es la puesta a tierra?",
        "¿Cuáles son los requisitos de seguridad?",
    ]
    
    for i, pregunta in enumerate(preguntas, 1):
        print(f"\n[Turno {i}]")
        ejemplo_2_hacer_pregunta(pregunta)
        time.sleep(1)  # Pequeña pausa entre preguntas
    
    return True

def ejemplo_4_estado():
    """Ejemplo 4: Verificar estado de la aplicación"""
    print("\n" + "="*60)
    print("EJEMPLO 4: Estado de la aplicación")
    print("="*60)
    
    try:
        respuesta = requests.get(f"{BASE_URL}/api/estado")
        datos = respuesta.json()
        
        print(f"\n✅ Estado de la aplicación:")
        print(f"   Estado: {datos['estado']}")
        print(f"   Asistente: {datos['asistente']}")
        print(f"   Rol: {datos['rol'][:50]}...")
        print(f"   Mensajes en histórico: {datos['mensajes_en_historico']}")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def ejemplo_5_limpiar_chat():
    """Ejemplo 5: Limpiar el histórico de chat"""
    print("\n" + "="*60)
    print("EJEMPLO 5: Limpiar histórico")
    print("="*60)
    
    try:
        respuesta = requests.post(f"{BASE_URL}/api/limpiar-chat")
        datos = respuesta.json()
        
        print(f"\n✅ {datos['estado']}")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Ejecuta los ejemplos"""
    print("\n" + "#"*60)
    print("# 🤖 EJEMPLOS DE USO - CHATBOT RAG API")
    print("#"*60)
    print("\n⚠️  Asegúrate de que la aplicación está ejecutándose:")
    print("   python app.py")
    
    time.sleep(2)
    
    # Ejecutar ejemplos
    ejemplos_exitosos = 0
    
    if ejemplo_1_informacion():
        ejemplos_exitosos += 1
    
    if ejemplo_4_estado():
        ejemplos_exitosos += 1
    
    if ejemplo_2_hacer_pregunta("¿Qué es el RETIE?"):
        ejemplos_exitosos += 1
    
    if ejemplo_3_conversacion():
        ejemplos_exitosos += 1
    
    if ejemplo_5_limpiar_chat():
        ejemplos_exitosos += 1
    
    # Resumen
    print("\n" + "#"*60)
    print(f"# Ejemplos completados: {ejemplos_exitosos}/5")
    print("#"*60 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Ejemplos interrumpidos por el usuario")
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: No se pudo conectar con el servidor")
        print("   Asegúrate de ejecutar: python app.py")
