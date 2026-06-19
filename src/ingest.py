"""
ingest.py
Fase de ingestión del sistema RAG.
"""

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
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

def cargar_documento(pdf_path: str):
    loader = PyPDFLoader(file_path=pdf_path)
    documentos = loader.load()
    
    # QUITA el límite de 20 páginas para procesar todo el documento
    # documentos = documentos[:20]   # <-- COMENTA O ELIMINA ESTA LÍNEA
    
    print(f"Páginas cargadas: {len(documentos)}")
    return documentos

def dividir_en_chunks(documentos):
    splitter = RecursiveCharacterTextSplitter(
        separators=config.SEPARATORS,
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
    )
    chunks = splitter.split_documents(documentos)
    print(f"Chunks generados: {len(chunks)}")
    
    # Mostrar ejemplo del primer chunk para verificar
    if chunks:
        print(f"\nEjemplo del primer chunk:")
        print(f"Longitud: {len(chunks[0].page_content)} caracteres")
        print(f"Preview: {chunks[0].page_content[:200]}...\n")
    
    return chunks

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

def guardar_en_chroma(chunks):
    embeddings = crear_embeddings()
    
    # Para documentos grandes, guardar en lotes
    batch_size = 100
    total_chunks = len(chunks)
    
    print(f"\nGuardando {total_chunks} chunks en ChromaDB...")
    
    for i in range(0, total_chunks, batch_size):
        batch = chunks[i:i+batch_size]
        if i == 0:
            # Primera vez: crear la base
            vector_store = Chroma.from_documents(
                documents=batch,
                embedding=embeddings,
                persist_directory=config.PERSIST_DIRECTORY,
            )
        else:
            # Añadir a la base existente
            vector_store.add_documents(batch)
        
        progreso = min(i + batch_size, total_chunks)
        print(f"Progreso: {progreso}/{total_chunks} chunks guardados")
    
    total = len(vector_store._collection.get(include=["metadatas"])["metadatas"])
    print(f"\n✅ Total documentos guardados en ChromaDB: {total}")
    return vector_store

def main():
    if not config.GOOGLE_API_KEY:
        raise RuntimeError(
            "No se encontró GOOGLE_API_KEY. Revisa tu archivo .env "
            "(copia .env.example a .env y pega tu key)."
        )

    print("🚀 Iniciando proceso de ingestión...")
    documentos = cargar_documento(config.PDF_PATH)
    chunks = dividir_en_chunks(documentos)
    guardar_en_chroma(chunks)
    print("\n✅ Ingesta completada. Ya puedes ejecutar: python src/chat.py")

if __name__ == "__main__":
    main()