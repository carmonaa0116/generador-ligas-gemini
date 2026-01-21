# 🏆 Generador de Ligas con Gemini AI

Una aplicación web moderna que **genera ligas deportivas y de videojuegos** usando inteligencia artificial (Gemini) y una interfaz visual atractiva con Gradio.

## ✨ Características

- 🤖 **IA Avanzada**: Usa Google Gemini 2.5 Flash para crear ligas realistas
- 🎨 **Interfaz Moderna**: Dark mode con tema personalizado y animaciones
- ⚡ **Rápido**: Respuestas instantáneas con configuración optimizada
- 📱 **Responsive**: Compatible con escritorio y dispositivos móviles
- 🎯 **Flexible**: Genera ligas a partir de nombres, descripciones o requisitos
- 📚 **Ejemplos Incluidos**: 10 ejemplos predefinidos para probar

## 📋 Descripción Detallada

### ¿Qué hace?

La aplicación permite crear ligas deportivas o de videojuegos completas en segundos. Solo necesitas:

**Ejemplos de entrada:**
- `Dragones, Tigres, Halcones, Lobos`
- `Liga de baloncesto con 12 equipos`
- `Torneo de ajedrez para 6 jugadores`
- `Crea una liga de Valorant con 10 equipos`

**Lo que genera:**
- ✅ Nombre de la liga
- ✅ Deporte o videojuego
- ✅ Número de equipos/jugadores
- ✅ Formato de competición
- ✅ Calendario de enfrentamientos
- ✅ Reglas de puntuación

---

## 🚀 Instalación

### Requisitos Previos

- **Python 3.8+** instalado en tu sistema
- **pip** (gestor de paquetes de Python)
- **Google Gemini API Key** (gratuita)

### Paso 1: Clonar o Descargar el Proyecto

```bash
# Con Git (recomendado)
git clone https://github.com/tu-usuario/generador-ligas-gemini.git
cd generador-ligas-gemini

# O descarga el ZIP desde GitHub y descomprime
```

### Paso 2: Crear Entorno Virtual

```powershell
# En Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

**Paquetes que se instalarán:**
- `google-genai` - Cliente de Google Gemini
- `gradio` - Framework para interfaz web
- `python-dotenv` - Gestión de variables de entorno
- `requests` - Cliente HTTP

### Paso 4: Configurar API Key de Gemini

#### Obtener tu API Key:

1. Ve a [Google AI Studio](https://ai.google.dev)
2. Haz clic en "Get API Key"
3. Selecciona o crea un proyecto
4. Copia la API Key generada

#### Crear archivo `.env`:

1. En la carpeta del proyecto, copia el archivo `.env.example`:
   ```powershell
   Copy-Item .env.example .env
   ```

2. Abre `.env` y reemplaza:
   ```env
   GEMINI_API_KEY=tu_api_key_aqui
   ```
   
   Con tu clave real:
   ```env
   GEMINI_API_KEY=AIzaSyDxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

3. **Guarda el archivo** (Ctrl+S)

#### Verificar configuración:

```powershell
python test_env.py
```

Deberías ver:
```
API KEY = AIzaSyDxxxxxxxxxxxxxxxxxxxxxxxxxxx
TIPO = <class 'str'>
LONGITUD = 39
STATUS = 200
RESPUESTA = {"models": [...]}
```

---

## 💻 Uso

### Ejecutar la Aplicación

```powershell
python interfaz_gemini_chat.py
```

### En tu navegador:

La aplicación abrirá automáticamente en: `http://localhost:7860`

### Cómo usar:

1. **En el cuadro de texto**, describe tu liga o escribe participantes
2. **Haz clic** en "Generar liga" o presiona Enter
3. **Espera** la respuesta de IA (2-5 segundos)
4. **Lee** la liga generada en el panel derecho
5. **Intenta** con otros ejemplos o descrippciones personalizadas

### Ejemplos rápidos:

```
✅ "Real Madrid, Barcelona, Bayern, PSG"
✅ "Torneo de tenis para 4 jugadores"
✅ "Liga de hockey sobre hielo con 6 equipos"
✅ "Crea una liga de Valorant con 10 equipos"
✅ "Competencia de ajedrez, 8 participantes"
```

---

## 📁 Estructura del Proyecto

```
generador-ligas-gemini/
│
├── interfaz_gemini_chat.py          ⭐ Archivo principal
│   └── App web completa con UI
│
├── instalacion_configuracion.py     📖 Guía de instalación
│   └── Documentación del setup
│
├── interfaz_basica_shout.py         📚 Ejemplo básico
│   └── Para aprender Gradio
│
├── test_env.py                      🧪 Script de prueba
│   └── Verifica conexión con API
│
├── requirements.txt                 📦 Dependencias
├── .env.example                     🔐 Template de configuración
├── .gitignore                       🚫 Archivos ignorados
├── README.md                        📘 Este archivo
├── GITHUB_SETUP.md                  🔧 Guía para GitHub
│
└── venv/                            (creado automáticamente)
    └── Entorno virtual Python
```

