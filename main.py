from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from lerDados import grafico_Produto_valor, grafico_Cidade_valor    

app = FastAPI()


@app.get("/")
def raiz():
    return{"message": "Api de Gráficos de Vendas"}

@app.get("/grafico/Produto/Valor",response_class=HTMLResponse)
def grafico_produto_valor():
    """
    Endpoint para obter o gráfico de valor total por produto.
    Retorna a imagem do gráfico codificada em base64.
    """
    img = grafico_Produto_valor()
    return f"<img src='data:image/png;base64,{img}'/>"
   
@app.get("/grafico/Cidade/Valor", response_class=HTMLResponse)
def grafico_cidade_valor():
    img  = grafico_Cidade_valor()
    return f"<img src='data:image/png;base64,{img}'/>"
#python -m uvicorn main:app --reload