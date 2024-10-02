import streamlit as st
import pandas as pd
import plotly.express as px

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

    # ---- Gráfico: Vendas por Filial ----
    st.subheader("Total de Vendas por Filial")
    st.markdown("""O gráfico abaixo mostra o total de vendas por filial. Ele é útil para visualizar rapidamente quais filiais estão se destacando.""")

    # Criando o gráfico de barras com Plotly
    fig = px.bar(vendas_por_filial, x='NOME_FILIAL', y='VALOR_VENDA',
                 title='Total de Vendas por Filial',
                 labels={'VALOR_VENDA': 'Valor Total das Vendas (R$)', 'NOME_FILIAL': 'Filial'},
                 color='VALOR_VENDA',
                 color_continuous_scale=px.colors.sequential.Plasma)  # Usando uma paleta de cores

    st.plotly_chart(fig)

    # Análise do desempenho de produtos por filial
    st.markdown(
        """
        <div style='padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4 style='text-align: center; color: #007BFF;'>📊 Análise de Vendas por Filial</h4>
            <div style='display: flex; justify-content: space-around; flex-wrap: wrap; margin-top: 20px;'>
                <div style='flex: 1; min-width: 250px; margin: 10px; background-color: #ADD8E6; padding: 15px; border-radius: 10px;'>
                    <h5 style='color: #00008B;'>🔵 BATEL</h5>
                    <p style='color: #000;'>Desempenho: Cerca de R$ 1,6 milhões em vendas. <br> Interpretação: Localização estratégica e equipe de vendas eficaz.</p>
                </div>
                <div style='flex: 1; min-width: 250px; margin: 10px; background-color: #98FB98; padding: 15px; border-radius: 10px;'>
                    <h5 style='color: #006400;'>🟢 AGUA VERDE</h5>
                    <p style='color: #000;'>Desempenho: Vendas significativas, mas abaixo de BATEL. <br> Interpretação: Bom desempenho, semelhante a BATEL.</p>
                </div>
                <div style='flex: 1; min-width: 250px; margin: 10px; background-color: #F08080; padding: 15px; border-radius: 10px;'>
                    <h5 style='color: #8B0000;'>🔴 UBERABA e CABRAL</h5>
                    <p style='color: #000;'>Desempenho: Vendas semelhantes, menores que BATEL e AGUA VERDE. <br> Interpretação: Necessita investigar desafios específicos.</p>
                </div>
                <div style='flex: 1; min-width: 250px; margin: 10px; background-color: #FFB6C1; padding: 15px; border-radius: 10px;'>
                    <h5 style='color: #8B0000;'>🔴 BOM RETIRO</h5>
                    <p style='color: #000;'>Desempenho: Menor volume de vendas. <br> Interpretação: Sinais de problemas que precisam ser abordados.</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

    # Conclusões e Próximos Passos
    st.markdown(
        """
        <div style='padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4 style='color: #663399;'>✅ Conclusão e Próximos Passos</h4>
            <ul>
                <li><strong>Para BATEL e AGUA VERDE:</strong> Continuar investindo nas estratégias que estão funcionando e explorar oportunidades.</li>
                <li><strong>Para UBERABA e CABRAL:</strong> Análise detalhada para identificar áreas de melhoria.</li>
                <li><strong>Para BOM RETIRO:</strong> Investigar a baixa performance e desenvolver um plano de ação focado.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )

# Chame a função run() para executar o script
if __name__ == "__main__":
    run()
