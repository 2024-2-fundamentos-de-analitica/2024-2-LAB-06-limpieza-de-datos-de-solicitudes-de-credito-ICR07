import pandas as pd
import os

def create_output_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def pregunta_01():

    data = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)
    output = "files/output/solicitudes_de_credito.csv"
    #Hacemos una copia para no dañar el archivo original
    data = data.copy()

    #Seleccionamos las columnas a evaluar
    columnas = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "monto_del_credito", "línea_credito"]

    #Hacemos un ciclo for para limpiar las columnas
    for col in columnas:
        if col in data.columns:
            data[col] = data[col].str.lower().str.strip().str.replace("_", " ").str.replace("-", " ").str.replace(",", "").str.replace("$", "").str.replace(".00", "").str.strip()
    #Limpiamos las columnas de barrio 
    if "barrio" in data.columns:
        data["barrio"] = data["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    #Limpiamos las columnas de comuna_ciudadano pasandolas a numericas
    if "comuna_ciudadano" in data.columns:
        data["comuna_ciudadano"] = pd.to_numeric(data["comuna_ciudadano"], errors="coerce", downcast="integer")
    #Limpiamos las columnas de monto_del_credito pasandolas a numericas
    if "monto_del_credito" in data.columns:
        data["monto_del_credito"] = pd.to_numeric(data["monto_del_credito"], errors="coerce")
    #Limpiamos las columnas de fecha_de_beneficio pasandolas a formato fecha
    if "fecha_de_beneficio" in data.columns:
        data["fecha_de_beneficio"] = pd.to_datetime(
            data["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
        ).combine_first(
            pd.to_datetime(data["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")
        )

    #Borramos duplicados y nulos
    data = data.drop_duplicates()
    data = data.dropna()
    data.to_csv(output, sep=";",index=False)
pregunta_01()
"""
Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
El archivo tiene problemas como registros duplicados y datos faltantes.
Tenga en cuenta todas las verificaciones discutidas en clase para
realizar la limpieza de los datos.

El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

"""
