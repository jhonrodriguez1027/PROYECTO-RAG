# Asistente RAG - RETIE (Reglamento Técnico de Instalaciones Eléctricas)

**Estudiante:** jHON SEBASTIAN RODRIGUEZ BENAVIDES
**Fecha:** 20/06/2026

---

## 🚀 Inicio Rápido - Aplicación Web Flask

### Requisitos Previos
- Python 3.9 o superior
- Variable de entorno `GOOGLE_API_KEY` configurada
- Virtual environment activado

### Instalación

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

2. **Ejecutar la aplicación:**
```bash
python app.py
```

3. **Acceder a la interfaz web:**
```
http://localhost:5000
```

### Características de la Aplicación Web

✅ **Interfaz moderna y responsiva** - Diseño adaptable para escritorio, tablet y móvil
✅ **Chat en tiempo real** - Envía preguntas y recibe respuestas instantáneas
✅ **RAG (Retrieval-Augmented Generation)** - Respuestas basadas en documentos relevantes
✅ **Histórico de conversación** - Mantiene el contexto de la conversación
✅ **Panel de información** - Consulta la configuración del asistente
✅ **Búsqueda optimizada** - Encuentra documentos relevantes automáticamente

### Estructura de Archivos

```
proyecto/
├── app.py                    # Aplicación Flask principal
├── requirements.txt          # Dependencias de Python
├── templates/
│   └── index.html           # Página principal (HTML)
├── static/
│   ├── style.css            # Estilos CSS
│   └── script.js            # Lógica del cliente (JavaScript)
├── src/
│   ├── chat.py              # Lógica del chatbot RAG
│   └── ingest.py            # Ingesta de documentos
├── LLM/
│   └── config.py            # Configuración central
├── chromadb/                # Base de datos vectorial
└── data/                    # Documentos de entrada
```

---

## 📄 Documento Seleccionado

**Documento: RETIE — Reglamento Técnico de Instalaciones Eléctricas (Colombia) Categoría: Normas técnicas**
Categoría: Normas técnicas

### Justificación:
El RETIE es el marco normativo fundamental para todas las instalaciones eléctricas en Colombia. Este documento es crítico para:
- Ingenieros electricistas
- Constructores
- Instaladores eléctricos
- Estudiantes de ingeniería

Su complejidad técnica (379 páginas) y su estructura legal lo convierten en un candidato perfecto para un sistema RAG, ya que:
1. Contiene información técnica densa y especializada
2. Es extenso y difícil de consultar manualmente
3. Requiere respuestas precisas respaldadas por el texto legal

---

## 👥 Persona Usuaria y Caso de Uso

**Persona objetivo:** Ingenieros electricistas y técnicos instaladores que necesitan consultar el RETIE durante proyectos de construcción o mantenimiento eléctrico.

**Caso de uso principal:**
> "Un ingeniero electricista está diseñando una instalación eléctrica para un edificio comercial y necesita verificar rápidamente los requisitos de puesta a tierra según el RETIE. En lugar de buscar manualmente en el PDF de 379 páginas, consulta al asistente 'Volt' que le proporciona la información exacta citando las páginas del reglamento."

---

## 🖐️ Cinco Preguntas y Respuestas del Sistema

### Pregunta 1: ¿Cuál es el objeto del RETIE?

Los requisitos y prescripciones técnicas del RETIE son de obligatorio cumplimiento en Colombia para todas las instalaciones eléctricas utilizadas en la generación, transporte, transformación, distribución y uso final de la electricidad. Esto incluye las instalaciones que alimentan equipos para señales de telecomunicaciones, electrodomésticos, vehículos, máquinas, herramientas y demás equipos.

Fuentes: Página(s) 159
(Páginas consultadas: 6, 24, 28, 56, 90, 160, 208, 269, 337, 374)

---

### Pregunta 2: ¿Qué es el RETIE y para qué sirve?

**Volt:** El RETIE son los requisitos y prescripciones técnicas de un Reglamento. Su propósito es ser de obligatorio cumplimiento en Colombia en todas las instalaciones eléctricas utilizadas en la generación, transporte, transformación, distribución y uso final de la electricidad. El Ministerio de Minas y Energía de Colombia es el órgano competente para su elaboración, revisión, actualización, interpretación y modificación.

Fuentes: Página(s) 159, 373
(Páginas consultadas: 23, 24, 28, 56, 160, 175, 208, 269, 271, 374)

