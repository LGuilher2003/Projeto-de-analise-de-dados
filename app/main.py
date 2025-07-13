from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy import create_engine 
from app.crud.crudVendas import criar_venda, listar_vendas, novaVendas, deletar_venda, atualizar_venda

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
DATABASE_URL = 'postgresql+psycopg2://postgres:postgres123@localhost:5432/Analise_Vendas'
engine = create_engine(DATABASE_URL) 

@app.get("/")
def raiz():
    return RedirectResponse(url ="/docs")  
    
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
