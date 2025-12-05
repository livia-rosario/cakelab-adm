from model.ingredientesModel import Massa, Recheio, Topping, Cobertura

class IngredientesRepository:
    def __init__(self, db):
        self.db = db

    # Massas:
    def criar_massa(self, massa: Massa) -> str | None:
        query = """INSERT INTO massa (nome, status_disponibilidade)
            VALUES (%s, %s)
            RETURNING id_massa
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            massa.nome,
            massa.status_disponibilidade
        ))

        novo_id = cursor.fetchone()[0]
        conn.commit()

        cursor.close()
        return novo_id
    
    def inserir_massa(self, massa: Massa) -> str | None:
        return self.criar_massa(massa)
    
    def apagar_massa(self, id_massa: str) -> None:
        query = "DELETE FROM massa WHERE id_massa = %s"
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(query, (id_massa,))
        conn.commit()
        cursor.close()

        return None
    
    def deletar_massa(self, id_massa: str) -> None:
        return self.apagar_massa(id_massa)
    
    def atualizar_massa(self, massa: Massa) -> None:
        query = """
            UPDATE massa
            SET nome = %s,
                status_disponibilidade = %s
            WHERE id_massa = %s
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            massa.nome,
            massa.status_disponibilidade,
            massa.id_massa
        ))
        conn.commit()
        cursor.close()
        
        return None
    
    def listar_massas(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id_massa, nome, status_disponibilidade FROM massa")
        linhas = cursor.fetchall()

        cursor.close()
        return [Massa(nome, status, id_massa) for (id_massa, nome, status) in linhas]

    def buscar_massa_por_id(self, id_massa: str):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id_massa, nome, status_disponibilidade FROM massa WHERE id_massa = %s", (id_massa,))
        linha = cursor.fetchone()

        cursor.close()
        if linha:
            return Massa(linha[1], linha[2], linha[0])
        return None

    # Recheios:
    def criar_recheio(self, recheio: Recheio) -> str:
        query = """
            INSERT INTO recheio (nome, status_disponibilidade, valor_adc)
            VALUES (%s, %s, %s)
            RETURNING id_recheio
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            recheio.nome,
            recheio.status_disponibilidade,
            recheio.valor_adc
        ))
        novo_id = cursor.fetchone()[0]
        conn.commit()

        cursor.close()
        return novo_id
    
    def inserir_recheio(self, recheio: Recheio) -> str:
        return self.criar_recheio(recheio)
    
    def apagar_recheio(self, id_recheio: str) -> None:
        query = "DELETE FROM recheio WHERE id_recheio = %s"
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(query, (id_recheio,))
        conn.commit()
        cursor.close()

        return None
    
    def deletar_recheio(self, id_recheio: str) -> None:
        return self.apagar_recheio(id_recheio)
    
    def atualizar_recheio(self, recheio: Recheio) -> None:
        query = """
            UPDATE recheio
            SET nome = %s,
                status_disponibilidade = %s,
                valor_adc = %s
            WHERE id_recheio = %s
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            recheio.nome,
            recheio.status_disponibilidade,
            recheio.valor_adc,
            recheio.id_recheio
        ))
        conn.commit()
        cursor.close()
        
        return None
    
    def listar_recheios(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id_recheio, nome, status_disponibilidade, valor_adc FROM recheio")
        linhas = cursor.fetchall()

        cursor.close()
        return [Recheio(nome, status, valor, id_recheio) for (id_recheio, nome, status, valor) in linhas]

    def buscar_recheio_por_id(self, id_recheio: str):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id_recheio, nome, status_disponibilidade, valor_adc FROM recheio WHERE id_recheio = %s", (id_recheio,))
        linha = cursor.fetchone()

        cursor.close()
        if linha:
            return Recheio(linha[1], linha[2], linha[3], linha[0])
        return None

    # Toppings:
    def criar_topping(self, topping: Topping) -> str:
        query = """
            INSERT INTO topping (nome, status_disponibilidade, valor_adc)
            VALUES (%s, %s, %s)
            RETURNING id_topping
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            topping.nome,
            topping.status_disponibilidade,
            topping.valor_adc
        ))
        novo_id = cursor.fetchone()[0]
        conn.commit()

        cursor.close()
        return novo_id
    
    def inserir_topping(self, topping: Topping) -> str:
        return self.criar_topping(topping)
    
    def apagar_topping(self, id_topping: str) -> None:
        query = "DELETE FROM topping WHERE id_topping = %s"
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(query, (id_topping,))
        conn.commit()
        cursor.close()

        return None
    
    def deletar_topping(self, id_topping: str) -> None:
        return self.apagar_topping(id_topping)
    def atualizar_topping(self, topping: Topping) -> None:
        query = """
            UPDATE topping
            SET nome = %s,
                status_disponibilidade = %s
            WHERE id_topping = %s
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            topping.nome,
            topping.status_disponibilidade,
            topping.id_topping
        ))
        conn.commit()
        cursor.close()
        
        return None
    
    def listar_toppings(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id_topping, nome, status_disponibilidade, valor_adc FROM topping")
        linhas = cursor.fetchall()

        cursor.close()
        return [Topping(nome, status, valor, id_topping) for (id_topping, nome, status, valor) in linhas]

    def buscar_topping_por_id(self, id_topping: str):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id_topping, nome, status_disponibilidade, valor_adc FROM topping WHERE id_topping = %s", (id_topping,))
        linha = cursor.fetchone()

        cursor.close()
        if linha:
            return Topping(linha[1], linha[2], linha[3], linha[0])
        return None

    # Coberturas:
    def criar_cobertura(self, cobertura: Cobertura) -> str:
        query = """
            INSERT INTO cobertura (nome, status_disponibilidade)
            VALUES (%s, %s)
            RETURNING id_cobertura
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            cobertura.nome,
            cobertura.status_disponibilidade
        ))
        novo_id = cursor.fetchone()[0]
        conn.commit()

        cursor.close()
        return novo_id
    
    def inserir_cobertura(self, cobertura: Cobertura) -> str:
        return self.criar_cobertura(cobertura)
    
    def apagar_cobertura(self, id_cobertura: str) -> None:
        query = "DELETE FROM coberturas WHERE id_cobertura = %s"
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(query, (id_cobertura,))
        conn.commit()
        cursor.close()

        return None
    
    def deletar_cobertura(self, id_cobertura: str) -> None:
        return self.apagar_cobertura(id_cobertura)

        return None
    
    def atualizar_cobertura(self, cobertura: Cobertura) -> None:
        query = """
            UPDATE cobertura
            SET nome = %s,
                status_disponibilidade = %s
            WHERE id_cobertura = %s
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            cobertura.nome,
            cobertura.status_disponibilidade,
            cobertura.id_cobertura
        ))
        conn.commit()
        cursor.close()
        
        return None
    
    def listar_coberturas(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id_cobertura, nome, status_disponibilidade FROM cobertura")
        linhas = cursor.fetchall()

        cursor.close()
        return [Cobertura(nome, status, id_cobertura) for (id_cobertura, nome, status) in linhas]

    def buscar_cobertura_por_id(self, id_cobertura: str):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id_cobertura, nome, status_disponibilidade FROM cobertura WHERE id_cobertura = %s", (id_cobertura,))
        linha = cursor.fetchone()

        cursor.close()
        if linha:
            return Cobertura(linha[1], linha[2], linha[0])
        return None