---

### Pregunta 3: ¿Cuáles son los requisitos para los conductores eléctricos?

**Volt:** Aquí están los requisitos para los conductores eléctricos, según el contexto proporcionado:

*   Los ensayos y las tolerancias para evaluar los cables y conductores eléctricos deben estar de acuerdo con el referencial normativo con el que fueron diseñados y fabricados. No deben ser evaluados con normas diferentes a las de fabricación.
*   La conexión de los conductores eléctricos a los terminales de los tomacorrientes y clavijas debe ser realizada por una persona competente, garantizando que no se generen calentamientos por malas prácticas.
*   En bandejas portacables, los cables que funcionan a más de 1.000 V deben ser de tipo MC o estar separados de los cables que funcionan a 1.000 V o menos mediante una barrera sólida fija.
*   Cuando los conductores individuales de un circuito de corriente alterna se conecten en paralelo, deben instalarse en grupos de máximo un conductor por fase, neutro o conductor puesto a tierra, y los circuitos deben ser marcados para su identificación.
*   Si los conductores individuales instalados en una bandeja portacables de escalera o fondo ventilada tienen una sección transversal de 53,5 mm² (1/0 AWG) a 107,21 mm² (4/0 AWG), deben instalarse en una sola capa.
*   No deben instalarse conductores eléctricos con tuberías para otros usos no eléctricos (gases, líquidos u otros fluidos) en la misma bandeja portacables.
*   En bandejas portacables o canalizaciones sin encerramiento, solo se deben instalar conductores probados y certificados para ese uso.
*   Las uniones entre conductores deben asegurar el mantenimiento de las características mecánicas y la continuidad eléctrica sin generación de puntos calientes, utilizando métodos de empalme adecuados o uniones con soldadura, borneras o conectores certificados. Si son aislados, el empalme o unión debe mantener el nivel de aislamiento.
*   Los empalmes o uniones solo se permiten en partes accesibles (cajas de empalme, conexión o inspección).
*   Los conductores en una canalización cerrada no deben superar la proporción de área que impida su ventilación natural, ni el número de conductores establecido en la NTC 2050 segunda actualización Capítulo 9 Tabla 1 para tubos y tuberías, ni los artículos 392.20 y 392.22 para bandejas portacables.
*   Los conductores no deben someterse a esfuerzos mecánicos que comprometan el aislamiento, y las canalizaciones u otros elementos no deben someterlos a esfuerzo mecánico.
*   Se debe respetar el radio mínimo de curvatura recomendado por el productor.
*   Los conductores de calibre 8 AWG o mayor deben ser cables; no se acepta alambre de estos calibres.
*   En sistemas aislados de tierra en instituciones de asistencia médica, el conductor aislado Nro. 1 debe ser naranja con al menos una banda de color distintivo (no blanca, verde ni gris), y el conductor separado Nro. 2 debe ser marrón con al menos una banda de color distintivo (no blanca, verde ni gris).
*   Para identificar las fases en sistemas de distribución y transmisión de energía eléctrica, se deben usar las letras A, B y C. Para redes de distribución con conductor de neutro, este se debe identificar con la letra N.

Fuentes: Página(s) 76, 176, 221, 232, 234
(Páginas consultadas: 19, 20, 77, 172, 177, 222, 233, 235, 272, 289)

---

### Pregunta 4: ¿Qué dice el RETIE sobre la puesta a tierra?

**Volt:** El RETIE establece lo siguiente sobre la puesta a tierra:

El requisito de puesta a tierra para instalaciones eléctricas cubre el sistema eléctrico y los apoyos o estructuras metálicas que, ante una sobretensión temporal, puedan desencadenar una falla permanente a frecuencia industrial, entre la estructura puesta a tierra y la red. Su objetivo es evitar que las personas en contacto con la instalación queden sometidas a tensiones de paso, de contacto o transferidas que superen los umbrales de soportabilidad del ser humano cuando se presente una falla.

La puesta a tierra debe instalarse de acuerdo con lo establecido en el Título 12 del Libro 3 o de conformidad con los requisitos de instalación para la puesta a tierra. Con el fin de garantizar la seguridad tanto del personal del operador de red como del público en general, se deben cumplir los requisitos de puesta a tierra que apliquen, establecidos en el Título 12 del presente Libro.

