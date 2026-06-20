// ============================================
// VARIABLES GLOBALES
// ============================================
let cargando = false;
const areaMensajes = document.getElementById('areaMensajes');
const inputMensaje = document.getElementById('inputMensaje');
const btnEnviar = document.querySelector('.btn-enviar');

// ============================================
// INICIALIZACIÓN
// ============================================
document.addEventListener('DOMContentLoaded', function() {
    cargarInformacionAsistente();
    inputMensaje.focus();
});

// ============================================
// FUNCIONES PRINCIPALES
// ============================================

/**
 * Envía un mensaje al servidor
 */
async function enviarMensaje() {
    const mensaje = inputMensaje.value.trim();
    
    if (!mensaje) {
        mostrarNotificacion('Por favor, escribe un mensaje', 'error');
        return;
    }
    
    if (cargando) {
        return;
    }
    
    // Mostrar mensaje del usuario
    agregarMensaje(mensaje, 'usuario');
    inputMensaje.value = '';
    inputMensaje.focus();
    
    // Mostrar indicador de carga
    cargando = true;
    agregarIndicadorCarga();
    btnEnviar.disabled = true;
    
    try {
        const respuesta = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ mensaje: mensaje })
        });
        
        // Eliminar indicador de carga
        eliminarIndicadorCarga();
        
        if (!respuesta.ok) {
            const error = await respuesta.json();
            throw new Error(error.error || 'Error al procesar el mensaje');
        }
        
        const datos = await respuesta.json();
        
        // Mostrar respuesta del asistente
        agregarMensaje(datos.respuesta, 'asistente');
        
        // Mostrar información de documentos consultados
        if (datos.documentos_consultados > 0) {
            mostrarNotificacion(
                `✓ Consulté ${datos.documentos_consultados} documento(s) relevante(s)`,
                'exito'
            );
        }
        
    } catch (error) {
        eliminarIndicadorCarga();
        console.error('Error:', error);
        agregarMensaje(
            `Lo siento, ocurrió un error: ${error.message}`,
            'error'
        );
    } finally {
        cargando = false;
        btnEnviar.disabled = false;
        inputMensaje.focus();
    }
}

/**
 * Agrega un mensaje a la conversación
 */
function agregarMensaje(contenido, tipo = 'usuario') {
    // Eliminar mensaje de bienvenida si existe
    const bienvenida = document.querySelector('.mensaje-bienvenida');
    if (bienvenida) {
        bienvenida.remove();
    }
    
    const div = document.createElement('div');
    div.className = `mensaje ${tipo}`;
    
    const burbuja = document.createElement('div');
    burbuja.className = 'burbuja-mensaje';
    
    if (tipo === 'error') {
        burbuja.classList.add('error-mensaje');
    }
    
    // Renderizar contenido con soporte básico para markdown
    burbuja.innerHTML = renderizarContenido(contenido);
    
    div.appendChild(burbuja);
    
    // Agregar marca de tiempo
    const marcaTiempo = document.createElement('div');
    marcaTiempo.className = 'marca-tiempo';
    marcaTiempo.textContent = obtenerHora();
    div.appendChild(marcaTiempo);
    
    areaMensajes.appendChild(div);
    
    // Scroll automático al final
    areaMensajes.scrollTop = areaMensajes.scrollHeight;
}

/**
 * Renderiza contenido con soporte para markdown básico
 */
function renderizarContenido(contenido) {
    let html = contenido
        // Escapar caracteres especiales HTML
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
    
    // Negritas: **texto**
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Cursiva: *texto*
    html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');
    
    // Código: `código`
    html = html.replace(/`(.*?)`/g, '<code style="background: rgba(0,0,0,0.2); padding: 2px 6px; border-radius: 3px; font-family: monospace;">$1</code>');
    
    // Links: [texto](url)
    html = html.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" style="color: #818cf8; text-decoration: underline;">$1</a>');
    
    // Saltos de línea
    html = html.replace(/\n/g, '<br>');
    
    return html;
}

/**
 * Agrega indicador de carga
 */
function agregarIndicadorCarga() {
    const div = document.createElement('div');
    div.className = 'mensaje asistente';
    div.id = 'indicador-carga';
    
    const indicador = document.createElement('div');
    indicador.className = 'indicador-carga';
    indicador.innerHTML = `
        <div class="punto-carga"></div>
        <div class="punto-carga"></div>
        <div class="punto-carga"></div>
    `;
    
    div.appendChild(indicador);
    areaMensajes.appendChild(div);
    areaMensajes.scrollTop = areaMensajes.scrollHeight;
}

