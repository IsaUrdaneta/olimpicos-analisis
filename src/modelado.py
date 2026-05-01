import pandas as pd
import os
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def crear_directorio():
    os.makedirs('outputs', exist_ok=True)
    os.makedirs('outputs/graficos', exist_ok=True)

def entrenar_modelo(df):

    crear_directorio()

    X = df[['Edad', 'Altura_cm', 'Peso_kg', 'Entrenamientos_Semanales']]
    y = df['Medallas_Totales']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)

    print(f"R² del modelo: {r2:.4f}")

    # Guardar resultados
    resultados = pd.DataFrame({
        'Real': y_test,
        'Predicho': y_pred
    })
    resultados.to_csv('outputs/resultados_modelo.csv', index=False)

    # Guardar métricas
    with open('outputs/metricas.txt', 'w') as f:
        f.write(f"R2: {r2:.4f}")

    # Gráfico
    plt.scatter(y_test, y_pred)
    plt.xlabel('Valores reales')
    plt.ylabel('Predicciones')
    plt.title('Modelo: Real vs Predicho')
    plt.savefig('outputs/graficos/modelo_prediccion.png')
    plt.close()

    return model, y_pred, r2