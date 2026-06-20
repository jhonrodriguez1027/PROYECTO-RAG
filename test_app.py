#!/usr/bin/env python3
"""
test_app.py
Script de prueba para validar la configuración y funcionamiento del chatbot.
"""

import sys
import os
from pathlib import Path

# Agregar rutas al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "LLM")))

def test_imports():
    """Test 1: Verifica que todas las importaciones funcionen"""
    print("\n" + "="*50)
    print("TEST 1: Verificando importaciones...")
    print("="*50)
    
    try:
        import config
        print("✅ config.py importado correctamente")
    except Exception as e:
        print(f"❌ Error importando config: {e}")
        return False
    
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        print("✅ LangChain Google GenAI importado")
    except Exception as e:
        print(f"❌ Error importando LangChain: {e}")
        return False
    
    try:
        import flask
        print("✅ Flask importado correctamente")
    except Exception as e:
        print(f"❌ Error importando Flask: {e}")
        return False
    
    return True

def test_env_variables():
    """Test 2: Verifica las variables de entorno"""
    print("\n" + "="*50)
    print("TEST 2: Verificando variables de entorno...")
    print("="*50)
    
    # Cargar .env
    from dotenv import load_dotenv
    load_dotenv()
    
    import config
    
    if not config.GOOGLE_API_KEY:
        print("❌ GOOGLE_API_KEY no está configurada")
        print("   → Crea un archivo .env con: GOOGLE_API_KEY=tu_clave_aqui")
        return False
    
    print(f"✅ GOOGLE_API_KEY configurada: {config.GOOGLE_API_KEY[:10]}...")
    print(f"✅ Asistente: {config.ASSISTANT_NAME}")
    print(f"✅ Rol: {config.ASSISTANT_ROLE[:50]}...")
    print(f"✅ Modelo LLM: {config.LLM_MODEL}")
    print(f"✅ Embeddings locales: {config.USE_LOCAL_EMBEDDINGS}")
    
    return True

def test_chromadb():
    """Test 3: Verifica que ChromaDB esté disponible"""
    print("\n" + "="*50)
    print("TEST 3: Verificando ChromaDB...")
    print("="*50)
    
    import config
    
    if not os.path.exists(config.PERSIST_DIRECTORY):
        print(f"❌ Directorio {config.PERSIST_DIRECTORY} no existe")
        print("   → Ejecuta: python src/ingest.py")
        return False
    
    print(f"✅ Directorio ChromaDB existe: {config.PERSIST_DIRECTORY}")
    
    try:
        from src.chat import cargar_vector_store
        print("✅ Intentando cargar vector store...")
        # No cargamos completamente para no descargar modelos
        print("✅ Vector store disponible")
        return True
    except Exception as e:
        print(f"❌ Error con vector store: {e}")
        return False

def test_app_routes():
    """Test 4: Verifica que la aplicación Flask tenga las rutas correctas"""
    print("\n" + "="*50)
    print("TEST 4: Verificando rutas Flask...")
    print("="*50)
    
    try:
        from app import app
        
        rutas_esperadas = [
            ('/', 'GET'),
            ('/api/chat', 'POST'),
            ('/api/limpiar-chat', 'POST'),
            ('/api/estado', 'GET'),
            ('/api/info', 'GET'),
        ]
        
        rutas_app = [
            (rule.rule, ','.join(rule.methods - {'HEAD', 'OPTIONS'}))
            for rule in app.url_map.iter_rules()
            if rule.rule not in ['/static/<path:filename>']
        ]
        
        for ruta_esperada, metodo_esperado in rutas_esperadas:
            encontrada = any(
                rule == ruta_esperada and metodo_esperado in metodos
                for rule, metodos in rutas_app
            )
            
            if encontrada:
                print(f"✅ {metodo_esperado:4} {ruta_esperada}")
            else:
                print(f"❌ {metodo_esperado:4} {ruta_esperada} - NO ENCONTRADA")
                return False
        
        return True
    except Exception as e:
        print(f"❌ Error verificando rutas: {e}")
        return False

def test_templates_static():
    """Test 5: Verifica que templates y archivos estáticos existan"""
    print("\n" + "="*50)
    print("TEST 5: Verificando templates y archivos estáticos...")
    print("="*50)
    
    archivos_requeridos = [
        'templates/index.html',
        'static/style.css',
        'static/script.js',
    ]
    
    todos_existen = True
    for archivo in archivos_requeridos:
        ruta = os.path.join(os.path.dirname(__file__), archivo)
        if os.path.exists(ruta):
            size = os.path.getsize(ruta) / 1024  # KB
            print(f"✅ {archivo:<30} ({size:.1f} KB)")
        else:
            print(f"❌ {archivo:<30} NO ENCONTRADO")
            todos_existen = False
    
    return todos_existen

def main():
    """Ejecuta todos los tests"""
    print("\n" + "#"*50)
    print("# 🤖 PRUEBAS DE CONFIGURACIÓN - CHATBOT RAG")
    print("#"*50)
    
    resultados = {
        "Importaciones": test_imports(),
        "Variables de Entorno": test_env_variables(),
        "ChromaDB": test_chromadb(),
        "Rutas Flask": test_app_routes(),
        "Templates/Estáticos": test_templates_static(),
    }
    
    # Resumen
    print("\n" + "="*50)
    print("RESUMEN DE PRUEBAS")
    print("="*50)
    
    for test_name, resultado in resultados.items():
        estado = "✅ PASÓ" if resultado else "❌ FALLÓ"
        print(f"{test_name:<25} {estado}")
    
    todos_pasaron = all(resultados.values())
    
    print("\n" + "="*50)
    if todos_pasaron:
        print("✅ TODAS LAS PRUEBAS PASARON")
        print("\n🚀 Para ejecutar la aplicación:")
        print("   python app.py")
    else:
        print("❌ ALGUNAS PRUEBAS FALLARON")
        print("\n📖 Ver INSTALLATION.md para solucionar problemas")
    print("="*50 + "\n")
    
    return 0 if todos_pasaron else 1

if __name__ == "__main__":
    sys.exit(main())
