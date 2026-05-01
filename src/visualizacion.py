import matplotlib.pyplot as plt
import seaborn as sns
import os

def guardar_graficos(df):
    os.makedirs("outputs/graficos", exist_ok=True)

    # Distribuciones
    df.hist(figsize=(10,8))
    plt.tight_layout()
    plt.savefig("outputs/graficos/distribuciones.png")
    plt.close()

    # Medallas por deporte
    df.groupby('Deporte')['Medallas_Totales'].sum().plot(kind='bar')
    plt.title('Medallas por deporte')
    plt.savefig("outputs/graficos/medallas_deporte.png")
    plt.close()

    # Scatter entrenamiento vs medallas
    plt.scatter(df['Entrenamientos_Semanales'], df['Medallas_Totales'])
    plt.xlabel('Entrenamientos')
    plt.ylabel('Medallas')
    plt.savefig("outputs/graficos/entrenamiento_medallas.png")
    plt.close()

    # Heatmap
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.savefig("outputs/graficos/heatmap.png")
    plt.close()