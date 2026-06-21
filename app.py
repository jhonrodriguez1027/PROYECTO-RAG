"""
app.py
Aplicación Flask para el chatbot conversacional RAG.
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sys
import os
from datetime import datetime

# Agregar rutas al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "LLM")))

from src.chat import cargar_vector_store, recuperar_contexto, generar_respuesta
import config

# Inicializar Flask
app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

# Variables globales para caching
vector_store = None
chat_history = []

def inicializar_vector_store():
    """Inicializa el vector store global"""
    global vector_store
    if vector_store is None:
        try:
            vector_store = cargar_vector_store()
            print("✓ Vector store cargado correctamente")
        except Exception as e:
            print(f"✗ Error al cargar vector store: {e}")
            raise

@app.before_request
def antes_de_request():
    """Se ejecuta antes de cada request"""
    global vector_store
    if vector_store is None:
        inicializar_vector_store()

@app.route('/')
def index():
    """Página principal del chatbot"""
    return render_template('index.html', bot_name=config.ASSISTANT_NAME)

@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint para procesar mensajes del usuario"""
    try:
        datos = request.get_json()
        mensaje_usuario = datos.get('mensaje', '').strip()
        
        if not mensaje_usuario:
            return jsonify({'error': 'Mensaje vacío'}), 400
        
        # Limitar longitud del mensaje
        if len(mensaje_usuario) > 1000:
            return jsonify({'error': 'Mensaje muy largo (máximo 1000 caracteres)'}), 400
        
        # Recuperar contexto del vector store
        documentos_relevantes = recuperar_contexto(vector_store, mensaje_usuario)
        
        # Generar respuesta del asistente
        respuesta_asistente = generar_respuesta(
            mensaje_usuario,
            documentos_relevantes,
            chat_history
        )
        
        # Actualizar histórico de chat
        chat_history.append({
            'rol': 'usuario',
            'contenido': mensaje_usuario,
            'timestamp': datetime.now().isoformat()
        })
        chat_history.append({
            'rol': 'asistente',
            'contenido': respuesta_asistente,
            'timestamp': datetime.now().isoformat()
        })
        
        # Mantener solo los últimos 20 mensajes en histórico
        if len(chat_history) > 20:
            chat_history[:] = chat_history[-20:]
        
        return jsonify({
            'respuesta': respuesta_asistente,
            'documentos_consultados': len(documentos_relevantes)
        })
    
    except Exception as e:
        print(f"Error en /api/chat: {e}")
        return jsonify({'error': f'Error al procesar mensaje: {str(e)}'}), 500

@app.route('/api/limpiar-chat', methods=['POST'])
def limpiar_chat():
    """Limpia el histórico de chat"""
    global chat_history
    chat_history = []
    return jsonify({'estado': 'Chat limpiado'})

@app.route('/api/estado', methods=['GET'])
def estado():
    """Retorna el estado de la aplicación"""
    return jsonify({
        'estado': 'activo',
        'asistente': config.ASSISTANT_NAME,
        'rol': config.ASSISTANT_ROLE,
        'mensajes_en_historico': len(chat_history)
    })

@app.route('/api/info', methods=['GET'])
def info():
    """Retorna información del asistente"""
    return jsonify({
        'nombre': config.ASSISTANT_NAME,
        'rol': config.ASSISTANT_ROLE,
        'embeddings_locales': config.USE_LOCAL_EMBEDDINGS,
        'modelo_embedding': config.LOCAL_EMBEDDING_MODEL if config.USE_LOCAL_EMBEDDINGS else config.EMBEDDING_MODEL
    })

@app.errorhandler(404)
def no_encontrado(error):
    """Maneja errores 404"""
    return jsonify({'error': 'Recurso no encontrado'}), 404

@app.errorhandler(500)
def error_interno(error):
    """Maneja errores 500"""
    return jsonify({'error': 'Error interno del servidor'}), 500

if __name__ == '__main__':
    try:
        # Inicializar vector store
        inicializar_vector_store()
        
        # Ejecutar la aplicación
        print(f"\n{'='*50}")
        print(f"🤖 Chatbot {config.ASSISTANT_NAME}")
        print(f"{'='*50}")
        print(f"Rol: {config.ASSISTANT_ROLE}")
        print(f"Embeddings: {'Locales' if config.USE_LOCAL_EMBEDDINGS else 'Google'}")
        print(f"\n🚀 Servidor iniciado en: http://localhost:5000")
        print(f"{'='*50}\n")
        
        app.run(
            debug=True,
            host='0.0.0.0',
            port=5000,
            use_reloader=True
        )
    except Exception as e:
        print(f"\n✗ Error al iniciar la aplicación: {e}")
        sys.exit(1)
