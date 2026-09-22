# TPFINAL1.ITD

# Proyectos Financiados por el BID — Enfoque en Ciencia y Tecnología

Trabajo Práctico de análisis de datos sobre el **IDB Projects Dataset**, el listado 
público de proyectos financiados por el Banco Interamericano de Desarrollo (BID), 
con foco en el sector de Ciencia y Tecnología.

## Objetivo

Analizar el dataset de proyectos del BID para identificar patrones, tendencias y 
relaciones entre variables, aplicando un flujo completo de ciencia de datos: desde 
la ingesta y limpieza hasta la construcción de un modelo predictivo simple.

## Dataset

- **Fuente**: [IDB Open Data Portal](https://data.iadb.org/dataset/idb-projects-dataset)
- **Licencia**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- Más detalles y cómo descargarlo en [`data/README.md`](data/README.md)

## Estructura del repositorio


## Metodología

**1. Ingesta y estructura**
- Carga del dataset en un DataFrame de pandas.
- Identificación de tipos de variables (numéricas, categóricas, fechas).

**2. Limpieza y estadística descriptiva**
- Tratamiento de valores nulos y duplicados.
- Resumen estadístico con `.describe()`, interpretando media y dispersión.

**3. Análisis visual**
- Distribución de una variable clave.
- Comparación entre variables o categorías.
- Correlación entre variables numéricas.

**4. Modelado**
- Implementación de un modelo de **Regresión Lineal** o **Árbol de Decisión**, 
  según la naturaleza de la variable a predecir.
- Justificación del modelo elegido en una celda Markdown del notebook.

## Tecnologías

- Python
- pandas
- matplotlib / seaborn
- scikit-learn

## Cómo correr el proyecto

```bash
git clone https://github.com/naomi29ar/TPFINAL1.ITD.git
cd TPFINAL1.ITD
pip install -r requirements.txt
python data/download_data.py
```

Luego abrir `notebooks/analisis.ipynb` en Jupyter o Google Colab.

## Autora

Naomi — Trabajo Práctico individual.
