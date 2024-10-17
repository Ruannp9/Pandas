import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy

#sidebar

st.sidebar.header("Filtros")

#Elementos de textos:

st.title("Isso é um :blue[título] :sunglasses:")
st.header("Isso aqui é um cabeçalho", divider="gray")
st.subheader("Isso aqui é um sub-cabeçalho", divider=True)
st.text("Isso aqui é um texto.")

#Elementos de dados:

df = pd.DataFrame(numpy.random.randn(50,20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)

#Elementos de seleção:

# CheckBox
selecao1 = st.checkbox("Marcado")

if selecao1:
    st.write("É o black")
else:
    st.write("Não é o black")
#Cor
cor = st.color_picker("Selecione a cor", "#00f900")
st.write("Cor selecionada", cor)

# Multiselect
opcoes = st.multiselect(
    "Selecione as opções",
    ["Green", "Yellow", "Red", "Blue"]
)
st.write("Sua seleção", opcoes)

#Radio
genero = st.radio(
    "Qual o seu estilo de filme favorito ?",
    [":rainbow[Comedia]", "***Drama***", "Documentario :movie_camera:"],
    captions=[
        "Você é o engraçado.",
        "Vai chorar manda audio.",
        "Só quer ser o inteligente.",
    ],
)

if genero == ":rainbow[Comedia]":
    st.write("Você selecionou comedia.")
else:
    st.write("Você não selecionou comedia.")
    
#Selectbox
option = st.selectbox(
    "Qual o seu melhor contato?",
    ("Email", "Telefone", "Celular"),
)

st.write("Você selecionou:", option)

#Slider
start_color, end_color = st.select_slider(
    "Selecione o range das cores",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "Violet",
    ],
    value=("red", "blue"),
)

#Toggle
on = st.toggle("Activate feature")

if on:
    st.write("Feature activated!")