/**
 * Elimina indicador de carga
 */
function eliminarIndicadorCarga() {
    const indicador = document.getElementById('indicador-carga');
    if (indicador) {
        indicador.remove();
    }
}

/**
 * Limpia el histórico de chat
 */
async function limpiarChat() {
    if (!confirm('¿Estás seguro de que quieres limpiar toda la conversación?')) {
        return;
    }
    
    try {
        await fetch('/api/limpiar-chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        
        // Limpiar UI
        areaMensajes.innerHTML = `
            <div class="mensaje-bienvenida">
                <div class="icono-bienvenida">
                    <i class="fas fa-wave-hand"></i>
                </div>
                <h3>¡Conversación limpiada!</h3>
                <p>Empecemos de nuevo. ¿En qué puedo ayudarte?</p>
            </div>
        `;
        
        inputMensaje.value = '';
        inputMensaje.focus();
        
        mostrarNotificacion('Chat limpiado correctamente', 'exito');
    } catch (error) {
        console.error('Error:', error);
        mostrarNotificacion('Error al limpiar el chat', 'error');
    }
}

/**
 * Cambia entre vistas
 */
function cambiarVista(vista) {
    // Actualizar botones
    document.querySelectorAll('.btn-menu').forEach(btn => {
        btn.classList.remove('activo');
    });
    event.target.closest('.btn-menu').classList.add('activo');
    
    // Actualizar vistas
    document.querySelectorAll('.vista').forEach(v => {
        v.classList.remove('vista-activa');
    });
    document.getElementById(`vista-${vista}`).classList.add('vista-activa');
    
    // Cerrar menú lateral en móvil
    const panelLateral = document.querySelector('.panel-lateral');
    if (window.innerWidth <= 768) {
        panelLateral.classList.remove('activo');
    }
}

/**
 * Toggle del menú lateral en móvil
 */
function toggleMenuLateral() {
    document.querySelector('.panel-lateral').classList.toggle('activo');
}

/**
 * Carga la información del asistente
 */
async function cargarInformacionAsistente() {
    try {
        const respuesta = await fetch('/api/info');
        const datos = await respuesta.json();
        
        document.getElementById('info-nombre').textContent = datos.nombre;
        document.getElementById('info-rol').textContent = datos.rol;
        document.getElementById('info-embeddings').textContent = 
            datos.embeddings_locales ? 'Locales' : 'Google Gemini';
        document.getElementById('info-modelo').textContent = datos.modelo_embedding;
    } catch (error) {
        console.error('Error al cargar información:', error);
    }
}

/**
 * Muestra una notificación
 */
function mostrarNotificacion(mensaje, tipo = 'info') {
    const notificacion = document.createElement('div');
    notificacion.className = `notificacion notificacion-${tipo}`;
    notificacion.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${obtenerColorNotificacion(tipo)};
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        font-size: 14px;
        z-index: 1000;
        animation: slideIn 0.3s ease-out;
        max-width: 300px;
    `;
    notificacion.textContent = mensaje;
    
    document.body.appendChild(notificacion);
    
    setTimeout(() => {
        notificacion.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => notificacion.remove(), 300);
    }, 3000);
}

/**
 * Obtiene color para notificación según tipo
 */
function obtenerColorNotificacion(tipo) {
    const colores = {
        'exito': '#10b981',
        'error': '#ef4444',
        'advertencia': '#f59e0b',
        'info': '#6366f1'
    };
    return colores[tipo] || colores['info'];
}

/**
 * Obtiene la hora actual en formato HH:MM
 */
function obtenerHora() {
    const ahora = new Date();
    return ahora.toLocaleTimeString('es-ES', { 
        hour: '2-digit', 
        minute: '2-digit',
        hour12: false
    });
}

/**
 * Maneja la tecla Enter
 */
function manejarEnter(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        enviarMensaje();
    }
}

// ============================================
// ANIMACIONES CSS DINÁMICAS
// ============================================
const estilosAnimacion = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;

const style = document.createElement('style');
style.textContent = estilosAnimacion;
document.head.appendChild(style);

// ============================================
// EVENTOS
// ============================================
document.addEventListener('DOMContentLoaded', function() {
    // Responder a cambios de tamaño de ventana
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            document.querySelector('.panel-lateral').classList.remove('activo');
        }
    });
});