Respecto a las puestas a tierra temporales (Artículo 3.17.25), deben instalarse de acuerdo con los siguientes requisitos:
*   Para garantizar la seguridad del operario, se deben tener en cuenta las "Reglas de oro" indicadas en el artículo 3.15.5 del presente Libro.
*   Se debe atender la guía de instalación, inspección y mantenimiento de la puesta a tierra temporal entregada por el proveedor.
*   El montaje para redes o líneas aéreas debe hacerse de tal manera que los pies del liniero queden al potencial de tierra y que los conductores que se conectan a las líneas tengan la menor longitud e impedancia posible.
*   Cuando la estructura o apoyo tenga su propia puesta a tierra, se conecta a esta.
*   Cuando vaya a "abrirse" un conductor o circuito, se colocarán tierras en ambos lados.
*   Cuando dos o más trabajadores o cuadrillas laboren en lugares distintos de las mismas líneas o equipo, serán responsables de coordinar la colocación y retiro de los equipos de puesta a tierra en sus lugares de trabajo correspondientes.

Fuentes: Página(s) 190, 209, 246, 247, 290
(Páginas consultadas: 12, 14, 191, 206, 210, 247, 248, 269, 291, 327)

---

### Pregunta 5: ¿Quién es responsable de la seguridad en una instalación eléctrica según el RETIE?

**Volt:** Según el RETIE, la responsabilidad de la seguridad en una instalación eléctrica recae en diversas personas y entidades, con roles específicos:

*   **Diseñadores**: Son responsables de verificar que en la etapa pre-constructiva se cumplan requisitos como las distancias de servidumbre y seguridad, y de asegurar que los diseños eléctricos cumplan con todos los requisitos del RETIE.
*   **Constructores**: Deben revisar los diseños eléctricos, asegurar que la instalación resultante cumpla con todos los requisitos del RETIE, informar al diseñador y propietario si los diseños no cumplen.
*   **Operadores**: El responsable de la operación de la instalación eléctrica debe realizar los ajustes requeridos para llevar la instalación a las condiciones reglamentarias cuando se reporta alto riesgo o peligro inminente.
*   **Inspectores**: Pueden ser denunciados e investigados disciplinariamente si violan las distancias de seguridad.
*   **Propietarios**: Tienen responsabilidades establecidas por el RETIE. Si modifican la construcción y violan las distancias mínimas de seguridad, serán objeto de investigación administrativa.
*   **Usuarios**: Tienen responsabilidades establecidas por el RETIE.
*   **Personas competentes**: Son quienes deben dirigir, supervisar y ejecutar el diseño, construcción, ampliación, modificación, remodelación e inspección de toda instalación eléctrica.

En general, el RETIE establece las responsabilidades que deben cumplir los diseñadores, constructores, interventores, operadores, inspectores, propietarios y usuarios de los sistemas e instalaciones eléctricas, además de otros actores, con el fin de minimizar los riesgos de origen eléctrico.

Fuentes: Página(s) 2, 22, 41, 163, 164, 180, 212
(Páginas consultadas: 3, 23, 42, 164, 165, 166, 181, 213, 258, 373)

---

## 🛠️ Instrucciones de Ejecución

### 1. Clonar el repositorio (si es necesario)

```bash
git clone <url-del-repo>
cd proyecto-rag
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar la API key

```bash
cp .env.example .env
```

Edita `.env` y pega tu key de Google AI Studio (https://aistudio.google.com/apikey):

```
GOOGLE_API_KEY=tu_api_key_real
```

### 4. Ejecutar la aplicación web

```bash
python app.py
```

Luego accede a: `http://localhost:5000`

---

## 🎓 Tecnologías Utilizadas

- **Backend**: Flask + Python
- **Frontend**: HTML + CSS + JavaScript
- **LLM**: Google Gemini
- **Embeddings**: Sentence Transformers
- **Vector DB**: ChromaDB
- **Framework**: LangChain

---

## 📝 Archivos Principales

- `app.py` - Servidor Flask
- `templates/index.html` - Interfaz web
- `static/style.css` - Estilos
- `static/script.js` - Lógica del cliente
- `src/chat.py` - Lógica RAG
- `LLM/config.py` - Configuración

---

## 🔐 Seguridad

- **NUNCA** compartas tu archivo `.env`
- Usa `.env.example` como plantilla
- Rota tus API keys regularmente
- Agrega `.env` a `.gitignore`

---

¡El chatbot está listo para usar! 🚀
