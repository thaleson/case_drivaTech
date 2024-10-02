import pandas as pd
from sklearn.cluster import KMeans
import streamlit as st
import plotly.express as px

def run():
    st.title("👥 Segmentação de Clientes")

    # Carregando os dados
    vendas = pd.read_csv('data/VENDAS.csv', delimiter=';')
    clientes = pd.read_csv('data/CLIENTES.csv', delimiter=';')

    # Convertendo o valor das vendas
    vendas['VALOR_VENDA'] = vendas['VALOR_VENDA'].str.replace('.', '').str.replace(',', '.').astype(float)

    # Agrupando vendas por cliente
    total_gasto = vendas.groupby('ID_CLIENTE')['VALOR_VENDA'].sum().reset_index()
    total_gasto.columns = ['ID_CLIENTE', 'total_gasto']

    # Juntando dados de clientes com o total gasto
    clientes_completo = clientes.merge(total_gasto, on='ID_CLIENTE', how='left').fillna(0)

    # Exibindo os dados
    st.write(clientes_completo)

    # Segmentação com K-Means
    kmeans = KMeans(n_clusters=3, random_state=42)
    clientes_completo['cluster'] = kmeans.fit_predict(clientes_completo[['total_gasto']])

    # Cores mais suaves para os clusters
    color_map = {0: 'lightblue', 1: 'lightgreen', 2: 'lightcoral'}
    clientes_completo['cluster_color'] = clientes_completo['cluster'].map(color_map)

    # Plotando os clusters com Plotly para gráficos mais interativos
    fig = px.scatter(
        clientes_completo, 
        x='ID_CLIENTE', 
        y='total_gasto', 
        color='cluster', 
        color_discrete_map=color_map,
        title='Segmentação de Clientes por Total Gasto',
        labels={'ID_CLIENTE': 'ID do Cliente', 'total_gasto': 'Total Gasto (R$)'},
        template='plotly_dark'
    )

    # Exibindo o gráfico
    st.plotly_chart(fig)

    # Adicionando a legenda personalizada abaixo do gráfico com quadrados coloridos
    st.markdown(
        """
        <div style=padding: 15px; border-radius: 8px; margin-top: 15px;'>
            <h4 style='color: #FFFFFF;'>LEGENDA:</h4>
            <ul style='list-style-type: none; padding-left: 0;'>
                <li><span style= padding: 10px; border-radius: 3px; color: #000;'>🔵 Grupo Azul Claro</span> - Grupo com menor gasto (menos de R$ 1.000).</li>
                <li><span style= padding: 10px; border-radius: 3px; color: #000;'>🟢 Grupo Verde Claro</span> - Grupo com gasto moderado (~ R$ 5.000).</li>
                <li><span style= padding: 10px; border-radius: 3px; color: #000;'>🔴 Grupo Coral Claro</span> - Grupo com maior gasto (acima de R$ 20.000).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )

        # Análise abaixo do gráfico
    st.markdown(
        """
        <div style= padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4 style='text-align: center; color: #007BFF;'>🔍 Análise da Segmentação de Clientes</h4>
            <div style='display: flex; justify-content: space-around; flex-wrap: wrap; margin-top: 20px;'>
                <div style='flex: 1; min-width: 250px; margin: 10px; background-color: #ADD8E6; padding: 15px; border-radius: 10px;'>
                    <h5 style='color: #00008B;'>🔵 Grupo Azul Claro</h5>
                    <p style='color: #000;'>Este grupo apresenta o menor gasto médio, abaixo de R$ 1.000. É fundamental identificar os motivos por trás desse comportamento e explorar maneiras de incentivar esse segmento a aumentar seu investimento.</p>
                </div>
                <div style='flex: 1; min-width: 250px; margin: 10px; background-color: #98FB98; padding: 15px; border-radius: 10px;'>
                    <h5 style='color: #006400;'>🟢 Grupo Verde Claro</h5>
                    <p style='color: #000;'>O grupo verde claro está na média, com um gasto médio de R$ 5.000. Isso indica um potencial considerável para o aumento de engajamento e fidelização. Estratégias personalizadas podem ser eficazes para elevar o gasto desse grupo.</p>
                </div>
                <div style='flex: 1; min-width: 250px; margin: 10px; background-color: #F08080; padding: 15px; border-radius: 10px;'>
                    <h5 style='color: #8B0000;'>🔴 Grupo Coral Claro</h5>
                    <p style='color: #000;'>Este grupo é o que apresenta o maior gasto médio, próximo de R$ 20.000. Isso sugere que os clientes deste segmento são altamente engajados e provavelmente respondem bem a campanhas de marketing e promoções.</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True
    )


        # Recomendações
    st.markdown(
        """
        <div style= padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4 style='color: #007BFF; text-align: center;'>💡 Recomendações Estratégicas</h4>
            <div style='display: flex; flex-wrap: wrap; justify-content: space-around;'>
                <div style='flex: 1; min-width: 250px; margin: 10px; background-color: #E9F7EF; padding: 15px; border-radius: 10px;'>
                    <h5 style='color: #28A745;'>📊 Análise de Produtos</h5>
                    <p style='color: #155724;'>Avaliar os produtos mais vendidos para cada grupo de clientes e otimizar o portfólio de ofertas.</p>
                </div>
                <div style='flex: 1; min-width: 250px; margin: 10px; background-color: #E3F2FD; padding: 15px; border-radius: 10px;'>
                    <h5 style='color: #007BFF;'>🎯 Campanhas Personalizadas</h5>
                    <p style='color: #1A73E8;'>Criar campanhas de marketing focadas nas preferências e comportamentos de cada segmento.</p>
                </div>
                <div style='flex: 1; min-width: 250px; margin: 10px; background-color: #FFF3CD; padding: 15px; border-radius: 10px;'>
                    <h5 style='color: #856404;'>🚚 Estratégia de Distribuição</h5>
                    <p style='color: #856404;'>Ajustar a distribuição de produtos com base na localização dos clientes e nas tendências de demanda.</p>
                </div>
                <div style='flex: 1; min-width: 250px; margin: 10px; background-color: #F8D7DA; padding: 15px; border-radius: 10px;'>
                    <h5 style='color: #DC3545;'>💼 Fidelização de Clientes</h5>
                    <p style='color: #721C24;'>Implementar programas de fidelidade para reter clientes de alto valor e aumentar a recorrência de compras.</p>
                </div>
                <div style='flex: 1; min-width: 250px; margin: 10px; background-color: #F3E5F5; padding: 15px; border-radius: 10px;'>
                    <h5 style='color: #6F42C1;'>📢 Feedback dos Clientes</h5>
                    <p style='color: #5A189A;'>Coletar feedback para entender melhor as necessidades dos clientes e aprimorar as ofertas.</p>
                </div>
                <div style='flex: 1; min-width: 250px; margin: 10px; background-color: #EBEDEF; padding: 15px; border-radius: 10px;'>
                    <h5 style='color: #343A40;'>📈 Análise Contínua</h5>
                    <p style='color: #343A40;'>Monitorar continuamente as vendas e ajustar as estratégias de marketing com base nos resultados.</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True
    )


# Chamar a função run para executar o app
if __name__ == "__main__":
    run()
