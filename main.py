import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="DrivaTech Dashboard", layout="wide", page_icon="📊")

# Cabeçalho
st.sidebar.image("assets/images/logo2.jpg", width=250)

# Aplicar estilos de CSS à página (se houver)
try:
    with open("static/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Arquivo de estilo CSS não encontrado!")

st.sidebar.title("DrivaTech Dashboard")

# Menu de Navegação
with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=["Home", "Vendas por Região", "Desempenho de Vendas por Filial", "Segmentação de Clientes", "Análise de Dados de Clientes", "Previsão das vendas"],
        icons=["house", "bar-chart", "box-seam", "people", "chat", "check-circle"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
    )

# Navegação entre as páginas
if selected == "Home":
    from pages.nav.home import run
    run()
elif selected == "Vendas por Região":
    from pages.nav.vendas_regiao import run
    run()
elif selected == "Desempenho de Vendas por Filial":
    from pages.nav.desempenho_produtos import run
    run()
elif selected == "Segmentação de Clientes":
    from pages.nav.segmentacao_clientes import run
    run()
elif selected == "Análise de Dados de Clientes":
    from pages.nav.analise_dados import run
    run()
elif selected == "Previsão das vendas" :
    from pages.nav.previsao import run
    run()
