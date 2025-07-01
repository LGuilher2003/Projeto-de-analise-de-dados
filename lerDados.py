import pandas as pd
import matplotlib.pyplot as plt
import io  #usado para manipular dados em memória
import base64 #converte dados binários em texto

# Função para carregar a planilha
def carregar_dados():
    df = pd.read_excel('vendas_ficticias.xlsx')
    return df

# Gera gráfico de valor total por produto e retorna como base64 (imagem)
def grafico_Produto_valor():
    df = carregar_dados()
    agrupar = df.groupby('Produto')['Valor Total'].sum()
    fig, ax = plt.subplots()
    agrupar.plot(kind='bar', title='Valor Total por Produto', ax=ax)
    plt.xlabel('Produto')
    plt.ylabel('Valor Total')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

# Gera gráfico de valor total por cidade
def grafico_Cidade_valor():
    df = carregar_dados()
    agrupar = df.groupby('Cidade')['Valor Total'].sum()
    fig, ax = plt.subplots()
    agrupar.plot(kind='bar', title='Valor Total por Cidade', ax=ax)
    plt.xlabel('Cidade')
    plt.ylabel('Valor Total')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')
