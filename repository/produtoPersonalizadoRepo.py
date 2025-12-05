from model.produtoPersonalizavelModel import ProdutoPersonalizavel
from model.ingredientesModel import Massa, Recheio, Topping, Cobertura
from database.conexao import Database

class ProdutoPersonalizadoRepository:
    def __init__(self, db: Database):
        self.db = db

    def listar_todos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
        SELECT 
            p.id_produto,
            p.nome,
            p.descricao,
            p.valor_base,
            p.status_disponibilidade,
            pp.valor_final,
            pp.fk_tamanho,
            m.nome AS massa,
            r1.nome AS recheio1,
            r2.nome AS recheio2,
            c.nome AS cobertura,
            t.nome AS topping

        FROM produto p
        JOIN produto_personalizavel pp ON p.id_produto = pp.fk_produto_id_produto
        JOIN massa m ON pp.fk_massa = m.id_massa
        JOIN recheio r1 ON pp.fk_recheio1 = r1.id_recheio
        JOIN recheio r2 ON pp.fk_recheio2 = r2.id_recheio
        JOIN cobertura c ON pp.fk_cobertura = c.id_cobertura
        LEFT JOIN topping t ON pp.fk_topping = t.id_topping
        ORDER BY p.id_produto;
        """

        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        produtos = []
        for row in rows:
            (id_prod, nome, descricao, valor_base, status,
             valor_final, tamanho, massa, recheio1, recheio2,
             cobertura, topping) = row

            produto = ProdutoPersonalizavel(
                id_produto=id_prod,
                nome=nome,
                descricao=descricao,
                valor_base=valor_base,
                status_disponibilidade=status,
                valor_final=valor_final,
                massa=Massa(massa, True),
                recheio1=Recheio(recheio1, True, 0),
                recheio2=Recheio(recheio2, True, 0),
                cobertura=Cobertura(cobertura, True),
                topping=Topping(topping, True),
                tamanho=tamanho
            )

            produtos.append(produto)

        return produtos

    def buscar_por_id(self, id_produto):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
        SELECT 
            p.id_produto,
            p.nome,
            p.descricao,
            p.valor_base,
            p.status_disponibilidade,

            pp.valor_final,
            pp.fk_tamanho,       

            m.nome AS massa,
            r1.nome AS recheio1,
            r2.nome AS recheio2,
            c.nome AS cobertura,
            t.nome AS topping

        FROM produto p
        JOIN produto_personalizavel pp ON p.id_produto = pp.fk_produto_id_produto
        JOIN massa m ON pp.fk_massa = m.id_massa
        JOIN recheio r1 ON pp.fk_recheio1 = r1.id_recheio
        JOIN recheio r2 ON pp.fk_recheio2 = r2.id_recheio
        JOIN cobertura c ON pp.fk_cobertura = c.id_cobertura
        LEFT JOIN topping t ON pp.fk_topping = t.id_topping
        WHERE p.id_produto = %s;
        """

        cursor.execute(query, (id_produto,))
        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        (id_prod, nome, descricao, valor_base, status,
        valor_final, tamanho,
        massa, recheio1, recheio2,
        cobertura, topping) = row

        return ProdutoPersonalizavel(
            id_produto=id_prod,
            nome=nome,
            descricao=descricao,
            valor_base=valor_base,
            status_disponibilidade=status,
            valor_final=valor_final,
            tamanho=tamanho,
            massa=Massa(massa, True),
            recheio1=Recheio(recheio1, True, 0),
            recheio2=Recheio(recheio2, True, 0),
            cobertura=Cobertura(cobertura, True),
            topping=Topping(topping, True) if topping else None
        )

    def listar_personalizaveis(self):
        return self.listar_todos()
    
    def buscar_personalizavel_por_id(self, id_produto):
        return self.buscar_por_id(id_produto)
    
    def inserir_personalizavel(self, produto):
        # Implementar inserção se necessário
        pass
    
    def atualizar_personalizavel(self, produto):
        # Implementar atualização se necessário
        pass
