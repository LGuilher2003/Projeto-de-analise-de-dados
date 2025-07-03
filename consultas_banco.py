import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:postgres123@localhost:5432/Analise_Vendas')
query = 'SELECT * FROM vendas WHERE "id" = \'103\''
df_filtrado = pd.read_sql_query(query, engine)
print(df_filtrado)