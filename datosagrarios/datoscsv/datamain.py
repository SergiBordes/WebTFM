import pandas as pd

def obtenerVariedades():
    df = pd.read_csv('datosagrarios/datoscsv/precios_agrarios_comunitat_valenciana.csv', delimiter=';')
    variedades_unicas = df['Producto castellano'].unique().tolist()
    # Convertir cada elemento a string si no lo es
    variedades_unicas = sorted([str(variedad) for variedad in variedades_unicas])
    # print(variedades_unicas)
    return variedades_unicas
