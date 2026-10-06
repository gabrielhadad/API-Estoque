from flask import jsonify, request
from models.produto import Produto


class ProdutoController:

    @staticmethod
    def mostrar_tudo():
        produtos = Produto.mostrar_tudo()
        return jsonify(produtos), 200

    @staticmethod
    def buscar_por_id(id):
        produto = Produto.buscar_por_id(id)

        if produto:
            return jsonify(produto), 200

        return jsonify({"mensagem": "Produto não encontrado"}), 404

    @staticmethod
    def buscar_por_tipo(tipo):
        produtos = Produto.buscar_por_tipo(tipo)
        return jsonify(produtos), 200

    @staticmethod
    def buscar_por_marca(marca):
        produtos = Produto.buscar_por_marca(marca)
        return jsonify(produtos), 200

    @staticmethod
    def buscar_por_nome(nome):
        produtos = Produto.buscar_por_nome(nome)
        return jsonify(produtos), 200

    @staticmethod
    def validar_dados(dados):
        campos = ["nome", "descricao", "tipo", "marca", "quantidade", "valor"]

        if not dados:
            return "Envie os dados do produto em JSON"

        faltando = [campo for campo in campos if campo not in dados]
        if faltando:
            return f"Campos obrigatórios: {', '.join(faltando)}"

        if not str(dados["nome"]).strip() or not str(dados["tipo"]).strip():
            return "Nome e tipo não podem ficar vazios"

        try:
            quantidade = int(dados["quantidade"])
            valor = float(dados["valor"])
        except (TypeError, ValueError):
            return "Quantidade e valor devem ser numéricos"

        if quantidade < 0 or valor < 0:
            return "Quantidade e valor não podem ser negativos"

        return None

    @staticmethod
    def cadastrar():
        dados = request.get_json(silent=True)
        erro = ProdutoController.validar_dados(dados)

        if erro:
            return jsonify({"mensagem": erro}), 400

        id_produto = Produto.cadastrar(
            dados["nome"].strip(),
            dados["descricao"].strip(),
            dados["tipo"].strip(),
            dados["marca"].strip(),
            int(dados["quantidade"]),
            float(dados["valor"]),
        )

        return jsonify({
            "mensagem": "Produto cadastrado com sucesso",
            "id": id_produto,
        }), 201

    @staticmethod
    def atualizar(id):
        produto = Produto.buscar_por_id(id)

        if not produto:
            return jsonify({"mensagem": "Produto não encontrado"}), 404

        dados = request.get_json(silent=True)
        erro = ProdutoController.validar_dados(dados)

        if erro:
            return jsonify({"mensagem": erro}), 400

        Produto.atualizar(
            id,
            dados["nome"].strip(),
            dados["descricao"].strip(),
            dados["tipo"].strip(),
            dados["marca"].strip(),
            int(dados["quantidade"]),
            float(dados["valor"]),
        )

        return jsonify({"mensagem": "Produto atualizado com sucesso"}), 200

    @staticmethod
    def excluir(id):
        produto = Produto.buscar_por_id(id)

        if not produto:
            return jsonify({"mensagem": "Produto não encontrado"}), 404

        Produto.excluir(id)
        return jsonify({"mensagem": "Produto excluído com sucesso"}), 200
