"""
config.py
Configuración central del asistente RAG.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# =========================================================
# Credenciales
# =========================================================
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# =========================================================
# Rutas
# =========================================================
PDF_PATH = "data/retie.pdf"
PERSIST_DIRECTORY = "./chromadb"

# =========================================================
# Identidad del asistente
# =========================================================
ASSISTANT_NAME = "Volt"
ASSISTANT_ROLE = (
    "asistente técnico especializado en el RETIE "
    "(Reglamento Técnico de Instalaciones Eléctricas de Colombia)"
)

# =========================================================
# Parámetros de chunking
# =========================================================
CHUNK_SIZE = 1500
CHUNK_OVERLAP = 300
SEPARATORS = ["\n\n", "\n", " ", ""]

# =========================================================
# Parámetros de recuperación
# =========================================================
TOP_K = 10

# =========================================================
# Modelos
# =========================================================
# NUEVO: Configuración para embeddings locales
USE_LOCAL_EMBEDDINGS = True  # Cambia a False para usar Gemini
LOCAL_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Modelos de Gemini (solo para el chat)
EMBEDDING_MODEL = "gemini-embedding-001"  # Solo si USE_LOCAL_EMBEDDINGS = False
LLM_MODEL = "gemini-2.5-flash"
LLM_TEMPERATURE = 0.2

# =========================================================
# Plantilla de prompt
# =========================================================
PROMPT_TEMPLATE = """Eres {nombre}, {rol}.

⚠️ REGLA FUNDAMENTAL (NO LA ROMPAS BAJO NINGUNA CIRCUNSTANCIA):
SOLO puedes usar la información del CONTEXTO que se te proporciona.
Si la respuesta NO está en el contexto, DEBES responder:
"No encontré esa información en el documento. ¿Puedes reformular tu pregunta?"

NUNCA:
- Inventes información
- Uses conocimiento previo
- Des respuestas genéricas
- Complementes con información externa

CONTEXTO (ÚNICA fuente de información):
{contexto}

Pregunta del usuario: {pregunta}

RESPUESTA (basada ESTRICTAMENTE en el contexto proporcionado):"""