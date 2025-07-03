import pandas as pd
from sqlalchemy import create_engine

def salvar_dados_postgres():
    df = pd.read_excel('vendas_ficticias.xlsx')
    engine = create_engine('postgresql+psycopg2://postgres:postgres123@localhost:5432/Analise_Vendas')
    df.to_sql('vendas',engine, if_exists='replace', index=False)
    print("Dados salvos com sucesso no PostgreSQL!")
salvar_dados_postgres()
