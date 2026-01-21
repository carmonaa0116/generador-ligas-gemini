# ======================================================
# Generador de ligas con Gemini (google-genai)
# Interfaz creada con Gradio (Dark UI compatible)
# ======================================================

import os
import gradio as gr
from google import genai
from google.genai import types
from dotenv import load_dotenv


# ------------------------------------------------------
# Configuración inicial
# ------------------------------------------------------

load_dotenv(override=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"

client = genai.Client(api_key=GEMINI_API_KEY)


# ------------------------------------------------------
# Prompt del sistema
# ------------------------------------------------------

system_instruction = """
Eres un asistente que crea ligas deportivas o de videojuegos a partir de la información
que proporciona el usuario en un único mensaje.

Cada solicitud es independiente y no debes asumir contexto previo.

Tu respuesta debe incluir siempre:
- Nombre de la liga
- Deporte o videojuego
- Número de equipos o jugadores
- Formato de competición
- Calendario o enfrentamientos resumidos
- Reglas básicas de puntuación

Si el usuario solo proporciona nombres, utilízalos como participantes y completa
el resto de la información de forma coherente.
Si faltan datos, rellénalos con opciones razonables.
La respuesta debe ser clara, ordenada y fácil de leer.
"""


# ------------------------------------------------------
# Función principal de generación
# ------------------------------------------------------

def message_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.9,
                max_output_tokens=2048
            )
        )
        return response.text
    except Exception as e:
        return str(e)


# ------------------------------------------------------
# Estilos personalizados (Dark UI)
# ------------------------------------------------------

custom_css = """
body {
    background-color: #1e1b4b;
    color: #e0e7ff;
}

.gradio-container {
    background: linear-gradient(135deg, #1e1b4b 0%, #581c87 50%, #1e1b4b 100%);
    font-family: 'Segoe UI', system-ui, sans-serif;
}

.header-container {
    text-align: center;
    padding: 2rem 1rem;
    background: linear-gradient(90deg, #fbbf24, #ec4899, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.generate-btn {
    background: linear-gradient(90deg, #06b6d4, #a855f7) !important;
    color: white !important;
    font-weight: 600;
    padding: 1rem 2rem;
    border-radius: 12px;
    border: none;
    cursor: pointer;
}

.output-box {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(10px);
    border: 2px solid rgba(168, 85, 247, 0.4);
    border-radius: 16px;
    padding: 1.5rem;
}
"""


# ------------------------------------------------------
# Ejemplos de entrada
# ------------------------------------------------------

examples = [
    ["Dragones, Tigres, Halcones, Lobos"],
    ["Liga de baloncesto con 12 equipos"],
    ["Torneo de ajedrez para 6 jugadores"],
    ["Real Madrid, Barcelona, Bayern, PSG"],
    ["Crea una liga de Valorant con 10 equipos"],
    ["Liga de fútbol con 8 equipos"],
    ["Torneo de tenis para 4 jugadores"],
    ["Liga de hockey sobre hielo con 6 equipos"],
    ["Crea una liga de baloncesto femenino con 10 equipos"],
    ["Torneo de voleibol para 8 equipos"]
]


# ------------------------------------------------------
# Interfaz Gradio
# ------------------------------------------------------

with gr.Blocks(theme=gr.themes.Soft(), css=custom_css) as demo:

    gr.HTML("""
        <div class="header-container">
            <h1 style="font-size: 3rem; margin: 0;">Generador de Ligas</h1>
            <p style="font-size: 1.2rem; color: #c4b5fd;">
                Crea ligas deportivas o de videojuegos a partir de una simple descripción
            </p>
        </div>
    """)

    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="Describe la liga o escribe los participantes",
                placeholder="Ejemplo: Dragones, Tigres, Halcones, Lobos",
                lines=6
            )

            generate_btn = gr.Button(
                "Generar liga",
                elem_classes="generate-btn"
            )

            gr.Examples(
                examples=examples,
                inputs=input_text
            )

        with gr.Column():
            output_text = gr.Markdown(
                label="Resultado",
                elem_classes="output-box"
            )

    generate_btn.click(
        fn=message_gemini,
        inputs=input_text,
        outputs=output_text
    )

    input_text.submit(
        fn=message_gemini,
        inputs=input_text,
        outputs=output_text
    )


# ------------------------------------------------------
# Lanzamiento
# ------------------------------------------------------

if __name__ == "__main__":
    demo.launch(
        share=True,
        inbrowser=True,
        server_name="localhost",
        show_error=True
    )
