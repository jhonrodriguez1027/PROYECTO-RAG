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
TOP_K = 15

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

Tu tarea es responder preguntas sobre el RETIE basándote ÚNICA Y EXCLUSIVAMENTE en el contexto proporcionado a continuación.

REGLAS IMPORTANTES:
1. Solo usa la información del CONTEXTO
2. Si la respuesta directa no está en el contexto pero hay información relacionada, puedes hacer inferencias lógicas
3. SIEMPRE cita las páginas de donde sacaste la información
4. Si REALMENTE no hay nada relevante en el contexto, dí: "No encontré información específica sobre eso en el RETIE. Las páginas consultadas fueron: [PÁGINAS]"
5. Sé conciso y técnico

CONTEXTO (ÚNICA fuente de información):
{contexto}

Pregunta del usuario: {pregunta}

RESPUESTA (basada en el contexto proporcionado):"""