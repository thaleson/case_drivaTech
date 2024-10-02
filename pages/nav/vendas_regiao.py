import streamlit as st
import pandas as pd
import plotly.express as px

def run():
    st.title("📍 Vendas por Região")

    # Carregando os dados
    vendas = pd.read_csv('data/VENDAS.csv', delimiter=';')
    filiais = pd.read_csv('data/FILIAIS.csv', delimiter=';')

    # Limpeza dos dados
    vendas['VALOR_VENDA'] = vendas['VALOR_VENDA'].astype(str).str.replace('.', '').str.replace(',', '.').astype(float)
    vendas = vendas.drop_duplicates()
    vendas['DATA_VENDA'] = pd.to_datetime(vendas['DATA_VENDA'], format='%d/%m/%Y')

    # Mesclando vendas com filiais
    vendas_filiais = vendas.merge(filiais, on='ID_FILIAL')

    # Agrupando vendas por UF
    vendas_por_uf = vendas_filiais.groupby('UF')['VALOR_VENDA'].sum().reset_index()

    # ---- Gráfico 1: Vendas por UF ----
    st.subheader("Vendas por Unidade Federativa (UF)")
    st.markdown("""O gráfico abaixo apresenta o valor total das vendas por UF. Este gráfico é útil para identificar onde estão localizados os maiores mercados e oportunidades.""")

    # Criando o gráfico de barras
    fig1 = px.bar(vendas_por_uf, x='UF', y='VALOR_VENDA',
                  title='Vendas por UF',
                  labels={'VALOR_VENDA': 'Valor das Vendas (R$)', 'UF': 'UF'},
                  color='VALOR_VENDA',
                  color_continuous_scale=px.colors.qualitative.Plotly)  # Usando a paleta Plotly

    st.plotly_chart(fig1)

    # ---- Gráfico 2: Vendas ao Longo do Tempo por UF ----
    st.subheader("Vendas ao Longo do Tempo por UF")
    st.markdown("""Este gráfico mostra como as vendas se comportam ao longo do tempo, separadas por UF. Ele pode revelar sazonalidades ou picos de vendas em certas regiões.""")

    vendas_por_data_uf = vendas_filiais.groupby(['DATA_VENDA', 'UF'])['VALOR_VENDA'].sum().reset_index()

    # Criando o gráfico de linha
    fig2 = px.line(vendas_por_data_uf, x='DATA_VENDA', y='VALOR_VENDA', color='UF',
                   title='Vendas ao Longo do Tempo por UF',
                   labels={'VALOR_VENDA': 'Valor Total das Vendas (R$)', 'DATA_VENDA': 'Data da Venda'},
                   markers=True)

    st.plotly_chart(fig2)

    # ---- Análise do desempenho de vendas por UF ----
    st.markdown(
        """
        <div style='background-color: #1a1a1a; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4 style='color: #f0db4f;'>📊 Análise do Desempenho de Vendas por Região:</h4>
            <p style='color: #ffffff;'>O gráfico acima mostra o total de vendas agrupadas por Unidade Federativa (UF). Vamos explorar alguns pontos importantes:</p>
            <p style='color: #ffffff;'><strong>UF com maior desempenho:</strong> A região que se destaca com um total de vendas significativo é <strong style='color: #ffcc00;'>Paraná (PR)</strong>. Com vendas que alcançam até <strong>R$ 4 milhões</strong>, PR é um mercado crucial e representa uma grande oportunidade para expandir estratégias de marketing e aumentar a penetração de mercado.</p>
            <p style='color: #ffffff;'><strong>Regiões com vendas moderadas:</strong> Estados como <strong style='color: #ffcc00;'>Minas Gerais (MG)</strong> e <strong style='color: #ffcc00;'>Rio de Janeiro (RJ)</strong> também mostram um desempenho notável, com vendas variando em torno de <strong>R$ 2 milhões</strong>. Essas regiões devem ser priorizadas em campanhas promocionais e eventos locais, visando engajar ainda mais os consumidores.</p>
            <p style='color: #ffffff;'><strong>Regiões com baixo desempenho:</strong> Por outro lado, estados com vendas em torno de <strong>R$ 0 a R$ 1 milhão</strong>, como <strong style='color: #ffcc00;'>Piauí (PI)</strong> e <strong style='color: #ffcc00;'>Alagoas (AL)</strong>, apresentam desafios. Nesses casos, é essencial investigar as causas desse baixo desempenho e avaliar a possibilidade de adaptar ofertas ou fortalecer a presença de mercado.</p>
            <p style='color: #ffffff;'><strong>Tendências ao longo do tempo:</strong> O gráfico de vendas ao longo do tempo revela tendências que podem ser úteis para planejar estoques e promoções. Observe que algumas UFs podem ter picos de vendas em determinados períodos, indicando sazonalidade que pode ser explorada em campanhas futuras.</p>
            <p style='color: #ffffff;'>Em suma, a análise das vendas por região oferece insights valiosos que podem guiar as decisões estratégicas da empresa. Ao entender quais regiões apresentam maiores oportunidades e quais precisam de atenção, é possível direcionar esforços de vendas e marketing de forma mais eficiente.</p>
        </div>
        """, unsafe_allow_html=True
    )

# Chame a função run() para executar o script
if __name__ == "__main__":
    run()
