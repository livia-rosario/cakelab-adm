from model.produtoNaoPersonalizavelModel import Bebidas, BoloPronto, ItensFesta

class BebidasRepository:
    def __init__(self, db):
        self.db = db

    def listar_bebidas(self) -> list[Bebidas]:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        query = """
        SELECT 
            p.id_produto,
            p.nome,
            p.descricao,
            p.valor_base,
            p.status_disponibilidade
        FROM produto p
        JOIN produto_naopersonalizavel np 
            ON np.fk_produto_id_produto = p.id_produto
        JOIN bebidas b
            ON b.fk_produto_naopersonalizavel = p.id_produto;
        """
        
        cursor.execute(query)
        linhas = cursor.fetchall()
        cursor.close()

        return [Bebidas(*linha) for linha in linhas]
    
    def buscar_por_id(self, id_produto: str) -> Bebidas | None:
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
        SELECT 
            p.id_produto,
            p.nome,
            p.descricao,
            p.valor_base,
            p.status_disponibilidade
        FROM produto p
        JOIN produto_naopersonalizavel np 
            ON np.fk_produto_id_produto = p.id_produto
        JOIN bebidas b
            ON b.fk_produto_naopersonalizavel = p.id_produto
        WHERE p.id_produto = %s;
        """

        cursor.execute(query, (id_produto,))
        linha = cursor.fetchone()
        cursor.close()

        return Bebidas(*linha) if linha else None
    
    def inserir_bebida(self, bebida: Bebidas) -> str:
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO produto (nome, descricao, valor_base, status_disponibilidade)
            VALUES (%s, %s, %s, %s)
            RETURNING id_produto;
        """, (
            bebida.nome,
            bebida.descricao,
            bebida.valor_base,
            bebida.status_disponibilidade,
        ))
        id_produto = cursor.fetchone()[0]

        cursor.execute("""
            INSERT INTO produto_naopersonalizavel (fk_produto_id_produto)
            VALUES (%s);
        """, (id_produto,))

        cursor.execute("""
            INSERT INTO bebidas (fk_produto_naopersonalizavel)
            VALUES (%s);
        """, (id_produto,))

        conn.commit()
        cursor.close()
        return id_produto

    def deletar_bebida(self, id_produto: str) -> None:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM produto WHERE id_produto = %s", (id_produto,))
        conn.commit()
        cursor.close()
        
        return None
    
    def atualizar_bebida(self, bebida: Bebidas) -> None:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE produto
            SET nome = %s,
                descricao = %s,
                valor_base = %s,
                status_disponibilidade = %s
            WHERE id_produto = %s
            """, (
                bebida.nome,
                bebida.descricao,
                bebida.valor_base,
                bebida.status_disponibilidade,
                bebida.id_produto
            ))
        conn.commit()
        cursor.close()
        
        return None
    
class ItensFestaRepository:
    def __init__(self, db):
        self.db = db
        
    def listar_itens_festa(self) -> list[ItensFesta]:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        query = """
        SELECT
            p.id_produto,
            p.nome,
            p.descricao,
            p.valor_base,
            p.status_disponibilidade
        FROM produto p
        JOIN produto_naopersonalizavel np
            ON np.fk_produto_id_produto = p.id_produto
        JOIN itens_festa i
            ON i.fk_produto_naopersonalizavel = p.id_produto;
        """
        
        cursor.execute(query)
        linhas = cursor.fetchall()
        cursor.close()

        return [ItensFesta(*linha) for linha in linhas]
    
    def buscar_por_id(self, id_produto: str) -> ItensFesta | None:
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
        SELECT
            p.id_produto,
            p.nome,
            p.descricao,
            p.valor_base,
            p.status_disponibilidade
        FROM produto p
        JOIN produto_naopersonalizavel np
            ON np.fk_produto_id_produto = p.id_produto
        JOIN itens_festa i
            ON i.fk_produto_naopersonalizavel = p.id_produto
        WHERE p.id_produto = %s;
        """

        cursor.execute(query, (id_produto,))
        linha = cursor.fetchone()
        cursor.close()

        return ItensFesta(*linha) if linha else None
    
    def inserir_itens_festa(self, itens_festa: ItensFesta) -> str:
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO produto (nome, descricao, valor_base, status_disponibilidade)
            VALUES (%s, %s, %s, %s)
            RETURNING id_produto;
            """, (
                itens_festa.nome,
                itens_festa.descricao,
                itens_festa.valor_base,
                itens_festa.status_disponibilidade,
            ))
        id_produto = cursor.fetchone()[0]

        cursor.execute("""
            INSERT INTO produto_naopersonalizavel (fk_produto_id_produto)
            VALUES (%s);
            """, (id_produto,))

        cursor.execute("""
            INSERT INTO itens_festa (fk_produto_naopersonalizavel)
            VALUES (%s);
            """, (id_produto,))

        conn.commit()
        cursor.close()
        return id_produto   
    
    def deletar_itens_festa(self, id_produto: str) -> None:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM produto WHERE id_produto = %s", (id_produto,))
        conn.commit()
        cursor.close()
        
        return None
    
    def atualizar_itens_festa(self, itens_festa: ItensFesta) -> None:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE produto
            SET nome = %s,
                descricao = %s,
                valor_base = %s,
                status_disponibilidade = %s
            WHERE id_produto = %s
            """, (
                itens_festa.nome,
                itens_festa.descricao,
                itens_festa.valor_base,
                itens_festa.status_disponibilidade,
                itens_festa.id_produto
            ))
        conn.commit()
        cursor.close()
        
        return None 
    
