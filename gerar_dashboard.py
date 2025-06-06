import pandas as pd
import numpy as np

# Gerando dados fictícios para a base de dados
np.random.seed(42)
dates = pd.date_range(start="2025-01-01", periods=100, freq='D')
regions = ['Sudeste', 'Sul', 'Nordeste', 'Centro-Oeste', 'Norte']
models = ['Xbox Series X', 'Xbox Series S']
channels = ['E-commerce', 'Loja Física', 'Marketplace']

data = {
    'Data': np.random.choice(dates, 100),
    'Região': np.random.choice(regions, 100),
    'Modelo Xbox': np.random.choice(models, 100),
    'Unidades Vendidas': np.random.randint(50, 300, size=100),
    'Preço Unitário': np.random.choice([4500, 2900], size=100),
    'Canal de Venda': np.random.choice(channels, 100)
}

df = pd.DataFrame(data)
df['Receita Total'] = df['Unidades Vendidas'] * df['Preço Unitário']

# Salvando em um arquivo Excel com múltiplas abas
output_path = "Dashboard_Vendas_Xbox.xlsx"

with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Base de Dados', index=False)

    indicadores = {
        'Indicador': [
            'Total de Unidades Vendidas',
            'Receita Total',
            'Ticket Médio',
            'Modelo Mais Vendido',
            'Região com Maior Receita'
        ],
        'Valor': [
            df['Unidades Vendidas'].sum(),
            df['Receita Total'].sum(),
            round(df['Receita Total'].sum() / df['Unidades Vendidas'].sum(), 2),
            df.groupby('Modelo Xbox')['Unidades Vendidas'].sum().idxmax(),
            df.groupby('Região')['Receita Total'].sum().idxmax()
        ]
    }
    indicadores_df = pd.DataFrame(indicadores)
    indicadores_df.to_excel(writer, sheet_name='Indicadores', index=False)
