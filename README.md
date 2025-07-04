# API de Gráficos de Vendas

Este projeto é uma API desenvolvida com FastAPI para análise e visualização de dados de vendas. O objetivo é facilitar estudos e experimentos em Data Science, integrando gráficos dinâmicos, banco de dados PostgreSQL e análises customizadas.

## Funcionalidades
- Visualização de gráficos de vendas por produto e por cidade
- Leitura de dados a partir de planilhas Excel
- Futuro: Integração com banco de dados PostgreSQL
- Futuro: Novas análises e endpoints para estudos em Data Science

## Tecnologias Utilizadas
- Python 3.10+
- FastAPI
- Pandas
- Matplotlib
- PostgreSQL (planejado)

## Como executar
1. Instale as dependências:
   ```bash
   pip install fastapi uvicorn pandas matplotlib openpyxl
   ```
2. Execute o servidor:
   ```bash
   python -m uvicorn main:app --reload
   ```
3. Acesse os endpoints no navegador:
   - `http://127.0.0.1:8000/grafico/Produto/Valor`
   - `http://127.0.0.1:8000/grafico/Cidade/Valor`

## Estrutura do Projeto
- `main.py`: Arquivo principal da API FastAPI
- `lerDados.py`: Funções para leitura e análise dos dados
- `vendas_ficticias.xlsx`: Base de dados fictícia para testes

## Futuras Expansões
- Conexão e manipulação de dados com PostgreSQL
- Novos endpoints para análises estatísticas e machine learning
- Documentação detalhada dos endpoints

## Objetivo
Este projeto serve como base para estudos em Data Science, APIs e integração com bancos de dados relacionais, sendo ideal para aprendizado e experimentação.
