import pandas as pd
from sklearn.cluster import KMeans
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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

    # Plotando os clusters
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=clientes_completo, x='ID_CLIENTE', y='total_gasto', hue='cluster', palette=['yellow', 'purple', 'green'])
    plt.title('Segmentação de Clientes')
    plt.xlabel('ID Cliente')
    plt.ylabel('Total Gasto (R$)')
    st.pyplot(plt)

    # Análise abaixo do gráfico
    st.markdown(
        """
        <div style='background-color: #0000FF; padding: 15px; border-radius: 8px; margin-top: 15px; margin-bottom: 10px;'>
            <h4>🔍 Análise da Segmentação de Clientes:</h4>
            <p><strong>Grupo Amarelo:</strong> Este grupo é o que apresenta o maior gasto médio, próximo de R$ 20.000. Isso sugere que os clientes deste segmento são altamente engajados e provavelmente respondem bem a campanhas de marketing e promoções.</p>
            <p><strong>Grupo Roxo:</strong> O grupo roxo está na média, com um gasto médio de R$ 5.000. Isso indica um potencial considerável para o aumento de engajamento e fidelização. Estratégias personalizadas podem ser eficazes para elevar o gasto desse grupo.</p>
            <p><strong>Grupo Verde:</strong> Este grupo apresenta o menor gasto médio, abaixo de R$ 1.000. É fundamental identificar os motivos por trás desse comportamento e explorar maneiras de incentivar esse segmento a aumentar seu investimento.</p>
        </div>
        """, unsafe_allow_html=True
    )

    # Recomendações
    st.markdown(
        """
        <div style='background-color: #e2f0d9; padding: 15px; border-radius: 8px; margin-top: 15px;'>
            <h4 style='color: #155724;'>Recomendações Estratégicas:</h4>
            <ul style='list-style-type: none; padding: 0;'>
                <li style='color: #4CAF50;'><strong>Análise de Produtos:</strong> Avaliar quais produtos são mais vendidos para cada grupo de clientes.</li>
                <li style='color: #2196F3;'><strong>Campanhas Personalizadas:</strong> Desenvolver campanhas de marketing específicas para cada grupo, levando em consideração suas preferências e comportamento de compra.</li>
                <li style='color: #FF9800;'><strong>Estratégia de Distribuição:</strong> Planejar a distribuição de produtos considerando a localização dos clientes, otimizando assim o alcance das campanhas.</li>
                <li style='color: #F44336;'><strong>Fidelização de Clientes:</strong> Implementar programas de fidelidade para incentivar a repetição de compras entre os clientes de maior gasto.</li>
                <li style='color: #9C27B0;'><strong>Feedback dos Clientes:</strong> Coletar feedback regularmente para entender melhor as necessidades e desejos dos diferentes grupos de clientes.</li>
                <li style='color: #3F51B5;'><strong>Análise Contínua:</strong> Monitorar o desempenho das vendas e a eficácia das campanhas para ajustar estratégias conforme necessário.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )

# Chamar a função run para executar o app
if __name__ == "__main__":
    run()
