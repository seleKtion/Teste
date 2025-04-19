
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Busca Intelbras", layout="wide")

@st.cache_data
def carregar_dados():
    return pd.read_excel("nobreaks_intelbras.xlsx")

df = carregar_dados()

# Cabeçalho
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Intelbras_logo.svg/2560px-Intelbras_logo.svg.png", width=150)
with col2:
    st.title("Catálogo de Nobreaks Intelbras")
    st.markdown("Pesquise, filtre e compare os nobreaks disponíveis.")

# Filtros
with st.sidebar:
    st.header("Filtros")
    tipo = st.multiselect("Tipo de nobreak", df["Tipo"].unique(), default=df["Tipo"].unique())
    tensao = st.multiselect("Tensão", df["Tensão"].unique(), default=df["Tensão"].unique())

# Aplicar filtros
df_filtrado = df[(df["Tipo"].isin(tipo)) & (df["Tensão"].isin(tensao))]

# Resultados
st.markdown(f"### Resultados encontrados: {len(df_filtrado)}")

# Cards de equipamentos
for _, row in df_filtrado.iterrows():
    with st.container():
        st.markdown("---")
        col1, col2 = st.columns([2, 4])
        with col1:
            st.subheader(row["Modelo"])
            st.write(f"**Tipo:** {row['Tipo']}")
            st.write(f"**Tensão:** {row['Tensão']}")
            st.write(f"**Tomadas:** {row['Tomadas']}")
            st.write(f"**Baterias:** {row['Baterias']}")
        with col2:
            st.markdown(
                "<div style='background-color:#F0F0F0;padding:10px;border-radius:10px;'>"
                "<strong>Descrição resumida:</strong><br>"
                "Nobreak ideal para pequenas e médias cargas com proteção contra quedas de energia e picos de tensão."
                "</div>",
                unsafe_allow_html=True
            )
