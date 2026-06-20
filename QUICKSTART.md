# ⚡ GUÍA RÁPIDA - Ejecutar el Chatbot

## 🎯 3 Pasos para Comenzar

### PASO 1: Configuración (1 minuto)
```powershell
# Crear archivo .env desde el ejemplo
copy .env.example .env

# ✏️ Editar .env y reemplazar:
# GOOGLE_API_KEY=tu_clave_real_aqui
```

### PASO 2: Instalar (5 minutos)
```powershell
# Activar virtual environment
.\venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt
```

### PASO 3: Ejecutar (1 minuto)
```powershell
# Iniciar servidor
python app.py

# Esperar a ver:
# 🚀 Servidor iniciado en: http://localhost:5000
```

---

## 🌐 Acceder a la Aplicación

1. Abre tu navegador
2. Ve a: **http://localhost:5000**
3. ¡Comienza a chatear! 💬

---

## 📋 Tareas Rápidas

### Validar Configuración
```powershell
python test_app.py
```

### Probar API
```powershell
python examples.py
```

### Preguntas de Ejemplo

```
"¿Cuál es el objeto del RETIE?"
"¿Qué es la puesta a tierra?"
"¿Cuáles son los requisitos de seguridad?"
"¿Cómo se deben instalar los conductores?"
```

---

## 🆘 Si Hay Problemas

| Problema | Solución |
|----------|----------|
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| `GOOGLE_API_KEY not found` | Editar `.env` con tu clave |
| `Connection refused` | Ejecutar `python app.py` primero |
| `Port 5000 already in use` | Cambiar puerto en `app.py` |
| `ChromaDB not found` | Ejecutar `python src/ingest.py` |

---

## 📚 Documentación Completa

```
📖 README.md              ← Descripción general
🚀 INSTALLATION.md        ← Guía detallada
⚡ QUICKSTART.md          ← Este archivo (referencia rápida)
📊 SUMMARY.md             ← Resumen del proyecto
🧪 test_app.py            ← Validación
📚 examples.py            ← Ejemplos de API
```

---

## 🎓 Estructura de la Aplicación

```
Cliente (Navegador)
    ↓↑
    WebSockets
    ↓↑
Servidor Flask (app.py)
    ↓↑
    API REST
    ↓↑
Lógica RAG (src/chat.py)
    ↓↑
    LLM (Google Gemini)
    ChromaDB (Vectores)
```

---

## ✨ Características Principales

🟢 Chat en tiempo real
🟢 Búsqueda de documentos
🟢 Generación de respuestas
🟢 Interfaz responsiva
🟢 API REST completa

---

## 🔗 Rutas Disponibles

| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Página principal |
| `/api/chat` | POST | Enviar pregunta |
| `/api/info` | GET | Info del asistente |
| `/api/estado` | GET | Estado de app |
| `/api/limpiar-chat` | POST | Limpiar histórico |

---

## ⏰ Tiempos Aproximados

- ⏱️ Primer inicio: 5-10 min (descarga modelos)
- ⏱️ Inicios posteriores: 10-20 segundos
- ⏱️ Respuesta por pregunta: 2-5 segundos

---

## 🚀 ¡LISTO!

Ya puedes:
✅ Hacer preguntas sobre el RETIE
✅ Recibir respuestas basadas en documentos
✅ Mantener conversaciones
✅ Consultar información del asistente

```
Visita: http://localhost:5000
```

---

## 💡 Tips

- Usa preguntas específicas para mejores respuestas
- El chat mantiene contexto de conversación anterior
- Limpia el chat entre conversaciones diferentes
- Comprueba la configuración en el panel Información

---

¿Preguntas? Ver **INSTALLATION.md** para guía completa.
