# 📊 DrivaTech Dashboard

![DrivaTech Logo](assets/images/logo2.jpg)

Bem-vindo ao **DrivaTech Dashboard**, uma aplicação web interativa desenvolvida para analisar o desempenho de vendas, segmentação de clientes e feedbacks. Este dashboard é projetado para otimizar estratégias de marketing e distribuição de produtos, fornecendo insights valiosos para a tomada de decisões estratégicas.

## 🚀 Visão Geral

O DrivaTech Dashboard oferece uma visão abrangente sobre:
- **Previsão de Vendas**: Modelagem preditiva para antecipar vendas futuras até 2029.
- **Desempenho de Vendas por Filial**: Análise detalhada do desempenho de diferentes filiais.
- **Processamento e Análise de Dados de Clientes**: Limpeza e exploração dos dados de clientes.

## 📁 Estrutura do Projeto

```
case_drivaTech/
│
├── main.py
├── pages/
│   └── nav/
│       ├── previsao.py
│       ├── desempenho_filial.py
│       ├── home.py
│       └── ...
├── data/
│   ├── VENDAS.csv
│   ├── FILIAIS.csv
│   └── CLIENTES.csv
├── assets/
│   ├── images/
│   │   └── logo2.jpg
│   ├── pagina_inicial1.json
│   └── animation1.json
├── requirements.txt
└── README.md
```

## 🛠️ Funcionalidades

### 📈 Previsão de Vendas
- **Descrição**: Utilize modelos de regressão para prever vendas futuras, ajudando na tomada de decisões estratégicas.
- **Recursos**:
  - Visualizações interativas com Plotly.
  - Previsões até o ano de 2029.
  - Análise de desempenho do modelo com métricas como RMSE.

### 🏢 Desempenho de Vendas por Filial
- **Descrição**: Analise o desempenho de vendas de diferentes filiais, identificando tendências e áreas de melhoria.
- **Recursos**:
  - Gráficos de barras detalhados.
  - Análise humanizada do desempenho de cada filial.
  - Reflexões e próximos passos baseados nos dados.

### 👥 Processamento e Análise de Dados de Clientes
- **Descrição**: Realize a limpeza, tratamento e análise dos dados de clientes para entender melhor o perfil e comportamento dos clientes.
- **Recursos**:
  - Tratamento de dados ausentes.
  - Análise exploratória de dados.
  - Visualizações da distribuição de clientes por cidade e estado.


## 📦 Instalação

### 1. Clone o Repositório
```bash
git clone https://github.com/thaleson/case_drivaTech.git
cd case_drivaTech
```

### 2. Crie um Ambiente Virtual (Opcional, mas Recomendado)
#### 🪟 **Windows**
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### 🐧 **Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 🍎 **MacOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Executando o Aplicativo

#### 🪟 **Windows**
```bash
streamlit run main.py
```

#### 🐧 **Linux**
```bash
streamlit run main.py
```

#### 🍎 **MacOS**
```bash
streamlit run main.py
```



## 📝 Conclusão

O **DrivaTech Dashboard** é uma ferramenta poderosa que oferece uma visão estratégica sobre o desempenho de vendas, comportamento do consumidor e operações das filiais. Com análises detalhadas e previsões precisas, a DrivaTech pode otimizar suas estratégias de marketing e distribuição, garantindo um crescimento sustentável e adaptável às mudanças do mercado.

### Principais Benefícios:
- **Antecipação de Tendências**: Identifique padrões de vendas e comportamento do consumidor para decisões informadas.
- **Otimização de Estoque**: Planeje a produção e estoque com base em previsões precisas, evitando excessos ou faltas.
- **Estratégias de Marketing Eficientes**: Direcione campanhas de marketing para regiões e períodos de alta demanda.
- **Tomada de Decisão Baseada em Dados**: Utilize insights detalhados para apoiar decisões estratégicas e operacionais.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou fazer pull requests para melhorar este projeto.

1. Fork o repositório
2. Crie sua branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## 📞 Contato

Para dúvidas ou sugestões, entre em contato:
- **Email**: thaleson19@hotmail.com
- **LinkedIn**: [Thaleson](https://www.linkedin.com/in/thaleson-silva/)

---

🔍 **Explore, Analise e Otimize com o DrivaTech Dashboard!**

