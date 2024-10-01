import streamlit as st
import json
from streamlit_lottie import st_lottie

def run():
    st.title("📊 Análise de Dados - DrivaTech")


    # Colunas que organizam a página
    col1, col2 = st.columns(2)

    # Carregando animações
    with open("assets/pagina_inicial1.json") as source:
        animacao_1 = json.load(source)

    with open("assets/animation1.json") as source:
        animacao_2 = json.load(source)

    # Conteúdo a ser exibido na coluna 1
    with col1:
        st_lottie(animacao_1, height=350, width=400)
        st.markdown("<h5 style='text-align: justify;'>Este projeto é uma aplicação web desenvolvida para analisar o desempenho de vendas e o comportamento do consumidor. Através de visualizações interativas, você poderá entender melhor as tendências de vendas e segmentar clientes, o que ajudará na otimização de estratégias de marketing e distribuição de produtos.</h5>", unsafe_allow_html=True)

    # Conteúdo a ser exibido na coluna 2
    with col2:
        st.markdown("<h5 style='text-align: justify;'>Bem-vindo à Análise de Vendas da DrivaTech! 🎉</h5>", unsafe_allow_html=True)
        st_lottie(animacao_2, height=500, width=540)

    # Texto de boas-vindas
    st.success("""
    Aqui você encontrará insights detalhados sobre o desempenho de vendas, segmentação de clientes e feedbacks, tudo com o objetivo de otimizar estratégias de marketing e distribuição de produtos.
    """)


# Chame a função run() para executar o script
if __name__ == "__main__":
    run()
