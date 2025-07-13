from pydantic import BaseModel
from datetime import date
from sqlalchemy import text

class novaVendas(BaseModel):
    data_da_venda: date
    cliente: str
    produto: str
    quantidade: int
    preco_unitario: float
    valor_total: float
    cidade: str
    vendedor: str
def  criar_venda(engine, venda: novaVendas):
    query = text("""
        INSERT INTO vendas ("Data da Venda", "Cliente", "Produto", "Quantidade", "Preço Unitário", "Valor Total", "Cidade", "Vendedor")
        VALUES (:data_da_venda, :cliente, :produto, :quantidade, :preco_unitario, :valor_total, :cidade, :vendedor)
    """)
    with engine.begin() as conn:
        conn.execute(query, venda)
    return {"message": "Venda registrada com sucesso!"}

def listar_vendas(engine):
    query = text('SELECT * FROM vendas')
    with engine.begin() as conn:                
        resultado = conn.execute(query)         
        return [dict(row._mapping) for row in resultado] 
def deletar_venda(engine, id: int):
    query = text('DELETE FROM vendas WHERE id = :id')
    with engine.begin() as conn:
        conn.execute(query, {"id": id})
    return {"message": "Venda deletada com sucesso!"}

def atualizar_venda(engine, id: int, venda: novaVendas):
    query = text("""
        UPDATE vendas
        SET "Data da Venda" = :data_da_venda,
            "Cliente" = :cliente,
            "Produto" = :produto,
            "Quantidade" = :quantidade,
            "Preço Unitário" = :preco_unitario,
            "Valor Total" = :valor_total,
            "Cidade" = :cidade,
            "Vendedor" = :vendedor
        WHERE id = :id
    """)
    with engine.begin() as conn:
        conn.execute(query, {**venda.dict(), "id": id})
    return {"message": "Venda atualizada com sucesso!"}
    
