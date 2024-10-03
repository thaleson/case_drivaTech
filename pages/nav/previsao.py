import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
import plotly.graph_objs as go

def run():
    st.title("📊 Previsão de Vendas")

    # Carregando os dados
    vendas = pd.read_csv('data/VENDAS.csv', delimiter=';')
    filiais = pd.read_csv('data/FILIAIS.csv', delimiter=';')

    # Limpeza dos dados
    vendas['VALOR_VENDA'] = vendas['VALOR_VENDA'].astype(str).str.replace('.', '').str.replace(',', '.').astype(float)
    vendas['DATA_VENDA'] = pd.to_datetime(vendas['DATA_VENDA'], format='%d/%m/%Y')

    # Extraindo características (features)
    vendas['MÊS'] = vendas['DATA_VENDA'].dt.month
    vendas['ANO'] = vendas['DATA_VENDA'].dt.year
    vendas_filiais = vendas.merge(filiais, on='ID_FILIAL')

    # Agrupando os dados para treinamento
    vendas_por_mes = vendas_filiais.groupby(['MÊS', 'ANO'])['VALOR_VENDA'].sum().reset_index()

    # Criação de variáveis dummy para os meses
    vendas_por_mes = pd.get_dummies(vendas_por_mes, columns=['MÊS'], drop_first=True)

    # Preparação dos dados para o modelo
    X = vendas_por_mes.drop(columns=['VALOR_VENDA'])
    y = vendas_por_mes['VALOR_VENDA']

    # Divisão dos dados
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Criação e treinamento do modelo com regularização
    model = Ridge(alpha=1.0)
    model.fit(X_train, y_train)

    # Previsões para os dados de teste
    y_pred = model.predict(X_test)

    # Avaliação
    rmse = np.sqrt(np.mean((y_pred - y_test) ** 2))
    st.write(f"RMSE: {rmse:.2f}")

    # Gráfico interativo para dados de teste
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=y_test.index, y=y_test, mode='lines+markers', name='Vendas Reais', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=y_test.index, y=y_pred, mode='lines+markers', name='Vendas Previstas', line=dict(color='red')))
    fig.update_layout(title="Comparação entre Vendas Reais e Previstas", xaxis_title="Índice", yaxis_title="Valor das Vendas (R$)")
    st.plotly_chart(fig)

    # Previsão para os próximos anos até 2029
    future_years = np.arange(2023, 2030)  # de 2023 a 2029
    future_months = np.tile(np.arange(1, 13), len(future_years))
    future_years_expanded = np.repeat(future_years, 12)

    future_data = pd.DataFrame({'MÊS': future_months, 'ANO': future_years_expanded})

    # Criação de variáveis dummy para os meses futuros
    future_data = pd.get_dummies(future_data, columns=['MÊS'], drop_first=True)

    # Adicionando colunas faltantes para garantir que o DataFrame futuro tenha a mesma estrutura que o DataFrame de treinamento
    for col in X.columns:
        if col not in future_data.columns:
            future_data[col] = 0  # Adiciona coluna com zero se não estiver presente

    # Realizando previsões futuras
    future_predictions = model.predict(future_data[X.columns])  # Alinhando com as colunas do modelo

    # Ajuste para evitar valores negativos
    future_predictions = np.maximum(future_predictions, 0)  # garante que não haja valores negativos

    # Gráfico interativo para previsões futuras
    future_fig = go.Figure()
    future_fig.add_trace(go.Scatter(x=future_data.index, y=future_predictions, mode='lines+markers', name='Previsões Futuras', line=dict(color='green')))
    future_fig.update_layout(title="Previsões de Vendas até 2029", xaxis_title="Índice", yaxis_title="Valor das Vendas (R$)")
    st.plotly_chart(future_fig)

    # Exibir previsões em tabela
    future_data['VALOR_VENDA_PREVISTA'] = future_predictions
    st.subheader("📈 Tabela de Previsões de Vendas para os próximos 6 anos")
    st.dataframe(future_data)

    # Comentários e Análise

    st.markdown(
            """
            <div style='background-color: #1a1a1a; padding: 20px; border-radius: 10px; margin-top: 20px;'>
                <h4 style='color: #f0db4f;'>🔍 Análise da Previsão de Vendas:</h4>
                <p><strong>Desempenho do Modelo:</strong> O modelo de regressão linear apresentou um RMSE de **{:.2f}**, indicando que, em média, as previsões de vendas se desviam em R$ {:.2f} do valor real.</p>
                <p><strong>Previsões Futuras:</strong></p>
                <p>A tabela acima apresenta as vendas previstas para os próximos 6 anos. A análise dessas previsões pode auxiliar na tomada de decisões estratégicas:</p>
                <ul>
                    <li><strong>Identificação de Tendências:</strong> Analise se há um crescimento constante nas vendas e se esse aumento é sustentável.</li>
                    <li><strong>Planejamento de Estoque:</strong> As previsões ajudam a planejar melhor a produção e o estoque, evitando excessos ou faltas.</li>
                    <li><strong>Estratégias de Marketing:</strong> Use as previsões para ajustar as campanhas de marketing, visando maximizar as vendas em períodos de alta demanda.</li>
                    <li><strong>Monitoramento e Ajustes:</strong> Estabeleça um monitoramento regular das vendas reais em comparação com as previsões e ajuste as estratégias conforme necessário.</li>
                </ul>
                <p><strong>Conclusão:</strong> A previsão de vendas até 2029 é um recurso estratégico vital para a DrivaTech, pois permite que a empresa:</p>
                <ul>
                    <li><strong>Antecipe Tendências de Mercado:</strong> Ao analisar os dados históricos de vendas e prever o comportamento futuro, a DrivaTech pode identificar padrões e tendências, possibilitando decisões informadas sobre onde concentrar esforços de vendas e marketing.</li>
                    <li><strong>Aprimore o Planejamento de Estoque:</strong> Com uma visão clara das vendas projetadas, a DrivaTech pode otimizar seu gerenciamento de estoque, evitando tanto excessos quanto faltas, o que se traduz em economia de custos e satisfação do cliente.</li>
                    <li><strong>Desenvolva Estratégias de Marketing Mais Eficientes:</strong> As previsões ajudam a identificar períodos de alta demanda, permitindo que a DrivaTech direcione suas campanhas de marketing de maneira mais eficaz, maximizando o retorno sobre o investimento.</li>
                    <li><strong>Monitore o Desempenho e Ajuste as Estratégias:</strong> A comparação contínua entre as vendas reais e as previsões permite que a DrivaTech ajuste suas estratégias conforme necessário, garantindo que a empresa permaneça ágil e adaptável às mudanças nas condições do mercado.</li>
                    <li><strong>Impulsione a Tomada de Decisão Baseada em Dados:</strong> A capacidade de prever vendas futuras fornece à DrivaTech uma base sólida para a tomada de decisões estratégicas, fundamentadas em dados concretos, o que é essencial para garantir um crescimento sustentável e a competitividade no mercado.</li>
                </ul>
                <p>Em resumo, a previsão de vendas não é apenas uma ferramenta analítica, mas uma abordagem estratégica que capacita a DrivaTech a se adaptar proativamente às dinâmicas do mercado, garantindo um crescimento contínuo e bem-sucedido.</p>
            </div>
            """.format(rmse, rmse), unsafe_allow_html=True
        )

# Chame a função run() para executar o script
if __name__ == "__main__":
    run()
