# 🤖 Guía de Instalación - Chatbot RAG Conversacional

## 📋 Requisitos del Sistema

- **Python**: 3.9 o superior
- **pip**: Gestor de paquetes de Python
- **Virtual Environment**: Recomendado (venv o conda)
- **Espacio en disco**: Mínimo 2GB para dependencias y modelos
- **Conexión a internet**: Para descargar dependencias

## 🔑 Paso 1: Obtener una API Key de Google

1. Ir a: https://makersuite.google.com/app/apikey
2. Hacer clic en "Create API key"
3. Copiar la clave generada
4. Guardarla de forma segura (no compartir)

## 📦 Paso 2: Configurar el Entorno

### 2.1 Crear archivo .env

Copia el archivo `.env.example` a `.env` y reemplaza `tu_api_key_aqui` con tu clave real:

```bash
# En Windows PowerShell
Copy-Item .env.example .env

# En macOS/Linux
cp .env.example .env
```

Edita `.env` y reemplaza:
```
GOOGLE_API_KEY=tu_clave_real_aqui
```

### 2.2 Crear Virtual Environment

```bash
# En Windows
python -m venv venv
.\venv\Scripts\Activate.ps1

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

## 📥 Paso 3: Instalar Dependencias

```bash
# Actualizar pip (recomendado)
pip install --upgrade pip

# Instalar dependencias del proyecto
pip install -r requirements.txt
```

**Nota:** La primera instalación puede tardar 5-10 minutos debido a la descarga de modelos.

## 🚀 Paso 4: Ejecutar la Aplicación

```bash
# Asegúrate de tener el virtual environment activado
python app.py
```

Deberías ver algo como:

```
==================================================
🤖 Chatbot Volt
==================================================
Rol: asistente técnico especializado en el RETIE (Reglamiento Técnico de Instalaciones Eléctricas de Colombia)
Embeddings: Locales

🚀 Servidor iniciado en: http://localhost:5000
==================================================
```

## 🌐 Paso 5: Acceder a la Interfaz Web

1. Abre tu navegador web
2. Ve a: `http://localhost:5000`
3. ¡Comienza a hacer preguntas!

## 🎯 Uso de la Aplicación

### Hacer Preguntas

1. Escribe tu pregunta en el campo de entrada
2. Presiona Enter o haz clic en el botón "Enviar"
3. Espera a que el asistente procese y genere la respuesta
4. La respuesta se mostrará con el número de documentos consultados

### Panel de Información

1. Haz clic en "Información" en el panel lateral
2. Consulta detalles del asistente
3. Verifica la configuración técnica

### Limpiar Conversación

1. Haz clic en "Limpiar chat" en el panel lateral
2. Confirma la acción
3. Empieza una nueva conversación

## 🔧 Configuración Avanzada

### Cambiar el Modelo de Lenguaje

En `LLM/config.py`:

```python
LLM_MODEL = "gemini-2.5-flash"  # Cambia a otro modelo disponible
LLM_TEMPERATURE = 0.2             # Ajusta la creatividad (0-1)
```

### Usar Embeddings de Google

En `LLM/config.py`:

```python
USE_LOCAL_EMBEDDINGS = False      # Usar Google Gemini
EMBEDDING_MODEL = "gemini-embedding-001"
```

### Ajustar Parámetros de Búsqueda

En `LLM/config.py`:

```python
TOP_K = 15                         # Más documentos = respuestas más completas
CHUNK_SIZE = 2000                  # Más grande = más contexto por documento
CHUNK_OVERLAP = 500                # Más overlap = mejor continuidad
```

## 🐛 Solución de Problemas

### Error: "GOOGLE_API_KEY not found"

**Solución:** Asegúrate de que:
1. El archivo `.env` existe en la raíz del proyecto
2. Contiene tu clave API válida: `GOOGLE_API_KEY=...`
3. El archivo no está entre comillas: `GOOGLE_API_KEY="..."` ❌

### Error: "ModuleNotFoundError: No module named..."

**Solución:**
```bash
# Desactiva y reactiva el virtual environment
deactivate
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # macOS/Linux

# Reinstala dependencias
pip install -r requirements.txt
```

### Aplicación lenta en primera ejecución

**Esperado:** La primera ejecución descarga modelos de embeddings (~300MB)
**Solución:** Espera a que se complete, luego será más rápida

### Error de conexión: "Connection refused"

**Solución:**
1. Asegúrate de que no hay otra aplicación en puerto 5000
2. Cambia el puerto en `app.py`: `app.run(port=5001)`

### ChromaDB no cargado

**Solución:**
1. Asegúrate de que exista el directorio `chromadb/`
2. Verifica que el archivo `data/retie.pdf` existe
3. Ejecuta `python src/ingest.py` para reinicializar

## 📊 Estructura de Carpetas Después de Instalar

```
Proyecto/
├── venv/                          # Virtual environment
├── chromadb/                      # Base de datos vectorial
├── data/
│   └── retie.pdf                  # Documento fuente
├── LLM/
│   └── config.py                  # Configuración
├── src/
│   ├── chat.py                    # Lógica RAG
│   └── ingest.py                  # Ingesta de documentos
├── static/
│   ├── style.css                  # Estilos
│   └── script.js                  # JavaScript del cliente
├── templates/
│   └── index.html                 # HTML de la interfaz
├── app.py                         # Servidor Flask
├── .env                           # Variables de entorno (no compartir)
├── .env.example                   # Plantilla de .env
├── requirements.txt               # Dependencias
└── README.md                      # Este archivo
```

## 🔐 Seguridad

⚠️ **IMPORTANTE:**
- **NUNCA** compartas tu archivo `.env`
- **NUNCA** hagas commit de `.env` en Git
- Usa `.env.example` para documentar qué variables necesitas
- Rota tus API keys regularmente

Agrega a `.gitignore`:
```
.env
venv/
__pycache__/
*.pyc
chromadb/
```

## 📞 Soporte y Recursos

- **Documentación de LangChain**: https://python.langchain.com
- **Google Generative AI**: https://ai.google.dev
- **ChromaDB**: https://docs.trychroma.com
- **Flask**: https://flask.palletsprojects.com

## ✅ Checklist Final

- [ ] Python 3.9+ instalado
- [ ] Virtual environment creado y activado
- [ ] `.env` configurado con API key válida
- [ ] Dependencias instaladas: `pip install -r requirements.txt`
- [ ] Aplicación ejecutándose: `python app.py`
- [ ] Navegador accediendo a `http://localhost:5000`
- [ ] Preguntas respondidas correctamente

¡Listo para usar tu chatbot RAG! 🚀
