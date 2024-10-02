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

  

    # Criando o gráfico de barras
    st.subheader('Vendas por UF')
    fig1 = px.bar(vendas_por_uf, x='UF', y='VALOR_VENDA',
                  labels={'VALOR_VENDA': 'Valor das Vendas (R$)', 'UF': 'UF'},
                  color='VALOR_VENDA',
                  color_continuous_scale=px.colors.qualitative.Plotly)  # Usando a paleta Plotly

    st.plotly_chart(fig1)

        # ---- Gráfico 1: Vendas por UF ----
    st.title("Vendas por Unidade Federativa (UF)")
    st.markdown(
        """
        O gráfico abaixo apresenta o valor total das vendas por UF. Este gráfico é útil para identificar onde estão localizados os maiores mercados e oportunidades.

        **Descrição do Gráfico:**
        - O gráfico é um gráfico de barras intitulado **"Vendas por UF"**.
        - O eixo horizontal representa os estados, como **"PR" (Paraná)**.
        - O eixo vertical representa o valor das vendas em Reais (R$), variando de 0 a 4 milhões.

        **Eixos do Gráfico:**
        - **Eixo X (horizontal):** Representa os estados. Neste caso, temos a sigla **PR** (Paraná).
        - **Eixo Y (vertical):** Representa o valor das vendas em Reais (R$), variando de 0 a 4 milhões.

        **Análise Detalhada:**
        - **Barra PR:**
            - **Valor das Vendas:** A barra correspondente ao estado PR atinge um pouco acima de 4 milhões de Reais.
            - **Consistência dos Dados:** A legenda ao lado do gráfico mostra valores repetidos de 4.398079M R$, o que pode indicar um erro na representação dos dados ou na legenda.
        """
    )


    # ---- Gráfico 2: Vendas ao Longo do Tempo por UF ----

    vendas_por_data_uf = vendas_filiais.groupby(['DATA_VENDA', 'UF'])['VALOR_VENDA'].sum().reset_index()

    # Criando o gráfico de linha
    st.title("Vendas ao Longo do Tempo por UF")
    fig2 = px.line(vendas_por_data_uf, x='DATA_VENDA', y='VALOR_VENDA', color='UF',
                   labels={'VALOR_VENDA': 'Valor Total das Vendas (R$)', 'DATA_VENDA': 'Data da Venda'},
                   markers=True)

    st.plotly_chart(fig2)

        # ---- Análise do desempenho de vendas por UF ----
    st.markdown(
        """
        <div style='background-color: #1a1a1a; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4 style='color: #f0db4f;'>📊 Análise do Desempenho de Vendas ao Longo do Tempo por UF:</h4>
            <p style='color: #ffffff;'>O gráfico abaixo apresenta a evolução das vendas ao longo de três meses, de outubro a dezembro de 2023, com foco em duas UFs específicas: UF e PR.</p>
            <p style='color: #ffffff;'><strong>Linha UF:</strong> Apresenta flutuações moderadas ao longo do tempo, sem grandes picos, indicando uma estabilidade nas vendas.</p>
            <p style='color: #ffffff;'><strong>Linha PR:</strong> Exibe flutuações mais acentuadas, com picos significativos. Esses picos podem estar relacionados a campanhas promocionais ou eventos específicos.</p>
            <p style='color: #ffffff;'><strong>Interpretação:</strong> A UF representa um cenário mais estável, sugerindo consistência nas vendas ao longo do tempo. A PR é mais volátil, com picos que podem ser explorados para identificar o que gerou esse aumento nas vendas e replicar essas estratégias no futuro.</p>
        </div>
        """, unsafe_allow_html=True
    )


# Chame a função run() para executar o script
if __name__ == "__main__":
    run()
