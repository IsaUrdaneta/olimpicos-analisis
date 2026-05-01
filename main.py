from src.limpieza import cargar_datos, limpiar_outliers
from src.analisis import resumen_estadistico, insight_clave
from src.modelado import entrenar_modelo
from src.visualizacion import guardar_graficos
import os

# 1. Carga (ajusta ruta consistente)
df = cargar_datos("data/raw/olimpicos.csv")

# 2. Limpieza
columnas = ['Edad','Altura_cm','Peso_kg','Entrenamientos_Semanales','Medallas_Totales']
df_clean = limpiar_outliers(df, columnas)

# 3. Análisis
resumen = resumen_estadistico(df_clean)
insights = insight_clave(df_clean)

# 4. Modelo
model, y_pred, r2 = entrenar_modelo(df_clean)

# 5. Visualización
guardar_graficos(df_clean)

# 6. Guardar outputs
os.makedirs("outputs/reportes", exist_ok=True)

with open("outputs/reportes/insights.txt", "w") as f:
    f.write(f"""
Promedio medallas: {insights['promedio_medallas']:.2f}
Deporte más frecuente: {insights['top_deporte']}
Correlación entrenamiento-medallas: {insights['correlacion_entrenamiento']:.2f}
R2 modelo: {r2:.4f}
""")

print("Pipeline ejecutado correctamente")