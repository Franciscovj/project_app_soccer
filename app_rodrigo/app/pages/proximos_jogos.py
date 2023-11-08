import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="FVJ JOGOS DO DIA",
    page_icon=":bar_chart:",
    layout="wide",
)
st.title("Web App fvj Stats ⚽")

st.markdown(
    """
    <span style="color: blue">**Faça aqui suas análises dos seus jogos do dia ⭐**</span><br>
    <span style="color: green">*boas análises!!!*</span>  
    """,
    unsafe_allow_html=True,
)




def load_data_jogos():
    data_jogos = pd.read_csv(r"app_rodrigo\app\dados_full_x.csv")
    data_jogos = data_jogos[
        [
            "League",
            "Date",
            "Time",
            "Round",
            "Home",
            "Away",
            "posicao_home",
            "posicao_away",
            "FT_Odd_H",
            "FT_Odd_D",
            "FT_Odd_A",
            "FT_Odd_Over25",
            "FT_Odd_Under25",
            "FT_Odd_BTTS_Yes",
            "FT_Odd_BTTS_No",
            "Media_Total_2HT_H",
            "Media_Total_2HT_A",
            "CV_Media_Total_2HT_H",
            "CV_Media_Total_2HT_A",
            "PPJ_H",
            "CV_Pontos_H",
            "PPJ_A",
            "CV_Pontos_A",
            "Media_primeiro_gol_home",
            "Media_primeiro_gol_away",
            "Media_primeiro_gol_home_sofrido",
            "Media_primeiro_gol_away_sofrido",
            "xg_home",
            "xg_away",
            "xg_jogo",
            "Power_home",
            "Power_away",
            "media_movel_chutes_por_gol_H",
            "media_movel_chutes_por_gol_A",
            "media_chutes_home",
            "media_chutes_away",
            "Porc_Over05HT_Home",
            'Porc_Over15HT_Home',
            'Porc_Under05HT_Home',
            'Porc_Over25FT_Home',
            "Porc_Home_Win",
            "Media_FT_Corners_H_MAR",
            "Media_FT_Corners_H_SFR",
            "Porc_Over05HT_Away",
            'Porc_Over15HT_Away',
            'Porc_Under05HT_Away',
            'Porc_Over25FT_Away',
            "Porc_Away_Win",
            "Media_FT_Corners_A_MAR",
            "Media_FT_Corners_A_SFR",
            'Diferente_0x0_Home',
            'Diferente_0x0_Away'
            
        ]
    ]


    return data_jogos

df_jogos = load_data_jogos()
with st.sidebar:
    st.sidebar.header("Jogos do Dia")
    with st.expander("Seleção Data"):
        sorted_unique_date = sorted(df_jogos.Date.unique())
        selected_date = st.multiselect(
            "Date", sorted_unique_date, sorted_unique_date
        )
        if not selected_date:
            st.warning("Selecione pelo menos uma data para continuar.")
        else:
            df_jogos = df_jogos[df_jogos["Date"].isin(selected_date)]

# Define o valor mínimo e máximo iniciais com base na coluna "FT_Odd_H" do DataFrame
valor_min_home = float(df_jogos["FT_Odd_H"].min())
valor_max_home = float(df_jogos["FT_Odd_H"].max())
valor_min_draw = float(df_jogos["FT_Odd_D"].min())
valor_max_draw = float(df_jogos["FT_Odd_D"].max())
valor_min_away = float(df_jogos["FT_Odd_A"].min())
valor_max_away = float(df_jogos["FT_Odd_A"].max())
valor_min_over = float(df_jogos["FT_Odd_Over25"].min())
valor_max_over = float(df_jogos["FT_Odd_Over25"].max())

st.markdown(
    """
<span style="color: blue">**Filtro de  Odds**</span><br>
""",
    unsafe_allow_html=True,
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    valor_min_home, valor_max_home = st.slider(
        "Casa",
        float(df_jogos["FT_Odd_H"].min()),
        float(df_jogos["FT_Odd_H"].max()),
        (valor_min_home, valor_max_home),
        step=0.01,
    )
with col2:
    valor_min_draw, valor_max_draw = st.slider(
        "Empate",
        float(df_jogos["FT_Odd_D"].min()),
        float(df_jogos["FT_Odd_D"].max()),
        (valor_min_draw, valor_max_draw),
        step=0.01,
    )
with col3:
    valor_min_away, valor_max_away = st.slider(
        "Fora",
        float(df_jogos["FT_Odd_A"].min()),
        float(df_jogos["FT_Odd_A"].max()),
        (valor_min_away, valor_max_away),
        step=0.01,
    )
with col4:
    valor_min_over, valor_max_over = st.slider(
        "Over 2.5",
        float(df_jogos["FT_Odd_Over25"].min()),
        float(df_jogos["FT_Odd_Over25"].max()),
        (valor_min_over, valor_max_over),
        step=0.01,
    )


df_filtrado = df_jogos.query(
    "@valor_min_home <= FT_Odd_H <= @valor_max_home and @valor_min_draw <= FT_Odd_D <= @valor_max_draw and\
                              @valor_min_away <= FT_Odd_A <= @valor_max_away and @valor_min_over <= FT_Odd_Over25 <= @valor_max_over"
)

st.subheader("Jogos do Dia")
st.markdown(f"Total jogos para o dia  de Hoje : {len(df_filtrado)} jogos")
st.dataframe(df_filtrado)