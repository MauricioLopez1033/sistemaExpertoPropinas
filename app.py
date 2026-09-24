import streamlit as st
from motorDifusoNativo import evaluarSistemaExpertoPropina
from conexionBD import guardarEvaluacionNube, obtenerHistorialNube

st.set_page_config(page_title="Sistema Experto de Propinas", page_icon="🍽️", layout="centered")

st.title("🍽️ Sistema Experto Difuso de Cálculo de Propinas")
st.markdown("Sistema de inferencia difusa basado en la evaluación de la comida y el servicio.")

st.divider()

columnaUno, columnaDos = st.columns(2)

with columnaUno:
    calidadComida = st.slider("Calidad de la Comida (0 a 10):", min_value=0.0, max_value=10.0, value=7.0, step=0.5)

with columnaDos:
    calidadServicio = st.slider("Calidad del Servicio (0 a 10):", min_value=0.0, max_value=10.0, value=8.0, step=0.5)

if st.button("Calcular Propina con IA", type="primary", use_container_width=True):
    porcentajePropina, nivelPropina = evaluarSistemaExpertoPropina(calidadComida, calidadServicio)

    st.success(f"### Propina Sugerida: {porcentajePropina}% ({nivelPropina})")

    exitoGuardado, mensajeError = guardarEvaluacionNube(calidadComida, calidadServicio, porcentajePropina, nivelPropina)
    if exitoGuardado:
        st.toast("✅ Registro guardado en Supabase (Nube)", icon="☁️")
    else:
        st.warning(f"No se pudo guardar en la nube: {mensajeError}")

st.divider()

st.subheader("📊 Historial de Registros en la Nube")
if st.button("Cargar Registros de la BD Remota"):
    listaRegistros = obtenerHistorialNube()
    if listaRegistros:
        st.dataframe(listaRegistros, use_container_width=True)  
    else:
        st.info("No hay registros en la base de datos.")