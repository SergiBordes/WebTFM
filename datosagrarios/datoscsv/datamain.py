import pandas as pd

df = pd.read_csv('datosagrarios/datoscsv/precios_agrarios_comunitat_valenciana.csv', delimiter=';')

#Obtener todos los productos
def obtenerProductos():
    productos_unicas = df['Producto castellano'].unique().tolist()
    # Convertir cada elemento a string si no lo es
    productos_unicas = sorted([str(producto) for producto in productos_unicas])
    # print(variedades_unicas)
    return productos_unicas

#Obtener todas las variedades
def obtenerVariedades():
    variedades_unicas = df['Variedad castellano'].unique().tolist()
    # Convertir cada elemento a string si no lo es
    variedades_unicas = sorted([str(variedad) for variedad in variedades_unicas])
    # print(variedades_unicas)
    return variedades_unicas

# Media de precio de variedad por año para la gráfica
def media_precio_por_anyo(variedad):
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

# Media de precio por provincia y año
def precio_medio_variedad_por_provincia(variedad, anyo):
    df = pd.read_csv('datosagrarios/datoscsv/precios_agrarios_comunitat_valenciana.csv', delimiter=';')
    # Filtrar por variedad y año
    df_filtrado = df[(df['Variedad castellano'] == variedad) & (df['Anyo Precio'] == anyo)]
    
    # Limpiar y convertir los valores de 'Precio Medio' a numéricos
    df_filtrado['Precio Medio'] = df_filtrado['Precio Medio'].str.replace(',', '.').astype(float)
    
    # Calcular el precio medio por provincia
    precios_medios = df_filtrado.groupby(['Zona castellano', 'Zona valenciano'])['Precio Medio'].mean().reset_index()
    
    # Ordenar los resultados de mayor a menor precio medio
    precios_medios = precios_medios.sort_values(by='Precio Medio', ascending=False)
    
    # Crear una lista de diccionarios en el formato deseado
    resultado_formato = [
        {"provincia": f"{row['Zona valenciano']}/{row['Zona castellano']}", "precio_medio": round(row['Precio Medio'], 2)}
        for index, row in precios_medios.iterrows()
    ]
    
    return resultado_formato

