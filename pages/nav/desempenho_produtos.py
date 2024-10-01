import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.title("📦 Desempenho de Vendas por Filial")
    
    # Carregando os dados
    vendas = pd.read_csv('data/VENDAS.csv', delimiter=';')
    filiais = pd.read_csv('data/FILIAIS.csv', delimiter=';')

    # Limpeza dos dados
    vendas['VALOR_VENDA'] = vendas['VALOR_VENDA'].astype(str).str.replace('.', '').str.replace(',', '.').astype(float)
    vendas = vendas.drop_duplicates()

    # Agrupando vendas por filial
    vendas_por_filial = vendas.groupby('ID_FILIAL')['VALOR_VENDA'].sum().reset_index()
    vendas_por_filial = vendas_por_filial.merge(filiais[['ID_FILIAL', 'NOME_FILIAL']], on='ID_FILIAL')

    # Plotando
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(data=vendas_por_filial, x='NOME_FILIAL', y='VALOR_VENDA', palette='magma', ax=ax)
    ax.set_title('Total de Vendas por Filial')
    ax.set_xlabel('Filial')
    ax.set_ylabel('Valor Total das Vendas (R$)')
    st.pyplot(fig)

    # Análise do desempenho de produtos por filial
    st.markdown(
        """
        ### Análise de Vendas por Filial

        O gráfico mostra o total de vendas em reais (R$) de cinco filiais diferentes: **BATEL**, **AGUA VERDE**, **UBERABA**, **CABRAL** e **BOM RETIRO**. Aqui está uma análise detalhada:

        1. **BATEL**:
           - **Desempenho**: Esta filial lidera com folga, alcançando cerca de 1,6 milhões de reais em vendas.
           - **Interpretação**: O alto volume de vendas pode indicar uma localização estratégica, uma equipe de vendas eficiente ou uma base de clientes fiel.

        2. **AGUA VERDE**:
           - **Desempenho**: Segunda colocada, com vendas significativas, mas ainda abaixo de BATEL.
           - **Interpretação**: Embora não tão alta quanto BATEL, esta filial também demonstra um bom desempenho, possivelmente devido a fatores semelhantes.

        3. **UBERABA** e **CABRAL**:
           - **Desempenho**: Ambas as filiais têm vendas semelhantes, mas consideravelmente menores que BATEL e AGUA VERDE.
           - **Interpretação**: Pode ser necessário investigar se há desafios específicos nessas regiões, como menor demanda ou concorrência mais acirrada.

        4. **BOM RETIRO**:
           - **Desempenho**: Esta filial tem o menor volume de vendas.
           - **Interpretação**: A baixa performance pode ser um sinal de problemas que precisam ser abordados, como localização desfavorável, estratégias de marketing ineficazes ou necessidade de treinamento da equipe.

        ### Conclusão

        Ao analisar esses dados, é importante lembrar que cada filial é composta por pessoas que trabalham duro para alcançar seus objetivos. As diferenças de desempenho podem ser influenciadas por diversos fatores, incluindo o ambiente de trabalho, a motivação da equipe e as condições econômicas locais. 

        ### Próximos Passos

        1. **Para BATEL e AGUA VERDE**: Continuar investindo nas estratégias que estão funcionando bem e explorar oportunidades para aumentar ainda mais as vendas.
        2. **Para UBERABA e CABRAL**: Realizar uma análise mais detalhada para identificar áreas de melhoria e implementar ações específicas para aumentar as vendas.
        3. **Para BOM RETIRO**: Investigar profundamente os motivos da baixa performance e desenvolver um plano de ação focado em reverter essa situação.
        """, unsafe_allow_html=True
    )

# Chame a função run() para executar o script
if __name__ == "__main__":
    run()
