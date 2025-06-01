#this page url -> https://appp1-vbvxxswaiodyhriql4c5q6.streamlit.app/

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#st.title("Manipulation de données et création de graphiques")

current_dataset = st.selectbox('Quel dataset veux-tu utiliser ?', sns.get_dataset_names())

#print("https://github.com/mwaskom/seaborn-data/blob/master/" + current_dataset + ".csv")
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/" + current_dataset + ".csv")
st.dataframe(df)

x= st.selectbox('Choisissez la colonne X ?', df.columns)
y= st.selectbox('Choisissez la colonne Y ?', df.drop(columns=[x]).columns)

plot_dict = {'scatter_chart': st.scatter_chart,
             'bar_chart': st.bar_chart,
             'line-chart': st.line_chart}
# Créer un graphique barbplot

plot_dict[st.selectbox('Quel graphique veux-tu utiliser ?', plot_dict.keys())](data=df, x=x, y=y)
if st.checkbox("Afficher la matrice de corrélation "):
    if pd.api.types.is_numeric_dtype(df[x]) and pd.api.types.is_numeric_dtype(df[y]):
        st.title("Ma matrice de corrélation")
        fig, ax = plt.subplots()
        sns.heatmap(df[[x, y]].corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    else:
        st.write("Impossible d'afficher la matrice de corrélation, les valeurs x et y ne sont pas numériques")