---

## 🛠️ Personalización

### Cambiar el Prompt del Sistema

Abre `interfaz_gemini_chat.py` y modifica la sección:

```python
system_instruction = """
Eres un asistente que crea ligas...
# Tu prompt personalizado aquí
"""
```

### Cambiar Tema/Colores

Modifica la sección `custom_css`:

```python
custom_css = """
body {
    background-color: #tu_color_aqui;
    ...
}
"""
```

### Agregar Más Ejemplos

En la lista `examples`:

```python
examples = [
    ["Tu ejemplo aquí"],
    ["Otro ejemplo"],
    # Agrega más
]
```

### Cambiar Modelo de IA

Busca `MODEL_NAME` y cámbialo:

```python
MODEL_NAME = "gemini-1.5-pro"  # O el modelo que prefieras
```

---

## 🔧 Troubleshooting

### "ModuleNotFoundError: No module named 'gradio'"

```powershell
# Asegúrate de activar el entorno virtual
.\venv\Scripts\Activate.ps1

# Instala dependencias nuevamente
pip install -r requirements.txt
```

### "GEMINI_API_KEY not found"

1. Verifica que existe el archivo `.env`
2. Comprueba que tiene el contenido correcto
3. Reinicia la aplicación después de crear `.env`

### "Connection refused (ConnectionRefusedError)"

- La API Key es inválida
- No tienes conexión a Internet
- El servicio de Gemini está caído

### "Port 7860 is already in use"

```powershell
# Cierra otra instancia de la app o cambia el puerto
# En el código: demo.launch(server_port=7861)
```

---

## 📊 Parámetros de Generación

En `interfaz_gemini_chat.py`, la configuración actual es:

```python
config=types.GenerateContentConfig(
    system_instruction=system_instruction,
    temperature=0.9,              # Creatividad (0-1)
    max_output_tokens=2048        # Límite de respuesta
)
```

- **temperature=0.9**: Más creativo (1=máximo, 0=predecible)
- **max_output_tokens=2048**: Respuestas más largas

---

## 🔐 Seguridad

### Proteger tu API Key:

✅ **Lo correcto:**
- Archivo `.env` en `.gitignore` (NO se sube a GitHub)
- API Key solo en tu máquina local
- Usar variables de entorno

❌ **Lo incorrecto:**
- Pegar API Key en el código
- Subir `.env` a GitHub
- Compartir API Key por email

---

## 🌐 Desplegar Online

Para compartir la app con otros:

### Opción 1: Gradio Share (Rápido)

```python
# En el código, ya está activado:
demo.launch(share=True)
```

Obtendrás un URL público temporal.

### Opción 2: Hugging Face Spaces (Recomendado)

1. Ve a [Hugging Face Spaces](https://huggingface.co/spaces)
2. Crea nuevo Space
3. Carga el código de tu repositorio
4. Configura `.env` como secreto en Settings
5. La app está online automáticamente

### Opción 3: Railway, Replit, Heroku

Servicios de alojamiento que permiten ejecutar Python.

---

## 📝 Licencia

Este proyecto está disponible bajo licencia **MIT** (edita según tus preferencias).

---

## 👨‍💻 Autor

Creado con ❤️ usando:
- **Google Gemini API** para IA
- **Gradio** para la interfaz
- **Python 3.11+**

---

## 🤝 Contribuciones

¿Tienes ideas para mejorar la app?

1. Haz fork del proyecto
2. Crea una rama (`git checkout -b feature/mi-idea`)
3. Haz commit de cambios (`git commit -m "Agrego: descripción"`)
4. Push a la rama (`git push origin feature/mi-idea`)
5. Abre un Pull Request

---

## 📞 Soporte

Si tienes problemas:

1. Verifica la sección **Troubleshooting** arriba
2. Comprueba tu conexión a Internet
3. Valida que tu API Key es correcta
4. Abre un Issue en GitHub

---

## 🚀 Próximas Mejoras (Roadmap)

- [ ] Guardar ligas generadas en base de datos
- [ ] Historial de conversación
- [ ] Exportar ligas a PDF
- [ ] Validación de API Key en interfaz
- [ ] Soporte multi-idioma
- [ ] Modo oscuro/claro automático
- [ ] Tests unitarios completos

---

**¡Gracias por usar Generador de Ligas!** 🏆

Para más información: [Google Gemini Docs](https://ai.google.dev) | [Gradio Docs](https://www.gradio.app)
