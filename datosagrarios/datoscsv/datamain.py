import pandas as pd

def obtenerProductos():
    df = pd.read_csv('datosagrarios/datoscsv/precios_agrarios_comunitat_valenciana.csv', delimiter=';')
    productos_unicas = df['Producto castellano'].unique().tolist()
    # Convertir cada elemento a string si no lo es
    productos_unicas = sorted([str(producto) for producto in productos_unicas])
    # print(variedades_unicas)
    return productos_unicas

def obtenerVariedades():
    df = pd.read_csv('datosagrarios/datoscsv/precios_agrarios_comunitat_valenciana.csv', delimiter=';')
    variedades_unicas = df['Variedad castellano'].unique().tolist()
    # Convertir cada elemento a string si no lo es
    variedades_unicas = sorted([str(variedad) for variedad in variedades_unicas])
    # print(variedades_unicas)
    return variedades_unicas

def media_precio_por_anyo(variedad):
    df = pd.read_csv('datosagrarios/datoscsv/precios_agrarios_comunitat_valenciana.csv', delimiter=';')
    # Filtra el DataFrame por la variedad especificada
    df_variedad = df[df['Variedad castellano'] == variedad]

    # Convertir la columna 'Precio Medio' a tipo numérico
    df_variedad['Precio Medio'] = pd.to_numeric(df_variedad['Precio Medio'].str.replace(',', '.'))

    # Agrupar por año y calcular la media del precio medio
    df_resultado = df_variedad.groupby('Anyo Precio')['Precio Medio'].mean().reset_index()

    # Crear una lista de diccionarios en el formato deseado
    resultado_formato = [
        {"y": row['Precio Medio'], "label": str(int(row['Anyo Precio']))}
        for _, row in df_resultado.iterrows()
    ]

    return resultado_formato

