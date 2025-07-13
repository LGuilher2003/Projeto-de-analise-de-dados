from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()  
def salvar_dados_postgres():
    df = pd.read_excel('dados/vendas_ficticias.xlsx')
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL)
    df.to_sql('vendas', engine, if_exists='replace', index=False)
    print("Dados salvos com sucesso no PostgreSQL!")

salvar_dados_postgres()
