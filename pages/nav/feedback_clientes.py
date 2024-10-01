import streamlit as st
import pandas as pd

def run():
    st.title("🔍 Processamento e Análise de Dados de Clientes")

    # Carregando os dados
    st.header("Carregando os Dados")
    clientes = pd.read_csv('data/CLIENTES.csv', delimiter=';')
    st.write("Dados brutos carregados:")
    st.dataframe(clientes.head())

    # Não há tratamento de idade e renda, então ajustamos a análise com base em cidade e estado (UF)
    st.header("Análise Exploratória")

    # Exibindo a contagem de clientes por cidade
    st.subheader("Distribuição de Clientes por Cidade")
    distribuicao_cidade = clientes['CIDADE'].value_counts()
    st.bar_chart(distribuicao_cidade)

    # Exibindo a contagem de clientes por estado (UF)
    st.subheader("Distribuição de Clientes por Estado (UF)")
    distribuicao_uf = clientes['UF'].value_counts()
    st.bar_chart(distribuicao_uf)

    # Agrupamento e resumo dos dados por UF
    st.subheader("Resumo por Estado (UF)")
    resumo_uf = clientes.groupby('UF').agg({'ID_CLIENTE': 'count'})
    resumo_uf.columns = ['Nº de Clientes']
    st.dataframe(resumo_uf)

    # Conclusão
    st.header("📊 Conclusão")
    st.markdown(
        """
        Após a análise dos dados de clientes, algumas conclusões importantes foram obtidas:
        - A maioria dos clientes está concentrada em certas cidades e estados específicos, o que pode guiar decisões de marketing regional.
        - Com a distribuição por UF, é possível direcionar campanhas e estratégias comerciais de acordo com as regiões que possuem mais clientes.
        
        Essas análises fornecem insights valiosos para entender a localização geográfica dos clientes e potencializar a atuação da empresa em regiões estratégicas.
        """
    )

# Chame a função run() para executar o script
if __name__ == "__main__":
    run()
