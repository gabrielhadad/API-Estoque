from flask import Flask, render_template
from flasgger import Swagger, swag_from
from controllers.produto_controller import ProdutoController
from config.swagger import (
    swagger_config,
    swagger_template,
    mostrar_produtos_swagger,
    buscar_produto_id_swagger,
    buscar_tipo_swagger,
    buscar_marca_swagger,
    buscar_nome_swagger,
    cadastrar_produto_swagger,
    atualizar_produto_swagger,
    excluir_produto_swagger,
)

app = Flask(__name__)
Swagger(app, config=swagger_config, template=swagger_template)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/produtos", methods=["GET"])
@swag_from(mostrar_produtos_swagger)
def mostrar_produtos():
    return ProdutoController.mostrar_tudo()


@app.route("/produtos/<int:id>", methods=["GET"])
@swag_from(buscar_produto_id_swagger)
def buscar_produto_por_id(id):
    return ProdutoController.buscar_por_id(id)


@app.route("/produtos/tipo/<string:tipo>", methods=["GET"])
@swag_from(buscar_tipo_swagger)
def buscar_produtos_por_tipo(tipo):
    return ProdutoController.buscar_por_tipo(tipo)


@app.route("/produtos/marca/<string:marca>", methods=["GET"])
@swag_from(buscar_marca_swagger)
def buscar_produtos_por_marca(marca):
    return ProdutoController.buscar_por_marca(marca)


@app.route("/produtos/nome/<string:nome>", methods=["GET"])
@swag_from(buscar_nome_swagger)
def buscar_produtos_por_nome(nome):
    return ProdutoController.buscar_por_nome(nome)


@app.route("/produtos", methods=["POST"])
@swag_from(cadastrar_produto_swagger)
def cadastrar_produto():
    return ProdutoController.cadastrar()


@app.route("/produtos/<int:id>", methods=["PUT"])
@swag_from(atualizar_produto_swagger)
def atualizar_produto(id):
    return ProdutoController.atualizar(id)


@app.route("/produtos/<int:id>", methods=["DELETE"])
@swag_from(excluir_produto_swagger)
def excluir_produto(id):
    return ProdutoController.excluir(id)


if __name__ == "__main__":
    app.run(debug=True)
