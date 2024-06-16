from controller.postgre_connector import PostgreConnector
from datetime import datetime

class LancamentoController:
    def __init__(self):
        self.db = PostgreConnector()

    def criar_lancamento(self, data_lancamento, tipo_lancamento, conta_id, categoria_id, valor, descricao):
        timestamp_registro = datetime.now()
        query = """
        INSERT INTO Lancamentos (data_lancamento, tipo_lancamento, conta_id, categoria_id, valor, descricao, timestamp_registro)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.db.execute_query(query, (data_lancamento, tipo_lancamento, conta_id, categoria_id, valor, descricao, timestamp_registro))

    def listar_lancamentos(self):
        query = "SELECT * FROM Lancamentos"
        return self.db.fetch_query(query)
    
    def atualizar_lancamento(self, lancamento_id, data_lancamento, tipo_lancamento, conta_id, categoria_id, valor, descricao):
        query = """
        UPDATE Lancamentos SET data_lancamento=%s, tipo_lancamento=%s, conta_id=%s, categoria_id=%s, valor=%s, descricao=%s
        WHERE id=%s
        """
        self.db.execute_query(query, (data_lancamento, tipo_lancamento, conta_id, categoria_id, valor, descricao, lancamento_id))

    def deletar_lancamento(self, lancamento_id):
        query = "DELETE FROM Lancamentos WHERE id=%s"
        self.db.execute_query(query, (lancamento_id,))
