from controller.postgre_connector import PostgreConnector

class ContaController:
    def __init__(self):
        self.db = PostgreConnector()

    def criar_conta(self, nome_conta, tipo_conta, dia_fechamento=None, dia_vencimento=None):
        query = """
        INSERT INTO Contas (nome_conta, tipo_conta, dia_fechamento, dia_vencimento)
        VALUES (%s, %s, %s, %s)
        """
        self.db.execute_query(query, (nome_conta, tipo_conta, dia_fechamento, dia_vencimento))

    def listar_contas(self):
        query = "SELECT * FROM Contas"
        return self.db.fetch_query(query)
    
    def atualizar_conta(self, conta_id, nome_conta, tipo_conta, dia_fechamento=None, dia_vencimento=None):
        query = """
        UPDATE Contas SET nome_conta=%s, tipo_conta=%s, dia_fechamento=%s, dia_vencimento=%s
        WHERE id=%s
        """
        self.db.execute_query(query, (nome_conta, tipo_conta, dia_fechamento, dia_vencimento, conta_id))

    def deletar_conta(self, conta_id):
        query = "DELETE FROM Contas WHERE id=%s"
        self.db.execute_query(query, (conta_id,))
