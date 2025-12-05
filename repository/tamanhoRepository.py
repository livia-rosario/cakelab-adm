from model.tamanhoModel import Tamanho

class TamanhoRepository:
    def __init__(self, db):
        self.db = db

    def listar_tamanhos(self):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT nome_tamanho, valor_base, status_disponibilidade FROM tamanho ORDER BY nome_tamanho")
        linhas = cursor.fetchall()
        cursor.close()
        return [Tamanho(nome, valor, status) for (nome, valor, status) in linhas]

    def buscar_tamanho(self, nome_tamanho):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT nome_tamanho, valor_base, status_disponibilidade FROM tamanho WHERE nome_tamanho = %s", (nome_tamanho,))
        linha = cursor.fetchone()
        cursor.close()
        if linha:
            return Tamanho(linha[0], linha[1], linha[2])
        return None

    def inserir_tamanho(self, tamanho: Tamanho):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tamanho (nome_tamanho, valor_base, status_disponibilidade) VALUES (%s, %s, %s)",
            (tamanho.nome_tamanho, tamanho.valor_base, tamanho.status_disponibilidade)
        )
        conn.commit()
        cursor.close()

    def atualizar_tamanho(self, tamanho: Tamanho):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tamanho SET valor_base = %s, status_disponibilidade = %s WHERE nome_tamanho = %s",
            (tamanho.valor_base, tamanho.status_disponibilidade, tamanho.nome_tamanho)
        )
        conn.commit()
        cursor.close()

    def deletar_tamanho(self, nome_tamanho: str):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tamanho WHERE nome_tamanho = %s", (nome_tamanho,))
        conn.commit()
        cursor.close()