class BoloProntoRepository:
    def __init__(self, db):
        self.db = db
        
    def listar_bolos_pronto(self) -> list[BoloPronto]:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        query = """
        SELECT
            p.id_produto,
            p.nome,
            p.descricao,
            p.valor_base,
            p.status_disponibilidade
        FROM produto p
        JOIN produto_naopersonalizavel np
            ON np.fk_produto_id_produto = p.id_produto
        JOIN bolo_pronto b
            ON b.fk_produto_naopersonalizavel = p.id_produto;
        """
        
        cursor.execute(query)
        linhas = cursor.fetchall()
        cursor.close()

        return [BoloPronto(*linha) for linha in linhas]
    
    def buscar_por_id(self, id_produto: str) -> BoloPronto | None:
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
        SELECT
            p.id_produto,
            p.nome,
            p.descricao,
            p.valor_base,
            p.status_disponibilidade
        FROM produto p
        JOIN produto_naopersonalizavel np
            ON np.fk_produto_id_produto = p.id_produto
        JOIN bolo_pronto b
            ON b.fk_produto_naopersonalizavel = p.id_produto
        WHERE p.id_produto = %s;
        """

        cursor.execute(query, (id_produto,))
        linha = cursor.fetchone()
        cursor.close()

        return BoloPronto(*linha) if linha else None
    
    def inserir_bolo_pronto(self, bolo_pronto: BoloPronto) -> str:
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO produto (nome, descricao, valor_base, status_disponibilidade)
            VALUES (%s, %s, %s, %s)
            RETURNING id_produto;
            """, (
                bolo_pronto.nome,
                bolo_pronto.descricao,
                bolo_pronto.valor_base,
                bolo_pronto.status_disponibilidade,
            ))
        id_produto = cursor.fetchone()[0]

        cursor.execute("""
            INSERT INTO produto_naopersonalizavel (fk_produto_id_produto)
            VALUES (%s);
            """, (id_produto,))

        cursor.execute("""
            INSERT INTO bolo_pronto (fk_produto_naopersonalizavel)
            VALUES (%s);
            """, (id_produto,))

        conn.commit()
        cursor.close()
        return id_produto
    
    def deletar_bolo_pronto(self, id_produto: str) -> None:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM produto WHERE id_produto = %s", (id_produto,))
        conn.commit()
        cursor.close()
        
        return None
    
    def atualizar_bolo_pronto(self, bolo_pronto: BoloPronto) -> None:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE produto
            SET nome = %s,
                descricao = %s,
                valor_base = %s,
                status_disponibilidade = %s
            WHERE id_produto = %s
            """, (
                bolo_pronto.nome,
                bolo_pronto.descricao,
                bolo_pronto.valor_base,
                bolo_pronto.status_disponibilidade,
                bolo_pronto.id_produto
            ))
        conn.commit()
        cursor.close()
        
        return None

class ProdutoNaoPersonalizadoRepository:
    def __init__(self, db):
        self.db = db
        self.bebidas_repo = BebidasRepository(db)
        self.itens_festa_repo = ItensFestaRepository(db)
        self.bolo_pronto_repo = BoloProntoRepository(db)
    
    def listar_nao_personalizaveis(self):
        bebidas = self.bebidas_repo.listar_bebidas()
        itens_festa = self.itens_festa_repo.listar_itens_festa()
        bolos_pronto = self.bolo_pronto_repo.listar_bolos_pronto()
        return bebidas + itens_festa + bolos_pronto
    
    def buscar_nao_personalizavel_por_id(self, id_produto):
        bebidas = self.bebidas_repo.buscar_bebida(id_produto)
        if bebidas:
            return bebidas
        
        itens_festa = self.itens_festa_repo.buscar_item_festa(id_produto)
        if itens_festa:
            return itens_festa
        
        bolos_pronto = self.bolo_pronto_repo.buscar_bolo_pronto(id_produto)
        if bolos_pronto:
            return bolos_pronto
        
        return None
