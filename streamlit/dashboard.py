import streamlit as st        
import pandas as pd           
df = pd.read_csv("veiculos.csv" , encoding='latin-1', sep=';')

#Rename columns
df.rename(columns={"Frota de Veículos - Total (número)": "Frota", 
                   "Acidentes de Trânsito - Total (número)": "Acidentes"}, inplace=True)

#Taxa de Acidentes por Frota
df["Taxa_Acidentes_por_frota"] = (df["Acidentes"] / df["Frota"]) * 100


#taxa de Crescimento da frota para cada localidade
df["Crescimento_frota"] = df["Frota"].pct_change() * 100
df.loc[df['Ano'] == 2008, 'Crescimento_frota'] = None


#taxa de Crescimento de Acidentes
df["Crescimento_acidentes"] = df["Acidentes"].pct_change() * 100
df.loc[df['Ano'] == 2008, 'Crescimento_acidentes'] = None


#iniciar o dashboard
# Configuração do layout da tabela na página
st.set_page_config(layout="wide")

# Configuração do título
st.title('Dashboard Frota por Acidentes - Goiás - 2008-2012')


# Cria um widget de seleção para escolher a localidade
# Removendo espaços antes e depois dos nomes das localidades (strip)
df["Localidade"] = df["Localidade"].astype(str).str.strip()


# Atualizar lista de localidades após limpeza
localidades = df["Localidade"].unique().tolist()
# Opção Todos para seleção
opcoes_localidade = ["Todos"] + localidades
localidade_selecionada = st.sidebar.selectbox("Selecione a Localidade:", opcoes_localidade)

if localidade_selecionada == "Todos": st.dataframe(df)
else: st.dataframe(df[df["Localidade"] == localidade_selecionada])


#Definindo o layout do gráfico, primeira linha com 2 colunas
col1, col2 = st.columns(2)
#Segunda linha com 3 colunas
col3, col4 = st.columns(2)

with col1:
    # Filtro para localidade escolhida
    if localidade_selecionada == "Todos":
        # Calcula média por ano
        
        st.write("### Média de acidentes por ano (Todas as localidades):")
        acidentes = df.groupby("Ano")["Acidentes"].mean() 
        st.bar_chart(acidentes)
    else:
        df_local = df[df["Localidade"] == localidade_selecionada]
        acidentes = df_local.groupby("Ano")["Acidentes"].mean()
        st.write(f"### Média de acidentes por ano ({localidade_selecionada}):")
        st.bar_chart(acidentes)

with col2:
    st.write("### Taxa de Acidentes por Frota")
    
    if localidade_selecionada == "Todos":
        taxa_acidentes_frota = df.groupby("Ano")["Taxa_Acidentes_por_frota"].mean()
    else:
        taxa_acidentes_frota = df_local.groupby("Ano")["Taxa_Acidentes_por_frota"].mean()
    st.line_chart(taxa_acidentes_frota)
    


with col3:
    st.write("### Taxa de Crescimento de Acidentes")
    
    if localidade_selecionada == "Todos":
        taxa_acidentes = df.groupby("Ano")["Crescimento_acidentes"].mean()
    else:
        taxa_acidentes = df_local.groupby("Ano")["Crescimento_acidentes"].mean()
    st.line_chart(taxa_acidentes)


with col4:
    st.write("### Taxa de Crescimento da Frota")
    
    if localidade_selecionada == "Todos":
        taxa_frota = df.groupby("Ano")["Crescimento_frota"].mean()
    else:
        taxa_frota = df_local.groupby("Ano")["Crescimento_frota"].mean()
        print(taxa_frota)
    st.line_chart(taxa_frota)
