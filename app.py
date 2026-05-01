import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("🏅 Análisis de Atletas Olímpicos")

@st.cache_data
def load_data():
    return pd.read_csv("data/raw/olimpicos.csv")

df = load_data()

#Agregar r2
st.subheader("Modelo")

try:
    with open("outputs/metricas.txt") as f:
        r2 = f.read()
    st.metric("R² del modelo", r2)
except:
    st.warning("Ejecuta primero main.py")

# ======================
# FILTRO
# ======================
st.sidebar.header("Filtros")

deporte = st.sidebar.selectbox(
    "Deporte",
    ["Todos"] + list(df["Deporte"].unique())
)

if deporte != "Todos":
    df = df[df["Deporte"] == deporte]

# ======================
# KPIs
# ======================
col1, col2, col3 = st.columns(3)

col1.metric("Total atletas", len(df))
col2.metric("Promedio medallas", round(df["Medallas_Totales"].mean(),2))
col3.metric("Máximo medallas", df["Medallas_Totales"].max())

# ======================
# GRÁFICO
# ======================
st.subheader("Entrenamientos vs Medallas")

fig, ax = plt.subplots()
sns.regplot(data=df, x="Entrenamientos_Semanales", y="Medallas_Totales", ax=ax)
st.pyplot(fig)

# ======================
# INSIGHTS
# ======================
st.subheader("Insights")

st.write(f"""
- Deporte dominante: **{df['Deporte'].value_counts().idxmax()}**
- Promedio entrenamientos: **{round(df['Entrenamientos_Semanales'].mean(),2)}**
""")

# ======================
# TABLA
# ======================
st.dataframe(df.head(50))