import os
import pandas as pd
import streamlit as st


# Configuración de la página
st.set_page_config(page_icon="📌", layout="wide")

st.title("Momento 2 - Actividad 2")

st.header("Estudiantes en Colombia")
st.markdown(
    """
En esta actividad, se trabajará con un archivo CSV que contiene información de 50 estudiantes en Colombia,
 incluyendo datos como su nombre, edad, ciudad, promedio académico y asistencia. 
"""
)

st.header("Objetivo de aprendizaje")

st.markdown(
    """
    El objetivo principal es desarrollar una aplicación interactiva con Streamlit que permita explorar 
    y visualizar fácilmente la informacion información del archivo CSV.

"""
)

st.header("Solución")


st.title("🧑‍🎓 Bienvenido al explorador de Estudiantes")

st.subheader("¿Qué deseas hacer hoy con los registros?")

opcion = st.selectbox(
    "Elige una opción:",
    (
        "Ver primeras y últimas 5 filas",
        "Ver el resumen con .info() y .describe().)",
        "Seleccionar columnas específicas",
        "Filtrar por promedio",
    ),
)


archivo = pd.read_csv("pages/static/datasets/estudiantes_colombia.csv")

# Opción 1
if opcion == "Ver primeras y últimas 5 filas":
    # primeras 5  filas

    st.subheader("▪️ Primeras 5 filas")
    st.dataframe(archivo.head())

    # ultimas  5 filas
    st.subheader("▪️ Últimas 5 filas")
    st.dataframe(archivo.tail())


# Opción 2
elif opcion == "Resumen del dataset (.info y .describe)":
    st.subheader("Resumen general del dataset")
    # mostrar resumen
    st.write(archivo.info())

    st.text("Resumen estadístico con .describe():")
    # Mostrar estadistica
    st.write(archivo.describe())


# Opción 3: Selección de columnas
elif opcion == "Seleccionar columnas específicas":
    st.subheader("Que columnas quieres ver")
    columnas = st.multiselect(
        "Selecciona una o más columnas:",
        archivo.columns.tolist(),
        default=["nombre", "edad", "ciudad", "promedio", "asistencia"],
    )
    st.dataframe(archivo[columnas])


# Opción 4: # Filtrar estudiantes con promedio mayor a un valor definido por el usuario (usando un slider).

elif opcion == "Filtrar por promedio":
    st.subheader("Filtra estudiantes según su promedio")
    st.subheader("promedio mayor de 3")
    st.write(archivo[archivo["promedio"] > 3])
