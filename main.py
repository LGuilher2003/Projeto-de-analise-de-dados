from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from datetime import date
from sqlalchemy import create_engine,text
from Gráficos import grafico_Produto_valor, grafico_Cidade_valor, grafico_quantidade_cidade  
from crudVendas import criar_venda, listar_vendas, novaVendas, deletar_venda, atualizar_venda

app = FastAPI()
DATABASE_URL = 'postgresql+psycopg2://postgres:postgres123@localhost:5432/Analise_Vendas'
engine = create_engine(DATABASE_URL) #cria uma conexão do python com o banco de dados PostgreSQL


@app.get("/")
def raiz():
    return RedirectResponse(url ="/docs")

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

@app.get("/grafico/Cidade/Quantidade", response_class=HTMLResponse)
def grafico_cidade_quantidade():
    img = grafico_quantidade_cidade()
    return f"<img src= 'data:/image/png;base64,{img}'/>"

#python -m uvicorn main:app --reload
@app.post("/Nova_Venda/")
def nova_venda(venda: novaVendas):
    return  criar_venda(engine, venda.dict())

@app.get("/vendas/")
def listas_vendas():
    return listar_vendas(engine)

@app.delete("/deletar_venda/{id}")
def deletar_venda_db(id: int):
    try:
        return deletar_venda(engine, id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.put("/atualizar_venda/{id}")
def atualizar_venda_db(id: int, venda: novaVendas):
    try:
        return atualizar_venda(engine, id, venda)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
