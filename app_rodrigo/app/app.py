import streamlit as st
import pandas as pd
from time import sleep
import numpy as np
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="FVJ H 2 H",
    page_icon=":bar_chart:",
    layout="wide",
)
st.title("Web App fvj Stats ⚽")

st.markdown(
    """
    <span style="color: blue">**H 2 H⭐**</span><br>
    <span style="color: green">*boas análises!!!*</span>  
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.sidebar.header("H 2 H")

st.markdown("""---""")


ligas = [
    'COLÔMBIA - PRIMEIRA A',
    'JAPÃO - LIGA J1',
    'SUÉCIA - ALLSVENSKAN',
    'EUA - MLS',
    'NORUEGA - ELITESERIEN',
    'BRASIL - SÉRIE B',
    'BRASIL - SÉRIE A',
    'MÉXICO - LIGA MX',
    'BRASIL - SÉRIE C',
    'ARÁBIA SAUDITA - LIGA PROFISSIONAL SAUDITA',
    'ALEMANHA - 2. BUNDESLIGA',
    'ITÁLIA - SERIE A',
    'PORTUGAL - LIGA PORTUGAL 2',
    'ALEMANHA - 3. LIGA',
    'ESPANHA - LALIGA',
    'ESPANHA - LALIGA2',
    'PAÍSES BAIXOS - EREDIVISIE',
    'ALEMANHA - BUNDESLIGA',
    'BÉLGICA - LIGA JUPILER',
    'INGLATERRA - PREMIER LEAGUE',
    'FRANÇA - LIGUE 1',
    'PORTUGAL - LIGA PORTUGAL',
    'INGLATERRA - CHAMPIONSHIP',
    'ÁUSTRIA - BUNDESLIGA',
    'ITÁLIA - SERIE B',
    'INGLATERRA - LEAGUE TWO (4ª DIVISÃO)',
    'INGLATERRA - LEAGUE ONE (3ª DIVISÃO)',
    'ESCÓCIA - PREMIERSHIP',
    'AUSTRÁLIA - A-LEAGUE',
    'TURQUIA - SUPER LIG', 
    'GRÉCIA - SUPERLIGA'
]

ligas_ordenadas = sorted(ligas)

with st.sidebar:
    st.sidebar.header("App análises FVJ")
    selected_league = st.sidebar.selectbox("Ligas", ligas_ordenadas)


def load_data(league):
    print("Carregando arquivo CSV...")
    data = pd.read_csv(r"app_rodrigo\app\dados_full_x.csv")
    print("Arquivo CSV carregado!")
    data = data[data["League"] == league]
    return data

df = load_data(selected_league)
st.subheader("Liga Selecionada - " + selected_league)
df_filtered = df.copy()
df_filtered_away = df.copy()

selected_team_home = None
selected_team_away = None 

############################################################################################################################################
def catoes_st():
    st.markdown("""---""")
    st.markdown("""#""")
    Media_de_Gol_Mar_Home = filtered_rows.FT_Goals_H.mean().round(2)
    Media_de_Gol_Sofr_Home = filtered_rows.FT_Goals_A.mean().round(2)
    Media_de_Gol_por_par = (Media_de_Gol_Mar_Home + Media_de_Gol_Sofr_Home).round(2)
    Media_de_Gol_Mar_Home_HT = filtered_rows.HT_Goals_H.mean().round(2)
    Media_de_Gol_Sofr_Home_HT = filtered_rows.HT_Goals_A.mean().round(2)
    Media_de_Gol_por_par_HT = (Media_de_Gol_Mar_Home_HT + Media_de_Gol_Sofr_Home_HT).round(2)
    total_jogos = len(filtered_rows)
    
    Media_de_cantos_Mar_Home = filtered_rows.FT_Corners_H.mean().round(2)
    Media_de_cantos_Sofr_Home = filtered_rows.FT_Corners_A.mean().round(2)
    Media_de_cantos_por_par = (Media_de_cantos_Mar_Home+ Media_de_cantos_Sofr_Home).round(2) 
    
    Media_de_cantos_Mar_Home_HT = filtered_rows.HT_Corners_H.mean().round(2)
    Media_de_cantos_Sofr_Home_HT = filtered_rows.HT_Corners_A.mean().round(2)
    Media_de_cantos_HT = (Media_de_cantos_Mar_Home_HT + Media_de_cantos_Sofr_Home_HT).round(2) 

    Media_de_cartoes_Mar_Home = filtered_rows.FT_Cartoes_H.mean().round(2)
    Media_de_cartoes_Sofr_Home = filtered_rows.FT_Cartoes_A.mean().round(2)
    Media_de_cartoes = (Media_de_cartoes_Mar_Home + Media_de_cartoes_Sofr_Home).round(2) 
        
    
    st.write("**TOTAL JOGOS 🆚:**")
    st.markdown(f"""
        **{total_jogos}**
        """)
    dst01, dst02, dst03, = st.columns(3)
    with dst01:
        st.write("**MEDIA DE GOLS MAR HT ⚽ :**")
        st.info(f"{Media_de_Gol_Mar_Home_HT}")
    with dst02:
        st.write("**MEDIA DE GOLS SOFR HT ⚽:**")
        st.info(f"{Media_de_Gol_Sofr_Home_HT}")
    with dst03:
        st.write("**MEDIA DE GOLS P. PART. HT⚽:**")
        st.info(f"{Media_de_Gol_por_par_HT}")
        
    dst1, dst2, dst3, = st.columns(3)
    with dst1:
        st.write("**MEDIA DE GOLS MAR FT⚽ :**")
        st.info(f"{Media_de_Gol_Mar_Home}")
    with dst2:
        st.write("**MEDIA DE GOLS SOFR FT⚽:**")
        st.info(f"{Media_de_Gol_Sofr_Home}")
    with dst3:
        st.write("**MEDIA DE GOLS P. PART. FT⚽:**")
        st.info(f"{Media_de_Gol_por_par}")

    dst8, dst9, dst10 = st.columns(3)
    with dst8:
        st.write("**MEDIA DE CANTOS MAR HT ⛳ :**")
        st.info(f"{Media_de_cantos_Mar_Home_HT }")
    with dst9:
        st.write("**MEDIA DE CANTOS SOFR HT ⛳:**")
        st.info(f"{Media_de_cantos_Sofr_Home_HT}")
    with dst10:
        st.write("**MEDIA DE CANTOS HT.⛳:**")
        st.info(f"{ Media_de_cantos_HT }") 
                
    dst5, dst6, dst7 = st.columns(3)
    with dst5:
        st.write("**MEDIA DE CANTOS MAR FT ⛳ :**")
        st.info(f"{Media_de_cantos_Mar_Home }")
    with dst6:
        st.write("**MEDIA DE CANTOS SOFR FT ⛳:**")
        st.info(f"{Media_de_cantos_Sofr_Home}")
    with dst7:
        st.write("**MEDIA DE CANTOS P. PART. FT⛳:**")
        st.info(f"{Media_de_cantos_por_par}") 
        
    dst11, dst12, dst13 = st.columns(3)
    with dst11:
        st.write("**MEDIA DE CARTOES A FAVOR 🟨 :**")
        st.info(f"{Media_de_cartoes_Mar_Home }")
    with dst12:
        st.write("**MEDIA DE CARTOES  CONTRA FT 🟨 :**")
        st.info(f"{Media_de_cartoes_Sofr_Home}")
    with dst13:
        st.write("**MEDIA DE CARTOES P. PART.🟨:**")
        st.info(f"{Media_de_cartoes}")
                   
##############################################################################################################################################        
def Analise_Home(): 
    global filtered_rows
    with st.form("ANALISE HOME"):
        unique_teams = df_filtered["Home"].unique()
        
        selected_team_home  = st.selectbox("Selecione um time (Home)", unique_teams)
        
        botao_form_home = st.form_submit_button("Verificar disponibilidade (Home)")
    if st.button("Limpar (Home)"):
        selected_team_home  = None 
    if botao_form_home:
        filtered_rows = df_filtered[
            df_filtered["Home"].str.lower() == selected_team_home.lower()
        ]
        filtered_rows = filtered_rows[
            [
                "Date",
                "Time",
                "League",
                "Season",
                "Round",
                "Home",
                "Away",
                "HT_Goals_H",
                "HT_Goals_A",
                "FT_Goals_H",
                "FT_Goals_A",
                "Total_Goals_HT",
                "Total_Goals_FT",
                "FT_Odd_H",
                "FT_Odd_D",
                "FT_Odd_A",
                "HT_Odd_Over05",
                "HT_Odd_Under05",
                "FT_Odd_Over05",
                "FT_Odd_Under05",
                "FT_Odd_Over15",
                "FT_Odd_Under15",
                "FT_Odd_Over25",
                "FT_Odd_Under25",
                "FT_Odd_Over35",
                "FT_Odd_Under35",
                "FT_Odd_Over45",
                "FT_Odd_Under45",
                "Odd_BTTS_Yes",
                "Odd_BTTS_No",
                "Odds_AH_Neg05_H",
                "Odds_AH_Pos05_A",
                "Odds_AH_Pos05_H",
                "Odds_AH_Neg05_A",
                "Media_Total_2HT_H",
                "Media_Total_2HT_A",
                "CV_Media_Total_2HT_H",
                "CV_Media_Total_2HT_A",
                "PPJ_H",
                "CV_Pontos_H",
                "PPJ_A",
                "CV_Pontos_A",
                "FT_Corners_H",
                "FT_Corners_A",
                "HT_Corners_H",
                "HT_Corners_A",
                "FT_Cartoes_H",
                "FT_Cartoes_A",
                "Goals_Minutes_Home",
                "Goals_Minutes_Away",
                "GM_H",
                "GM_A",
                "GS_H",
                "GS_A",
                "Media_GM_H",
                "Media_GM_A",
                "Media_GS_H",
                "Media_GS_A",
                "Media_GM_H_10",
                "Media_GM_A_10",
                "Media_GS_H_10",
                "Media_GS_A_10",
                "Media_primeiro_gol_home",
                "Media_primeiro_gol_away",
                "primeiro_gol_home",
                "primeiro_gol_away",
                "Media_primeiro_gol_away_sofrido",
                "Media_primeiro_gol_home_sofrido",
                "Power_home",
                "Power_away",
                "FT_Finalizações_H",
                "FT_Finalizações_A",
                "HT_Finalizações_H",
                "HT_Finalizações_A",
                "FT_Chutes_fora_H",
                "FT_Chutes_fora_A",
                "HT_Chutes_fora_H",
                "HT_Chutes_fora_A",
                "media_chutes_por_gol_H",
                "media_chutes_por_gol_A",
                "media_movel_chutes_por_gol_H",
                "media_movel_chutes_por_gol_A",
            ]
        ]

        filtered_rows = filtered_rows.drop_duplicates()

        filtered_rows["Date"] = pd.to_datetime(
            filtered_rows["Date"], format="%d/%m/%Y", errors="coerce"
        )

        filtered_rows = filtered_rows.dropna(subset=["Date"])

        filtered_rows = filtered_rows.sort_values(by=["Date"])
        filtered_rows.index = filtered_rows.index + 1
        filtered_rows.index.name = "Nº" 
        if not filtered_rows.empty:
            st.write("Temos informações sobre esse time:")
            filtered_rows = filtered_rows.tail(10)
            media_chutes = filtered_rows['FT_Finalizações_H'].mean().round(2)
            media_chutes_fora = filtered_rows['FT_Chutes_fora_H'].mean().round(2)
            media_min_gol = filtered_rows['primeiro_gol_home'].mean().round(2)
            
            media_gols_mar_ht  = filtered_rows['HT_Goals_H'].mean().round(2)
            desv_pad_mar_ht = filtered_rows['HT_Goals_H'].std().round(2)
            cv_mar_ht = (desv_pad_mar_ht / media_gols_mar_ht ).round(2)
            media_gols_sof_ht  = filtered_rows['HT_Goals_A'].mean().round(2)
            media_gols_mar_ht_sum  = filtered_rows['HT_Goals_H'].sum()
            desv_pad_sof_ht = filtered_rows['HT_Goals_A'].std().round(2)
            cv_sof_ht = (desv_pad_sof_ht / media_gols_sof_ht ).round(2)
             
            media_gols_mar  = filtered_rows['FT_Goals_H'].mean().round(2)
            desv_pad_mar = filtered_rows['FT_Goals_H'].std().round(2)
            cv_mar = (desv_pad_mar / media_gols_mar ).round(2)
            media_gols_sof  = filtered_rows['FT_Goals_A'].mean().round(2)
            media_gols_sfr_ht_sum  = filtered_rows['HT_Goals_A'].sum()            
            desv_pad_sof = filtered_rows['FT_Goals_A'].std().round(2)
            cv_sof = (desv_pad_sof / media_gols_sof ).round(2)   
            total_matches = len(filtered_rows)

            away_win_ht = filtered_rows.apply(lambda row: 1 if row['HT_Goals_H'] > row['HT_Goals_A'] else 0, axis=1)
            draw_ht = filtered_rows.apply(lambda row: 1 if row['HT_Goals_H'] == row['HT_Goals_A'] else 0, axis=1)
            loss_ht = filtered_rows.apply(lambda row: 1 if row['HT_Goals_H'] < row['HT_Goals_A'] else 0, axis=1)

            porc_win_ht = ((away_win_ht.sum() / total_matches) * 100).round(2)
            porc_draw_ht = ((draw_ht.sum() / total_matches) * 100).round(2)
            porc_loss_ht = ((loss_ht.sum() / total_matches) * 100).round(2)
            catoes_st()
            
            for h_goals in range(5):
                for a_goals in range(5):
                    col_name = f"{h_goals}x{a_goals}"
                    filtered_rows[col_name] = ((filtered_rows['FT_Goals_H'] == h_goals) & (filtered_rows['FT_Goals_A'] == a_goals)).astype(int)
                    
            st.markdown("""---""")                
            st.write( 
                """
                <span style="color: blue">**Atenção 🚨:**</span><br>
                """,
                unsafe_allow_html=True,)
            
            st.write(f"O TIME DA CASA LEVA EM MEDIA -- {media_min_gol} MIN  PARA MARCAR O PRIMEIRO GOL")
            st.write(f"TEM UMA MEDIA DE -- {media_chutes} FINALIZAÇÕES POR PARTIDA  ")
            st.write(f"TEM UMA MEDIA DE -- {media_chutes_fora} CHUTES PRA FORA POR PARTIDA  ")
            st.write(f"TEM UMA SOMA DE GOLS MARCADOS HT -- {media_gols_mar_ht_sum } ")
            st.write(f"TEM UMA SOMA DE GOLS SOFRI HT  -- {media_gols_sfr_ht_sum} ")                
            st.write(f"TEM CV DE GOLS MARCADOS -- {cv_mar}")
            st.write(f"TEM CV DE GOLS SOFRIDOS -- {cv_sof}") 
            st.write(f"TEM CV DE GOLS MARCADOS HT -- {cv_mar_ht}")
            st.write(f"TEM CV DE GOLS SOFRIDOS HT -- {cv_sof_ht}")        
            st.write(f"VENCEU O HT  -- {porc_win_ht} %")   
            st.write(f"EMPATOU O HT  -- {porc_draw_ht} %")
            st.write(f"PERDEU O HT -- {porc_loss_ht} %")                  
            
            st.markdown("""---""")
            st.write( 
                """
                <span style="color: blue">**Placares mais frequentes🎯:**</span><br>
                
                """,
                unsafe_allow_html=True,)
            placares_frequentes = []
            for h_goals in range(5):
                for a_goals in range(5):
                    col_name = f"{h_goals}x{a_goals}"
                    filtered_rows[col_name] = ((filtered_rows['FT_Goals_H'] == h_goals) & (filtered_rows['FT_Goals_A'] == a_goals)).astype(int)
                    porcentagem = (filtered_rows[col_name].sum() / total_matches) * 100
                    if porcentagem >= 10: 
                        placares_frequentes.append((col_name, porcentagem))

            for placar, porcentagem in placares_frequentes:
                st.write(f'Placar {placar}: {porcentagem:.2f} %')
                
            st.write( 
                """
                <span style="color: blue">**Placares mais frequentes HT🎯:**</span><br>
                
                """,
                unsafe_allow_html=True,)    
            placares_frequentes_ht = []
            for h_goals in range(5):
                for a_goals in range(5):
                    col_name = f"HT_{h_goals}x{a_goals}"  # Use um prefixo como 'HT_' para indicar o primeiro tempo
                    filtered_rows[col_name] = ((filtered_rows['HT_Goals_H'] == h_goals) & (filtered_rows['HT_Goals_A'] == a_goals)).astype(int)
                    porcentagem = (filtered_rows[col_name].sum() / total_matches) * 100
                    if porcentagem >= 10: 
                        placares_frequentes_ht.append((col_name, porcentagem))

            for placar, porcentagem in placares_frequentes_ht:
                st.write(f'Placar HT {placar}: {porcentagem:.2f} %')                
                
        else:
            st.write("Não temos informações sobre esse time.")
   
        df_h2h = filtered_rows.copy() 
        df_h2h = df_h2h[
            [               
                "Date",
                "Time",
                "League",
                "Season",
                "Round",
                "Home",
                "Away",
                "HT_Goals_H",
                "HT_Goals_A",
                "FT_Goals_H",
                "FT_Goals_A",
                "Total_Goals_HT",
                "Total_Goals_FT",
                "FT_Odd_H",
                "FT_Odd_D",
                "FT_Odd_A",
            
            
        ]
            
            
            ]   
   
        st.dataframe(df_h2h)    
###################################################################################################################################################        
def catoes_st_away():
    st.markdown("""---""")
    st.markdown("""#""")
    Media_de_Gol_Mar_away = filtered_rows_away.FT_Goals_A.mean().round(2)
    Media_de_Gol_Sofr_away = filtered_rows_away.FT_Goals_H.mean().round(2)
    Media_de_Gol_por_par = (Media_de_Gol_Mar_away + Media_de_Gol_Sofr_away).round(2)
    Media_de_Gol_Mar_away_HT = filtered_rows_away.HT_Goals_A.mean().round(2)
    Media_de_Gol_Sofr_away_HT = filtered_rows_away.HT_Goals_H.mean().round(2)
    Media_de_Gol_por_par_HT = (Media_de_Gol_Mar_away_HT + Media_de_Gol_Sofr_away_HT).round(2)
    total_jogos = len(filtered_rows_away)
    
    Media_de_cantos_Mar_away = filtered_rows_away.FT_Corners_A.mean().round(2)
    Media_de_cantos_Sofr_away = filtered_rows_away.FT_Corners_H.mean().round(2)
    Media_de_cantos_por_par = (Media_de_cantos_Mar_away+ Media_de_cantos_Sofr_away).round(2) 
    
    Media_de_cantos_Mar_away_HT = filtered_rows_away.HT_Corners_A.mean().round(2)
    Media_de_cantos_Sofr_away_HT = filtered_rows_away.HT_Corners_H.mean().round(2)
    Media_de_cantos_HT = (Media_de_cantos_Mar_away_HT + Media_de_cantos_Sofr_away_HT).round(2) 

    Media_de_cartoes_Mar_away = filtered_rows_away.FT_Cartoes_A.mean().round(2)
    Media_de_cartoes_Sofr_away = filtered_rows_away.FT_Cartoes_H.mean().round(2)
    Media_de_cartoes = (Media_de_cartoes_Mar_away + Media_de_cartoes_Sofr_away).round(2) 
        
    
    st.write("**TOTAL JOGOS 🆚:**")
    st.markdown(f"""
        **{total_jogos}**
        """)
    dst01, dst02, dst03, = st.columns(3)
    with dst01:
        st.write("**MEDIA DE GOLS MAR HT ⚽ :**")
        st.info(f"{Media_de_Gol_Mar_away_HT}")
    with dst02:
        st.write("**MEDIA DE GOLS SOFR HT ⚽:**")
        st.info(f"{Media_de_Gol_Sofr_away_HT}")
    with dst03:
        st.write("**MEDIA DE GOLS P. PART. HT⚽:**")
        st.info(f"{Media_de_Gol_por_par_HT}")
            
    
    dst1, dst2, dst3, = st.columns(3)
    with dst1:
        st.write("**MEDIA DE GOLS MAR FT⚽ :**")
        st.info(f"{Media_de_Gol_Mar_away}")
    with dst2:
        st.write("**MEDIA DE GOLS SOFR FT⚽:**")
        st.info(f"{Media_de_Gol_Sofr_away}")
    with dst3:
        st.write("**MEDIA DE GOLS P. PART. FT⚽:**")
        st.info(f"{Media_de_Gol_por_par}")

    dst8, dst9, dst10 = st.columns(3)
    with dst8:
        st.write("**MEDIA DE CANTOS MAR HT ⛳ :**")
        st.info(f"{Media_de_cantos_Mar_away_HT }")
    with dst9:
        st.write("**MEDIA DE CANTOS SOFR HT ⛳:**")
        st.info(f"{Media_de_cantos_Sofr_away_HT}")
    with dst10:
        st.write("**MEDIA DE CANTOS HT.⛳:**")
        st.info(f"{ Media_de_cantos_HT }") 
                
    dst5, dst6, dst7 = st.columns(3)
    with dst5:
        st.write("**MEDIA DE CANTOS MAR FT ⛳ :**")
        st.info(f"{Media_de_cantos_Mar_away }")
    with dst6:
        st.write("**MEDIA DE CANTOS SOFR FT ⛳:**")
        st.info(f"{Media_de_cantos_Sofr_away}")
    with dst7:
        st.write("**MEDIA DE CANTOS P. PART FT.⛳:**")
        st.info(f"{Media_de_cantos_por_par}") 
        
    dst11, dst12, dst13 = st.columns(3)
    with dst11:
        st.write("**MEDIA DE CARTOES A FAVOR 🟨 :**")
        st.info(f"{Media_de_cartoes_Mar_away }")
    with dst12:
        st.write("**MEDIA DE CARTOES  CONTRA FT 🟨 :**")
        st.info(f"{Media_de_cartoes_Sofr_away}")
    with dst13:
        st.write("**MEDIA DE CARTOES P. PART.🟨:**")
        st.info(f"{Media_de_cartoes}") 
        
###############################################################################################################################################        
      
def Analise_Away(): 
    global selected_team_away  
    global filtered_rows_away    
    with st.form("ANALISE AWAY"):
        unique_teams_away = df_filtered_away["Away"].unique()
        
        selected_team_away = st.selectbox("Selecione um time (Away)", unique_teams_away)
        
        botao_form_away = st.form_submit_button("Verificar disponibilidade (Away)")

    if st.button("Limpar (Away)"):
        selected_team_away = None
    if botao_form_away:
        filtered_rows_away = df_filtered_away[
            df_filtered_away["Away"].str.lower() == selected_team_away.lower()
        ]

        filtered_rows_away = filtered_rows_away[
            [
                "Date",
                "Time",
                "League",
                "Season",
                "Round",
                "Home",
                "Away",
                "HT_Goals_H",
                "HT_Goals_A",
                "FT_Goals_H",
                "FT_Goals_A",
                "Total_Goals_HT",
                "Total_Goals_FT",
                "FT_Odd_H",
                "FT_Odd_D",
                "FT_Odd_A",
                "HT_Odd_Over05",
                "HT_Odd_Under05",
                "FT_Odd_Over05",
                "FT_Odd_Under05",
                "FT_Odd_Over15",
                "FT_Odd_Under15",
                "FT_Odd_Over25",
                "FT_Odd_Under25",
                "FT_Odd_Over35",
                "FT_Odd_Under35",
                "FT_Odd_Over45",
                "FT_Odd_Under45",
                "Odd_BTTS_Yes",
                "Odd_BTTS_No",
                "Odds_AH_Neg05_H",
                "Odds_AH_Pos05_A",
                "Odds_AH_Pos05_H",
                "Odds_AH_Neg05_A",
                "Media_Total_2HT_H",
                "Media_Total_2HT_A",
                "CV_Media_Total_2HT_H",
                "CV_Media_Total_2HT_A",
                "PPJ_H",
                "CV_Pontos_H",
                "PPJ_A",
                "CV_Pontos_A",
                "FT_Corners_H",
                "FT_Corners_A",
                "HT_Corners_H",
                "HT_Corners_A",
                "FT_Cartoes_H",
                "FT_Cartoes_A",
                "Goals_Minutes_Home",
                "Goals_Minutes_Away",
                "GM_H",
                "GM_A",
                "GS_H",
                "GS_A",
                "Media_GM_H",
                "Media_GM_A",
                "Media_GS_H",
                "Media_GS_A",
                "Media_GM_H_10",
                "Media_GM_A_10",
                "Media_GS_H_10",
                "Media_GS_A_10",
                "Media_primeiro_gol_home",
                "Media_primeiro_gol_away",
                "primeiro_gol_home",
                "primeiro_gol_away",
                "Media_primeiro_gol_away_sofrido",
                "Media_primeiro_gol_home_sofrido",
                "Power_home",
                "Power_away",
                "FT_Finalizações_H",
                "FT_Finalizações_A",
                "HT_Finalizações_H",
                "HT_Finalizações_A",
                "FT_Chutes_fora_H",
                "FT_Chutes_fora_A",
                "HT_Chutes_fora_H",
                "HT_Chutes_fora_A",
                "media_chutes_por_gol_H",
                "media_chutes_por_gol_A",
                "media_movel_chutes_por_gol_H",
                "media_movel_chutes_por_gol_A",
            ]
        ]

        filtered_rows_away = filtered_rows_away.drop_duplicates()

        filtered_rows_away["Date"] = pd.to_datetime(
            filtered_rows_away["Date"], format="%d/%m/%Y", errors="coerce"
        )


        filtered_rows_away = filtered_rows_away.sort_values(by=["Date"])
        filtered_rows_away.index = filtered_rows_away.index + 1
        filtered_rows_away.index.name = "Nº"
         
        if not filtered_rows_away.empty:
            st.write("Temos informações sobre esse time:")
            filtered_rows_away = filtered_rows_away.tail(10)
            media_chutes = filtered_rows_away['FT_Finalizações_A'].mean().round(2)
            media_chutes_fora = filtered_rows_away['FT_Chutes_fora_A'].mean().round(2)
            media_min_gol = filtered_rows_away['primeiro_gol_away'].mean().round(2)

            media_gols_mar_ht  = filtered_rows_away['HT_Goals_A'].mean().round(2)
            media_gols_mar_ht_sum  = filtered_rows_away['HT_Goals_A'].sum()
            desv_pad_mar_ht = filtered_rows_away['HT_Goals_A'].std().round(2)
            cv_mar_ht = (desv_pad_mar_ht / media_gols_mar_ht ).round(2)
            media_gols_sof_ht  = filtered_rows_away['HT_Goals_H'].mean().round(2)
            media_gols_sfr_ht_sum  = filtered_rows_away['HT_Goals_H'].sum()
            desv_pad_sof_ht = filtered_rows_away['HT_Goals_H'].std().round(2)
            cv_sof_ht = (desv_pad_sof_ht / media_gols_sof_ht ).round(2) 
              
            media_gols_mar  = filtered_rows_away['FT_Goals_A'].mean().round(2)
            desv_pad_mar = filtered_rows_away['FT_Goals_A'].std().round(2)
            cv_mar = (desv_pad_mar / media_gols_mar ).round(2)
            media_gols_sof  = filtered_rows_away['FT_Goals_H'].mean().round(2)
            desv_pad_sof = filtered_rows_away['FT_Goals_H'].std().round(2)
            cv_sof = (desv_pad_sof / media_gols_sof ).round(2)  
            
            total_matches = len(filtered_rows_away)  # Total de partidas

            away_win_ht = filtered_rows_away.apply(lambda row: 1 if row['HT_Goals_H'] < row['HT_Goals_A'] else 0, axis=1)
            draw_ht = filtered_rows_away.apply(lambda row: 1 if row['HT_Goals_H'] == row['HT_Goals_A'] else 0, axis=1)
            loss_ht = filtered_rows_away.apply(lambda row: 1 if row['HT_Goals_H'] > row['HT_Goals_A'] else 0, axis=1)

            porc_win_ht = ((away_win_ht.sum() / total_matches) * 100).round(2)
            porc_draw_ht = ((draw_ht.sum() / total_matches) * 100).round(2)
            porc_loss_ht = ((loss_ht.sum() / total_matches) * 100).round(2)
                   
            catoes_st_away()
            
            for h_goals in range(5):
                for a_goals in range(5):
                    col_name = f"{h_goals}x{a_goals}"
                    filtered_rows_away[col_name] = ((filtered_rows_away['FT_Goals_H'] == h_goals) & (filtered_rows_away['FT_Goals_A'] == a_goals)).astype(int)
                    
            st.markdown("""---""")                
            st.write( 
                """
                <span style="color: blue">**Atenção 🚨:**</span><br>
                """,
                unsafe_allow_html=True,)
            
            st.write(f"O TIME DA VISITANTE LEVA EM MEDIA -- {media_min_gol} MIN  PARA MARCAR O PRIMEIRO GOL")
            st.write(f"TEM UMA MEDIA DE -- {media_chutes} FINALIZAÇÕES POR PARTIDA  ")
            st.write(f"TEM UMA MEDIA DE -- {media_chutes_fora} CHUTES PRA FORA POR PARTIDA  ")
            st.write(f"TEM UMA SOMA DE GOLS MARCADOS HT -- {media_gols_mar_ht_sum } ")
            st.write(f"TEM UMA SOMA DE GOLS SOFRI HT  -- {media_gols_sfr_ht_sum} ")            
            st.write(f"TEM CV DE GOLS MARCADOS -- {cv_mar}")
            st.write(f"TEM CV DE GOLS SOFRIDOS -- {cv_sof}")   
            st.write(f"TEM CV DE GOLS MARCADOS HT -- {cv_mar_ht}")
            st.write(f"TEM CV DE GOLS SOFRIDOS HT -- {cv_sof_ht}")
            st.write(f"VENCEU O HT  -- {porc_win_ht} %")   
            st.write(f"EMPATOU O HT  -- {porc_draw_ht} %")
            st.write(f"PERDEU O HT -- {porc_loss_ht} %")            
            st.markdown("""---""")
            st.write( 
                """
                <span style="color: blue">**Placares mais frequentes FT🎯:**</span><br>
                
                """,
                unsafe_allow_html=True,)
            
            placares_frequentes = []
            for h_goals in range(5):
                for a_goals in range(5):
                    col_name = f"{h_goals}x{a_goals}"
                    filtered_rows_away[col_name] = ((filtered_rows_away['FT_Goals_H'] == h_goals) & (filtered_rows_away['FT_Goals_A'] == a_goals)).astype(int)
                    porcentagem = (filtered_rows_away[col_name].sum() / total_matches) * 100
                    if porcentagem >= 10: 
                        placares_frequentes.append((col_name, porcentagem))

            for placar, porcentagem in placares_frequentes:
                st.write(f'Placar {placar}: {porcentagem:.2f} %')
            st.write( 
                """
                <span style="color: blue">**Placares mais frequentes HT🎯:**</span><br>
                
                """,
                unsafe_allow_html=True,)    
            placares_frequentes_ht = []
            for h_goals in range(5):
                for a_goals in range(5):
                    col_name = f"HT_{h_goals}x{a_goals}"  # Use um prefixo como 'HT_' para indicar o primeiro tempo
                    filtered_rows_away[col_name] = ((filtered_rows_away['HT_Goals_H'] == h_goals) & (filtered_rows_away['HT_Goals_A'] == a_goals)).astype(int)
                    porcentagem = (filtered_rows_away[col_name].sum() / total_matches) * 100
                    if porcentagem >= 10: 
                        placares_frequentes_ht.append((col_name, porcentagem))

            for placar, porcentagem in placares_frequentes_ht:
                st.write(f'Placar HT {placar}: {porcentagem:.2f} %')
               
        else:
            st.write("Não temos informações sobre esse time.") 
            
        df_h2h = filtered_rows_away.copy() 
        df_h2h = df_h2h[
            [               
                "Date",
                "Time",
                "League",
                "Season",
                "Round",
                "Home",
                "Away",
                "HT_Goals_H",
                "HT_Goals_A",
                "FT_Goals_H",
                "FT_Goals_A",
                "Total_Goals_HT",
                "Total_Goals_FT",
                "FT_Odd_H",
                "FT_Odd_D",
                "FT_Odd_A",
            
            
        ]
            
            
            ]   
   
        st.dataframe(df_h2h)     

st.markdown(
    """
    <span style="color: blue">**FAÇA SUAS ANALISES⭐**</span><br>
    <span style="color: green">*SELECIONE UMA EQUIPE!!!*</span>  
    """,
    unsafe_allow_html=True,
)            
            
           
tab1, tab2 = st.tabs(["Informações Time Mandante", "informações Time Visitante"])
with tab1:
    Analise_Home()
            
with tab2:
    Analise_Away()            
    
  