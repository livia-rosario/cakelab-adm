from model.produtoModel import Produto
from model.ingredientesModel import Massa, Recheio, Topping, Cobertura

class ProdutoPersonalizavel(Produto):
    def __init__(self, id_produto: int, nome: str, descricao: str, valor_base: float,
        status_disponibilidade: str, valor_final: float, tamanho: str,
        massa: Massa, recheio_um: Recheio, recheio_dois: Recheio, topping: Topping, cobertura: Cobertura):
        
        super().__init__(id_produto, nome, descricao, valor_base, status_disponibilidade)

        self.valor_final = valor_final
        self.tamanho = tamanho
        self.massa = massa
        self.recheio_um = recheio_um
        self.recheio_dois = recheio_dois
        self.topping = topping
        self.cobertura = cobertura
        

    def __str__(self):
        return f"{self.id_produto} - {self.nome} (R${self.valor_final}) - Tamanho: {self.tamanho}"