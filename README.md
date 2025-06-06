#  Dashboard de Vendas do Xbox

Este projeto tem como objetivo a criação de um **Dashboard de Vendas do Xbox**, com dados fictícios, para fins de estudo e prática de visualização e análise de dados no Excel.

##  Arquivos Incluídos

- `Dashboard_Vendas_Xbox.xlsx`  
  Planilha com:
  - Aba **Base de Dados**: 100 registros de vendas fictícias por data, região, modelo, canal e valores.
  - Aba **Indicadores**: KPIs importantes como Receita Total, Modelo mais vendido e Região com maior receita.

- `gerar_dashboard.py`  
  Script em Python responsável por:
  - Gerar dados de vendas fictícios.
  - Calcular receita total por linha.
  - Exportar o conteúdo para um arquivo Excel com múltiplas abas usando `pandas` e `xlsxwriter`.

##  Como Executar o Script Python

### Pré-requisitos
```bash
pip install pandas numpy xlsxwriter
```

### Execução
```bash
python gerar_dashboard.py
```

##  O Que Você Pode Fazer com Este Projeto

- Inserir Tabelas Dinâmicas e Gráficos Dinâmicos no Excel.
- Aplicar segmentações (slicers) por:
  - Região
  - Modelo Xbox
  - Canal de Venda
- Criar seu próprio painel de KPIs com indicadores interativos.
- Personalizar com Power Query e Power Pivot.

##  Observação

Os dados utilizados neste projeto são totalmente fictícios e criados aleatoriamente para fins de prática educacional.
