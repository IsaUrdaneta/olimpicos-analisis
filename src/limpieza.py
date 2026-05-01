import pandas as pd

def cargar_datos(path):
    return pd.read_csv(path)

def limpiar_outliers(df, columnas):
    df_clean = df.copy()

    for col in columnas:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1

        lim_inf = q1 - 1.5 * iqr
        lim_sup = q3 + 1.5 * iqr

        df_clean = df_clean[(df_clean[col] >= lim_inf) & (df_clean[col] <= lim_sup)]

    return df_clean