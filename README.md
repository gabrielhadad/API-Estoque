# API Estoque de TI

Projeto acadêmico de API REST em Python/Flask para controle de estoque de TI.

## Banco de dados

- MySQL (XAMPP)
- Banco: `estoque_ti`
- Tabela: `produtos`
- Script: `config/banco.sql`

## Estrutura

- `app.py`: rotas Flask, Swagger e rota do front
- `models/produto.py`: consultas e comandos SQL
- `controllers/produto_controller.py`: regras de entrada/saída da API
- `config/conexao.py`: conexão com MySQL
- `config/swagger.py`: documentação dos endpoints
- `templates/index.html`: front simples que consome a API

## Endpoints

- `GET /produtos` — listar todos
- `GET /produtos/<id>` — buscar por ID
- `GET /produtos/tipo/<tipo>` — buscar por tipo com LIKE
- `GET /produtos/marca/<marca>` — buscar por marca com LIKE
- `GET /produtos/nome/<nome>` — buscar por nome com LIKE
- `POST /produtos` — cadastrar
- `PUT /produtos/<id>` — atualizar
- `DELETE /produtos/<id>` — excluir

## Executar

1. Inicie Apache/MySQL no XAMPP e execute `config/banco.sql` no MySQL.
2. Confira usuário, senha e porta em `config/conexao.py`.
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute:

```bash
python app.py
```

5. Acesse:

- Front: `http://127.0.0.1:5000/`
- Swagger: `http://127.0.0.1:5000/apidocs/`
