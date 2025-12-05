class Massa():
    def __init__(self, nome: str, status_disponibilidade: bool, id_massa: str = None):
        self.id_massa = id_massa
        self.nome = nome
        self.status_disponibilidade = status_disponibilidade

class Recheio():
    def __init__(self, nome: str, status_disponibilidade: bool, valor_adc: float, id_recheio: str = None):
        self.id_recheio = id_recheio
        self.nome = nome
        self.status_disponibilidade = status_disponibilidade
        self.valor_adc = valor_adc

class Topping():
    def __init__(self, nome: str, status_disponibilidade: bool, valor_adc: float, id_topping: str = None):
        self.id_topping = id_topping
        self.nome = nome
        self.status_disponibilidade = status_disponibilidade
        self.valor_adc = valor_adc

class Cobertura():
    def __init__(self, nome: str, status_disponibilidade: bool, id_cobertura: str = None):
        self.id_cobertura = id_cobertura
        self.nome = nome
        self.status_disponibilidade = status_disponibilidade
        
