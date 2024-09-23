# CRUD FastAPI Project

Este é um projeto CRUD (Create, Read, Update, Delete) desenvolvido com FastAPI, utilizando PostgreSQL como banco de dados e SQLAlchemy para a modelagem de dados.

## Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)**: Versão 0.114.2
- **[Uvicorn](https://www.uvicorn.org/)**: Versão 0.30.6 (servidor ASGI)
- **[Requests](https://docs.python-requests.org/)**: Versão 2.32.3 (para requisições HTTP)
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: Versão 2.0.34 (ORM para a base de dados)
- **[psycopg2](https://www.psycopg.org/)**: Versão 2.9.9 (driver PostgreSQL)
- **[Alembic](https://alembic.sqlalchemy.org/)**: Versão 1.13.2 (ferramenta de migração de banco de dados)
- **[Black](https://black.readthedocs.io/en/stable/)**: Versão 24.8.0 (formatação de código)
- **[Pytest](https://docs.pytest.org/en/7.4.x/)**: Versões 7.4.2 e 8.3.3 (ferramenta de testes)
- **[Pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)**: Versão 4.1.0 (geração de relatório de cobertura de testes)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Pedro-Adriano/crud_fastapi.git
   cd crud_fastapi

2. Crie um ambiente virtual e ative:
    python3 -m venv venv
    source venv/bin/activate  # Em sistemas Unix
    # ou
    venv\Scripts\activate  # Em Windows

3. Instale as dependências:
   pip install -r requirements.txt

4. Defina as variáveis de ambiente com as informações do banco:
   export DATABASE_URL=postgresql://usuario:senha@localhost/nome_do_banco

5. Execute as migrações do banco:
   alembic upgrade head

6. Inicie o servidor utilizando o Uvicorn:
   uvicorn app.main:app --reload

Estrutura do Projeto
crud_fastapi/
│
├── alembic/              # Migrações do banco
├── app/
│   ├── api/              # Rotas da API
│   ├── models/           # Modelos do SQLAlchemy
│   ├── crud.py           # Funções CRUD
│   └── main.py           # Ponto de entrada da aplicação
│
├── tests/                # Testes do projeto
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto

   
