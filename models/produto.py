from config.conexao import get_connection


class Produto:


    @staticmethod
    def mostrar_tudo():
        conexao = get_connection()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

        cursor.close()
        conexao.close()

        return produtos


    @staticmethod
    def buscar_por_id(id):
        conexao = get_connection()
        cursor = conexao.cursor(dictionary=True)

        sql = "SELECT * FROM produtos WHERE id = %s"
        cursor.execute(sql, (id,))

        produto = cursor.fetchone()

        cursor.close()
        conexao.close()

        return produto


    @staticmethod
    def buscar_por_tipo(tipo):
        conexao = get_connection()
        cursor = conexao.cursor(dictionary=True)

        sql = "SELECT * FROM produtos WHERE tipo LIKE %s"
        cursor.execute(sql, (f"%{tipo}%",))

        produtos = cursor.fetchall()

        cursor.close()
        conexao.close()

        return produtos


    @staticmethod
    def buscar_por_marca(marca):
        conexao = get_connection()
        cursor = conexao.cursor(dictionary=True)

        sql = "SELECT * FROM produtos WHERE marca LIKE %s"
        cursor.execute(sql, (f"%{marca}%",))

        produtos = cursor.fetchall()

        cursor.close()
        conexao.close()

        return produtos


    @staticmethod
    def buscar_por_nome(nome):
        conexao = get_connection()
        cursor = conexao.cursor(dictionary=True)

        sql = "SELECT * FROM produtos WHERE nome LIKE %s"
        cursor.execute(sql, (f"%{nome}%",))

        produtos = cursor.fetchall()

        cursor.close()
        conexao.close()

        return produtos


    @staticmethod
    def cadastrar(nome, descricao, tipo, marca, quantidade, valor):
        conexao = get_connection()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO produtos
            (nome, descricao, tipo, marca, quantidade, valor)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (
            nome,
            descricao,
            tipo,
            marca,
            quantidade,
            valor
        )

        cursor.execute(sql, valores)
        conexao.commit()

        id_produto = cursor.lastrowid

        cursor.close()
        conexao.close()

        return id_produto


    @staticmethod
    def atualizar(id, nome, descricao, tipo, marca, quantidade, valor):
        conexao = get_connection()
        cursor = conexao.cursor()

        sql = """
            UPDATE produtos
            SET nome = %s,
                descricao = %s,
                tipo = %s,
                marca = %s,
                quantidade = %s,
                valor = %s
            WHERE id = %s
        """

        valores = (
            nome,
            descricao,
            tipo,
            marca,
            quantidade,
            valor,
            id
        )

        cursor.execute(sql, valores)
        conexao.commit()

        linhas_afetadas = cursor.rowcount

        cursor.close()
        conexao.close()

        return linhas_afetadas


    @staticmethod
    def excluir(id):
        conexao = get_connection()
        cursor = conexao.cursor()

        sql = "DELETE FROM produtos WHERE id = %s"
        cursor.execute(sql, (id,))

        conexao.commit()

        linhas_afetadas = cursor.rowcount

        cursor.close()
        conexao.close()

        return linhas_afetadas