swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API Estoque de TI",
        "description": "API REST acadêmica para controle de produtos de um estoque de TI.",
        "version": "1.0.0",
    },
    "basePath": "/",
    "schemes": ["http"],
    "definitions": {
        "Produto": {
            "type": "object",
            "properties": {
                "id": {"type": "integer", "example": 1},
                "nome": {"type": "string", "example": "SSD 480GB SATA"},
                "descricao": {"type": "string", "example": "SSD SATA de 2.5 polegadas com 480GB"},
                "tipo": {"type": "string", "example": "Armazenamento"},
                "marca": {"type": "string", "example": "Kingston"},
                "quantidade": {"type": "integer", "example": 8},
                "valor": {"type": "number", "format": "float", "example": 219.90},
            },
        },
        "ProdutoEntrada": {
            "type": "object",
            "required": ["nome", "descricao", "tipo", "marca", "quantidade", "valor"],
            "properties": {
                "nome": {"type": "string", "example": "SSD 480GB SATA"},
                "descricao": {"type": "string", "example": "SSD SATA de 2.5 polegadas com 480GB"},
                "tipo": {"type": "string", "example": "Armazenamento"},
                "marca": {"type": "string", "example": "Kingston"},
                "quantidade": {"type": "integer", "example": 8},
                "valor": {"type": "number", "format": "float", "example": 219.90},
            },
        },
    },
}


def resposta_produtos(tag="Produtos"):
    return {
        "tags": [tag],
        "responses": {
            200: {
                "description": "Lista de produtos",
                "schema": {"type": "array", "items": {"$ref": "#/definitions/Produto"}},
            }
        },
    }


mostrar_produtos_swagger = {
    "tags": ["Produtos"],
    "summary": "Listar todos os produtos",
    "responses": {
        200: {
            "description": "Produtos cadastrados",
            "schema": {"type": "array", "items": {"$ref": "#/definitions/Produto"}},
        }
    },
}

buscar_produto_id_swagger = {
    "tags": ["Produtos"],
    "summary": "Buscar produto por ID",
    "parameters": [
        {"name": "id", "in": "path", "required": True, "type": "integer"}
    ],
    "responses": {
        200: {"description": "Produto encontrado", "schema": {"$ref": "#/definitions/Produto"}},
        404: {"description": "Produto não encontrado"},
    },
}

buscar_tipo_swagger = {
    "tags": ["Consultas"],
    "summary": "Buscar produtos por tipo",
    "description": "Pesquisa parcial utilizando LIKE.",
    "parameters": [
        {"name": "tipo", "in": "path", "required": True, "type": "string"}
    ],
    "responses": {
        200: {
            "description": "Produtos encontrados",
            "schema": {"type": "array", "items": {"$ref": "#/definitions/Produto"}},
        }
    },
}

buscar_marca_swagger = {
    "tags": ["Consultas"],
    "summary": "Buscar produtos por marca",
    "description": "Pesquisa parcial utilizando LIKE.",
    "parameters": [
        {"name": "marca", "in": "path", "required": True, "type": "string"}
    ],
    "responses": {
        200: {
            "description": "Produtos encontrados",
            "schema": {"type": "array", "items": {"$ref": "#/definitions/Produto"}},
        }
    },
}

buscar_nome_swagger = {
    "tags": ["Consultas"],
    "summary": "Buscar produtos por nome",
    "description": "Pesquisa parcial utilizando LIKE.",
    "parameters": [
        {"name": "nome", "in": "path", "required": True, "type": "string"}
    ],
    "responses": {
        200: {
            "description": "Produtos encontrados",
            "schema": {"type": "array", "items": {"$ref": "#/definitions/Produto"}},
        }
    },
}

cadastrar_produto_swagger = {
    "tags": ["Produtos"],
    "summary": "Cadastrar produto",
    "parameters": [
        {
            "name": "produto",
            "in": "body",
            "required": True,
            "schema": {"$ref": "#/definitions/ProdutoEntrada"},
        }
    ],
    "responses": {
        201: {"description": "Produto cadastrado com sucesso"},
        400: {"description": "Dados inválidos"},
    },
}

atualizar_produto_swagger = {
    "tags": ["Produtos"],
    "summary": "Atualizar produto",
    "parameters": [
        {"name": "id", "in": "path", "required": True, "type": "integer"},
        {
            "name": "produto",
            "in": "body",
            "required": True,
            "schema": {"$ref": "#/definitions/ProdutoEntrada"},
        },
    ],
    "responses": {
        200: {"description": "Produto atualizado com sucesso"},
        400: {"description": "Dados inválidos"},
        404: {"description": "Produto não encontrado"},
    },
}

excluir_produto_swagger = {
    "tags": ["Produtos"],
    "summary": "Excluir produto",
    "parameters": [
        {"name": "id", "in": "path", "required": True, "type": "integer"}
    ],
    "responses": {
        200: {"description": "Produto excluído com sucesso"},
        404: {"description": "Produto não encontrado"},
    },
}
