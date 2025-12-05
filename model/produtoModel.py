from database.conexao import Database

class Produto(): 
    def __init__(self, id_produto: int, nome: str, descricao: str, valor_base: float, status_disponibilidade: bool):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.valor_base = valor_base
        self.status_disponibilidade = status_disponibilidade

    def __str__(self):
        return f"{self.id_produto} - {self.nome} (R${self.valor_base})"