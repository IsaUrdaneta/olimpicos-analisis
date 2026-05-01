def resumen_estadistico(df):
    return df.describe()

def correlacion(df):
    return df.corr(numeric_only=True)

def insight_clave(df):
    return {
        "promedio_medallas": df["Medallas_Totales"].mean(),
        "top_deporte": df["Deporte"].value_counts().idxmax(),
        "correlacion_entrenamiento": df["Entrenamientos_Semanales"].corr(df["Medallas_Totales"])
    }