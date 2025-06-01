#this page url -> https://appp2-triaypccd5eojuqwkkvmmf.streamlit.app/

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Creation d'un dictionnaire contenant les fonctions pour creer differents graphs
plot_dict = {'scatter_chart': st.scatter_chart,
             'bar_chart': st.bar_chart,
             'line-chart': st.line_chart}

#Choix du dataset proposer par seaborn
current_dataset = st.selectbox('Quel dataset veux-tu utiliser ?', sns.get_dataset_names())

#Chargement du dataset choisit par le user
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/" + current_dataset + ".csv")

#Affichage du dataset
st.dataframe(df)

#Le user choisit la colonne X
x= st.selectbox('Choisissez la colonne X ?', df.columns)

#Le user choisit la colonne Y
y= st.selectbox('Choisissez la colonne Y ?', df.drop(columns=[x]).columns)

#Demande au user de chosir le type de graph dans la liste des clefs du dictionnaire, puis affiche le graph
plot_dict[st.selectbox('Quel graphique veux-tu utiliser ?', plot_dict.keys())](data=df, x=x, y=y)

#Si le user a choisit d'afficher la matrice de correlation
if st.checkbox("Afficher la matrice de corrélation "):

    #Et si x et y sont numeriques
    if pd.api.types.is_numeric_dtype(df[x]) and pd.api.types.is_numeric_dtype(df[y]):

        #Affichage du titre
        st.title("Ma matrice de corrélation")

        #Creation d'un subplot
        fig, ax = plt.subplots()

        #Creation du heatmap
        sns.heatmap(df[[x, y]].corr(), annot=True, cmap='coolwarm', ax=ax)

        #Affichage du heatmap
        st.pyplot(fig)

    else:
        st.write("Impossible d'afficher la matrice de corrélation, les valeurs x et y ne sont pas numériques")