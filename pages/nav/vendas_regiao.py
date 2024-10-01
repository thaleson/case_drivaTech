import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    st.markdown("""
    O gráfico abaixo apresenta o valor total das vendas por UF. Este gráfico é útil para identificar onde estão localizados os maiores mercados e oportunidades.
    """)

    fig, ax = plt.subplots(figsize=(8, 8))
    sns.barplot(data=vendas_por_uf, x='UF', y='VALOR_VENDA', palette='viridis', ax=ax)
    ax.set_title('Vendas por UF', fontsize=16, pad=20)  # O valor 20 aumenta a distância

    ax.set_xlabel('UF', fontsize=14)
    ax.set_ylabel('Valor das Vendas (R$)', fontsize=14)

    # Adicionando rótulos nas barras
    for index, row in vendas_por_uf.iterrows():
        ax.text(row.name, row.VALOR_VENDA + 0.05 * max(vendas_por_uf.VALOR_VENDA),
                f'R$ {row.VALOR_VENDA:,.2f}', color='black', ha='center', fontsize=10)

    st.pyplot(fig)

    # ---- Gráfico 2: Vendas ao Longo do Tempo por UF ----
    st.subheader("Vendas ao Longo do Tempo por UF")
    st.markdown("""
    Este gráfico mostra como as vendas se comportam ao longo do tempo, separadas por UF. Ele pode revelar sazonalidades ou picos de vendas em certas regiões.
    """)

    vendas_por_data_uf = vendas_filiais.groupby(['DATA_VENDA', 'UF'])['VALOR_VENDA'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=vendas_por_data_uf, x='DATA_VENDA', y='VALOR_VENDA', hue='UF', marker='o', ax=ax)
    ax.set_title('Vendas ao Longo do Tempo por UF', fontsize=16 )
    ax.set_xlabel('Data da Venda', fontsize=14)
    ax.set_ylabel('Valor Total das Vendas (R$)', fontsize=14)
    ax.legend(title='UF', bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot(fig)

    # ---- Gráfico 3: Top 5 UFs com Maior Vendas ----
    st.subheader("Top 5 UFs com Maior Vendas")
    st.markdown("""
    Aqui estão as 5 UFs com o maior valor total de vendas. Esse gráfico destaca as regiões mais lucrativas.
    """)

    top_5_ufs = vendas_por_uf.nlargest(5, 'VALOR_VENDA')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=top_5_ufs, x='UF', y='VALOR_VENDA', palette='magma', ax=ax)
    ax.set_title('Top 5 UFs com Maior Vendas', fontsize=16 ,pad=20)
    ax.set_xlabel('UF', fontsize=14)
    ax.set_ylabel('Valor das Vendas (R$)', fontsize=14)

    # Adicionando rótulos nas barras
    for index, row in top_5_ufs.iterrows():
        ax.text(row.name, row.VALOR_VENDA + 0.05 * max(top_5_ufs.VALOR_VENDA),
                f'R$ {row.VALOR_VENDA:,.2f}', color='black', ha='center', fontsize=10)

    st.pyplot(fig)

    # ---- Análise do desempenho de vendas por UF ----
    st.markdown(
        """
        <div style='background-color: #0000FF; padding: 15px; border-radius: 8px; margin-top: 20px;'>
            <h4>📊 Análise do Desempenho de Vendas por Região:</h4>
            <p>O gráfico acima mostra o total de vendas agrupadas por Unidade Federativa (UF). Vamos explorar alguns pontos importantes:</p>
            <p><strong>UF com maior desempenho:</strong> A região que se destaca com um total de vendas significativo é <strong>São Paulo (SP)</strong>. Com vendas que alcançam até <strong>R$ 4 milhões</strong>, SP é um mercado crucial e representa uma grande oportunidade para expandir estratégias de marketing e aumentar a penetração de mercado.</p>
            <p><strong>Regiões com vendas moderadas:</strong> Estados como <strong>Minas Gerais (MG)</strong> e <strong>Rio de Janeiro (RJ)</strong> também mostram um desempenho notável, com vendas variando em torno de <strong>R$ 2 milhões</strong>. Essas regiões devem ser priorizadas em campanhas promocionais e eventos locais, visando engajar ainda mais os consumidores.</p>
            <p><strong>Regiões com baixo desempenho:</strong> Por outro lado, estados com vendas em torno de <strong>R$ 0 a R$ 1 milhão</strong>, como <strong>Piauí (PI)</strong> e <strong>Alagoas (AL)</strong>, apresentam desafios. Nesses casos, é essencial investigar as causas desse baixo desempenho e avaliar a possibilidade de adaptar ofertas ou fortalecer a presença de mercado.</p>
            <p><strong>Tendências ao longo do tempo:</strong> O gráfico de vendas ao longo do tempo revela tendências que podem ser úteis para planejar estoques e promoções. Observe que algumas UFs podem ter picos de vendas em determinados períodos, indicando sazonalidade que pode ser explorada em campanhas futuras.</p>
            <p><strong>Top 5 UFs:</strong> A análise dos cinco principais estados em vendas destaca os mercados mais lucrativos e onde o foco das estratégias de vendas deve ser reforçado.</p>
            <p>Em suma, a análise das vendas por região oferece insights valiosos que podem guiar as decisões estratégicas da empresa. Ao entender quais regiões apresentam maiores oportunidades e quais precisam de atenção, é possível direcionar esforços de vendas e marketing de forma mais eficiente.</p>
        </div>
        """, unsafe_allow_html=True
    )

# Chame a função run() para executar o script
if __name__ == "__main__":
    run()
