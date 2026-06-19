"""
chat.py
Bucle conversacional del asistente RAG.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "LLM")
    )
)
import config

# Importar el embedder adecuado según configuración
if config.USE_LOCAL_EMBEDDINGS:
    from langchain_huggingface import HuggingFaceEmbeddings
else:
    from langchain_google_genai import GoogleGenerativeAIEmbeddings

def crear_embeddings():
    """Crea el objeto de embeddings según configuración"""
    if config.USE_LOCAL_EMBEDDINGS:
        print(f"Usando embeddings locales: {config.LOCAL_EMBEDDING_MODEL}")
        return HuggingFaceEmbeddings(
            model_name=config.LOCAL_EMBEDDING_MODEL,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
    else:
        print(f"Usando embeddings Gemini: {config.EMBEDDING_MODEL}")
        return GoogleGenerativeAIEmbeddings(
            model=config.EMBEDDING_MODEL,
            api_key=config.GOOGLE_API_KEY,
        )

def cargar_vector_store():
    embeddings = crear_embeddings()
    return Chroma(
        persist_directory=config.PERSIST_DIRECTORY,
        embedding_function=embeddings,
    )

def recuperar_contexto(vector_store, pregunta: str):
    # Usar MMR para mejor diversidad en los resultados
    retriever = vector_store.as_retriever(
        search_type="mmr",  # Maximum Marginal Relevance
        search_kwargs={
            "k": config.TOP_K,
            "fetch_k": 20,  # Trae 20 candidatos
            "lambda_mult": 0.7  # Balance entre relevancia (1) y diversidad (0)
        }
    )
    return retriever.invoke(pregunta)

def construir_contexto(documentos) -> str:
    return "\n\n--\n\n".join(
        f"[Fragmento {i + 1} - Pág. {doc.metadata.get('page', '?')}]\n{doc.page_content}"
        for i, doc in enumerate(documentos)
    )

def extraer_paginas(documentos) -> str:
    paginas = sorted({
        (doc.metadata.get("page", -1) + 1)
        for doc in documentos
        if doc.metadata.get("page") is not None
    })
    return ", ".join(str(p) for p in paginas) if paginas else "N/A"

def construir_prompt(pregunta: str, contexto: str):
    template = ChatPromptTemplate.from_template(config.PROMPT_TEMPLATE)
    return template.invoke({
        "nombre": config.ASSISTANT_NAME,
        "rol": config.ASSISTANT_ROLE,
        "contexto": contexto,
        "pregunta": pregunta,
    })

def texto_de_respuesta(respuesta) -> str:
    """Normaliza la respuesta del LLM a un string plano."""
    contenido = respuesta.content
    if isinstance(contenido, str):
        return contenido
    if isinstance(contenido, list):
        return "".join(
            bloque.get("text", "") for bloque in contenido if isinstance(bloque, dict)
        )
    return str(contenido)

def preguntar(vector_store, llm, pregunta: str):
    # Primero, intentar búsqueda directa
    documentos = recuperar_contexto(vector_store, pregunta)
    
    # Si no encuentra nada relevante, intentar con consulta mejorada
    if not documentos or len(documentos) < 2:
        print("🔍 Intentando búsqueda optimizada...")
        try:
            # Crear un query enhancer solo para reformular
            enhancer = ChatGoogleGenerativeAI(
                model=config.LLM_MODEL,
                temperature=0.1,
                api_key=config.GOOGLE_API_KEY,
            )
            
            enhance_prompt = f"""
            Reformula esta pregunta para búsqueda en un documento técnico legal (RETIE).
            Usa términos clave del reglamento.
            
            Pregunta original: {pregunta}
            
            Consulta optimizada (máximo 10 palabras):
            """
            
            enhanced_query = enhancer.invoke(enhance_prompt).content.strip()
            print(f"📝 Consulta mejorada: {enhanced_query}")
            
            # Hacer segunda búsqueda con la consulta mejorada
            documentos_mejorados = recuperar_contexto(vector_store, enhanced_query)
            
            # Combinar resultados (evitar duplicados por página)
            paginas_vistas = set()
            documentos_finales = []
            
            for doc in documentos + documentos_mejorados:
                pagina = doc.metadata.get('page')
                if pagina not in paginas_vistas:
                    paginas_vistas.add(pagina)
                    documentos_finales.append(doc)
            
            documentos = documentos_finales[:config.TOP_K]
            
        except Exception as e:
            print(f"⚠️ Error en búsqueda mejorada: {e}")
            # Si falla, usar los resultados originales
            pass
    
    contexto = construir_contexto(documentos)
    prompt = construir_prompt(pregunta, contexto)
    respuesta = llm.invoke(prompt)
    
    return texto_de_respuesta(respuesta), extraer_paginas(documentos)

def main():
    if not config.GOOGLE_API_KEY:
        raise RuntimeError(
            "No se encontró GOOGLE_API_KEY. Revisa tu archivo .env."
        )

    print(f"=== {config.ASSISTANT_NAME} ===")
    print(f"{config.ASSISTANT_ROLE}")
    print("Escribe tu pregunta (o 'salir' para terminar)\n")

    vector_store = cargar_vector_store()
    llm = ChatGoogleGenerativeAI(
        model=config.LLM_MODEL,
        temperature=config.LLM_TEMPERATURE,
        api_key=config.GOOGLE_API_KEY,
    )

    while True:
        pregunta = input("Tú: ").strip()

        if pregunta.lower() in ("salir", "exit", "quit"):
            print(f"\n{config.ASSISTANT_NAME}: ¡Hasta luego!")
            break

        if not pregunta:
            continue

        respuesta, paginas = preguntar(vector_store, llm, pregunta)
        print(f"\n{config.ASSISTANT_NAME}: {respuesta}")
        print(f"(Páginas consultadas: {paginas})\n")

if __name__ == "__main__":
    main()