import streamlit as st
from PIL import Image

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="Salito & Pablo 💗",
    page_icon="💕",
    layout="wide"
)

# =========================================================
# ESTILOS
# =========================================================

st.markdown("""
<style>

    /* -------------------- FONDO -------------------- */

    .stApp {
        background: linear-gradient(
            135deg,
            #fff5f7 0%,
            #ffffff 45%,
            #fff0f3 100%
        );
    }

    /* -------------------- CONTENEDOR PRINCIPAL -------------------- */

    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }

    /* -------------------- TITULOS -------------------- */

    h1 {
        color: #c9184a !important;
        text-align: center;
        font-size: 46px !important;
        font-weight: 800 !important;
        margin-bottom: 0.3rem !important;
    }

    h2 {
        color: #a4133c !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #c9184a !important;
        font-weight: 700 !important;
    }

    /* -------------------- TEXTO -------------------- */

    p {
        color: #6d4c55;
        font-size: 16px;
    }

    /* -------------------- TITULO PRINCIPAL -------------------- */

    [data-testid="stTitle"] {
        padding-bottom: 0.5rem;
    }

    /* -------------------- IMAGEN -------------------- */

    [data-testid="stImage"] {
        background: white;
        padding: 12px;
        border-radius: 24px;
        box-shadow: 0 8px 25px rgba(201, 24, 74, 0.12);
    }

    /* -------------------- INPUT -------------------- */

    div[data-baseweb="input"] {
        border-radius: 15px;
        border: 1px solid #f3b6c5;
        background-color: white;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #c9184a;
        box-shadow: 0 0 0 2px rgba(201, 24, 74, 0.12);
    }

    /* -------------------- RADIO Y CHECKBOX -------------------- */

    [data-testid="stCheckbox"] label,
    [data-testid="stRadio"] label {
        color: #6d4c55 !important;
    }

    /* -------------------- TARJETAS DE COLUMNAS -------------------- */

    [data-testid="column"] {
        background: rgba(255, 255, 255, 0.85);
        border: 1px solid #f6cbd5;
        border-radius: 22px;
        padding: 1.5rem;
        box-shadow: 0 8px 25px rgba(201, 24, 74, 0.08);
    }

    /* -------------------- DIVISORES -------------------- */

    hr {
        border: none;
        height: 1px;
        background: linear-gradient(
            to right,
            transparent,
            #f3a6b8,
            transparent
        );
        margin: 2rem 0;
    }

    /* -------------------- ALERTAS -------------------- */

    [data-testid="stAlert"] {
        border-radius: 15px;
        border: 1px solid #f3b6c5;
    }

    /* -------------------- ESPACIO -------------------- */

    .spacer {
        height: 10px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITULO
# =========================================================

st.title("💕 Hola!!, mi nombre es Salito 💕")

st.write("")


# =========================================================
# IMAGEN
# =========================================================

image = Image.open("amoor.jpg")

st.image(
    image,
    caption="🐱💕 Gatitos enamorados 💕🐱"
)


# =========================================================
# PRESENTACIÓN
# =========================================================

st.header("❤️ Página de Salomé y Pablo ❤️")



st.divider()


# =========================================================
# TEXTO
# =========================================================

st.subheader("💌 Déjanos un mensajito")

texto = st.text_input(
    "Aaaaaah!!!! 💗",
    "Este es mi texto"
)

st.write(
    "💬 El texto escrito es:",
    texto
)


st.divider()


# =========================================================
# COLUMNAS
# =========================================================

st.subheader("💞 Ahora usemos 2 columnas")

col1, col2 = st.columns(2)


# =========================================================
# PRIMERA COLUMNA
# =========================================================

with col1:

    st.subheader("💗 Esta es la primera columna")

    st.write(
        "Las interfaces multimodales mejoran "
        "la experiencia de usuario ✨"
    )

    resp = st.checkbox(
        "Estoy de acuerdo 💕"
    )

    if resp:

        st.write(
            "💖 Correcto"
        )


# =========================================================
# SEGUNDA COLUMNA
# =========================================================

with col2:

    st.subheader("🌹 Esta es la segunda columna")

    modo = st.radio(
        "¿Cuál es la modalidad que predomina en tu interfaz?",
        ("Visual", "Auditiva", "Táctil")
    )

    if modo == "Visual":

        st.write(
            "👀 Lo visual es importante para las interfaces"
        )

    if modo == "Auditiva":

        st.write(
            "🎧 La audición es importante para las interfaces"
        )

    if modo == "Táctil":

        st.write(
            "🖐️ Lo táctil es importante para las interfaces"
        )


# =========================================================
# FINAL
# =========================================================

st.divider()

st.caption(
    "💕 Hecho con amor por Salito & Pablo 💕"
)
    
  
