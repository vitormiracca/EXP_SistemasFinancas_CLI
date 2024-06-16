from controller.postgre_connector import PostgreConnector

class CategoriaController:
    def __init__(self):
        self.db = PostgreConnector()

    def criar_categoria(self, tipo_lancamento, nome_categoria):
        query = "INSERT INTO Categorias (tipo_lancamento, nome_categoria) VALUES (%s, %s)"
        self.db.execute_query(query, (tipo_lancamento, nome_categoria))

    def listar_categorias(self, tipo_lancamento=None):
        if tipo_lancamento:
            query = "SELECT * FROM Categorias WHERE tipo_lancamento=%s"
            return self.db.fetch_query(query, (tipo_lancamento,))
        else:
            query = "SELECT * FROM Categorias"
            return self.db.fetch_query(query)

    def atualizar_categoria(self, categoria_id, tipo_lancamento, nome_categoria):
        query = """
        UPDATE Categorias SET tipo_lancamento=%s, nome_categoria=%s
        WHERE id=%s
        """
        self.db.execute_query(query, (tipo_lancamento, nome_categoria, categoria_id))

    def deletar_categoria(self, categoria_id):
        query = "DELETE FROM Categorias WHERE id=%s"
        self.db.execute_query(query, (categoria_id,))
