import streamlit as st

# Configura el título de la página
st.set_page_config(page_title="Nutrix AI", page_icon=":shallow_pan_of_food:", layout="wide")

# CSS para personalizar los colores y tipografías
st.markdown("""
<style>
.main {
    background-color: #F0F2F6;
}
.sidebar .sidebar-content {
    background-image: linear-gradient(#FFC107,#FFC107);
}
.button {
    background-color: #4CAF50;
    color: white;
    padding: 0.25em 0.5em;
    border: none;
    border-radius: 0.3em;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("path_to_logo.png", width=100)  # Asegúrate de tener un logo en la ruta especificada
    st.title("Nutrix AI")
    menu = ["Inicio", "Evaluación corporal peso", "Carga tus medidas de hoy", "Mi perfil"]
    choice = st.sidebar.selectbox("Menú", menu)

# Contenido principal de la página
st.header("Tu información Nutricional en un solo lugar")

# Atajos (botones)
col1, col2, col3 = st.columns(3)
with col1:
    st.button("Mejores hábitos")

with col2:
    st.button("Cargá tu peso")

with col3:
    st.button("Nutrix IA")

# Seguimiento de comidas
st.subheader("Seguí tus comidas:")
col_desayuno, col_almuerzo, col_cena = st.columns(3)
with col_desayuno:
    st.button("Añadir desayuno")

with col_almuerzo:
    st.button("Añadir almuerzo")

with col_cena:
    st.button("Añadir cena")

# Sección de peso corporal
st.subheader("Body weight")
# Aquí podrías añadir un widget para ingresar el peso

# Código para las otras páginas, cada una activada por el menú
if choice == "Evaluación corporal peso":
    st.write("Aquí va el contenido de la Evaluación corporal peso")

elif choice == "Carga tus medidas de hoy":
    st.write("Aquí va el contenido de Carga tus medidas de hoy")

elif choice == "Mi perfil":
    st.write("Aquí va el contenido de Mi perfil")

