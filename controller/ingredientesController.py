from repository.ingredientesRepository import IngredientesRepository
from model.ingredientesModel import Massa, Recheio, Cobertura, Topping

class IngredientesController:
    def __init__(self, db):
        self.repo = IngredientesRepository(db)

    def executar(self):
        while True:
            print("\n" + "="*50)
            print("   SISTEMA DE GERENCIAMENTO DE INGREDIENTES")
            print("="*50)
            print("1 - Gerenciar Massas")
            print("2 - Gerenciar Recheios")
            print("3 - Gerenciar Coberturas")
            print("4 - Gerenciar Toppings")
            print("0 - Sair")
            print("="*50)

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "1":
                self.menu_massas()
            elif opcao == "2":
                self.menu_recheios()
            elif opcao == "3":
                self.menu_coberturas()
            elif opcao == "4":
                self.menu_toppings()
            elif opcao == "0":
                print("\nSaindo do sistema. Até logo!")
                break
            else:
                print("\n Opção inválida!")

    # ==================== MASSAS ====================
    def menu_massas(self):
        while True:
            print("\n" + "="*50)
            print("   GERENCIAR MASSAS")
            print("="*50)
            print("1 - Listar todas as massas")
            print("2 - Buscar massa por ID")
            print("3 - Inserir nova massa")
            print("4 - Atualizar massa")
            print("5 - Deletar massa")
            print("0 - Voltar")
            print("="*50)
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.listar_massas()
            elif opcao == "2":
                self.buscar_massa()
            elif opcao == "3":
                self.inserir_massa()
            elif opcao == "4":
                self.atualizar_massa()
            elif opcao == "5":
                self.deletar_massa()
            elif opcao == "0":
                break
            else:
                print("\n Opção inválida!")

    def listar_massas(self):
        print("\n--- LISTA DE MASSAS ---")
        massas = self.repo.listar_massas()
        if not massas:
            print("Nenhuma massa cadastrada.")
            return
        for m in massas:
            status = " Disponível" if m.status_disponibilidade else " Indisponível"
            print(f"ID: {m.id_massa} | Nome: {m.nome} | Status: {status}")

    def buscar_massa(self):
        id_massa = input("\nDigite o ID da massa: ").strip()
        massa = self.repo.buscar_massa_por_id(id_massa)
        if massa:
            status = " Disponível" if massa.status_disponibilidade else " Indisponível"
            print(f"\nID: {massa.id_massa}")
            print(f"Nome: {massa.nome}")
            print(f"Status: {status}")
        else:
            print("\n Massa não encontrada!")

    def inserir_massa(self):
        print("\n--- INSERIR NOVA MASSA ---")
        nome = input("Nome: ").strip()
        status_disponibilidade = input("Disponível? (s/n): ").strip().lower() == 's'
        
        massa = Massa(nome, status_disponibilidade)
        try:
            self.repo.inserir_massa(massa)
            print("\n Massa inserida com sucesso!")
        except Exception as e:
            print(f"\n Erro ao inserir massa: {e}")

    def atualizar_massa(self):
        print("\n--- ATUALIZAR MASSA ---")
        id_massa = input("ID da massa: ").strip()
        massa = self.repo.buscar_massa_por_id(id_massa)
        
        if not massa:
            print("\n Massa não encontrada!")
            return
        
        print(f"\nDados atuais: {massa.nome} | Disponível: {massa.status_disponibilidade}")
        nome = input("Novo nome (Enter para manter): ").strip() or massa.nome
        status_input = input("Disponível? (s/n/Enter para manter): ").strip().lower()
        status = massa.status_disponibilidade if status_input == '' else (status_input == 's')
        
        massa_atualizada = Massa(nome, status, id_massa)
        try:
            self.repo.atualizar_massa(massa_atualizada)
            print("\n Massa atualizada com sucesso!")
        except Exception as e:
            print(f"\n Erro ao atualizar massa: {e}")

    def deletar_massa(self):
        id_massa = input("\nDigite o ID da massa a deletar: ").strip()
        confirma = input(f"Confirma a exclusão da massa '{id_massa}'? (s/n): ").strip().lower()
        
        if confirma == 's':
            try:
                self.repo.deletar_massa(id_massa)
                print("\n Massa deletada com sucesso!")
            except Exception as e:
                print(f"\n Erro ao deletar massa: {e}")
        else:
            print("\nOperação cancelada.")

    # ==================== RECHEIOS ====================
    def menu_recheios(self):
        while True:
            print("\n" + "="*50)
            print("   GERENCIAR RECHEIOS")
            print("="*50)
            print("1 - Listar todos os recheios")
            print("2 - Buscar recheio por ID")
            print("3 - Inserir novo recheio")
            print("4 - Atualizar recheio")
            print("5 - Deletar recheio")
            print("0 - Voltar")
            print("="*50)
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.listar_recheios()
            elif opcao == "2":
                self.buscar_recheio()
            elif opcao == "3":
                self.inserir_recheio()
            elif opcao == "4":
                self.atualizar_recheio()
            elif opcao == "5":
                self.deletar_recheio()
            elif opcao == "0":
                break
            else:
                print("\n Opção inválida!")

    def listar_recheios(self):
        print("\n--- LISTA DE RECHEIOS ---")
        recheios = self.repo.listar_recheios()
        if not recheios:
            print("Nenhum recheio cadastrado.")
            return
        for r in recheios:
            status = " Disponível" if r.status_disponibilidade else " Indisponível"
            print(f"ID: {r.id_recheio} | Nome: {r.nome} | Valor Adicional: R$ {r.valor_adc:.2f} | Status: {status}")

    def buscar_recheio(self):
        id_recheio = input("\nDigite o ID do recheio: ").strip()
        recheio = self.repo.buscar_recheio_por_id(id_recheio)
        if recheio:
            status = " Disponível" if recheio.status_disponibilidade else " Indisponível"
            print(f"\nID: {recheio.id_recheio}")
            print(f"Nome: {recheio.nome}")
            print(f"Valor Adicional: R$ {recheio.valor_adc:.2f}")
            print(f"Status: {status}")
        else:
            print("\n Recheio não encontrado!")

    def inserir_recheio(self):
        print("\n--- INSERIR NOVO RECHEIO ---")
        nome = input("Nome: ").strip()
        valor_adc = float(input("Valor adicional: ").strip())
        status = input("Disponível? (s/n): ").strip().lower() == 's'
        
        recheio = Recheio(nome, status, valor_adc)
        try:
            self.repo.inserir_recheio(recheio)
            print("\n Recheio inserido com sucesso!")
        except Exception as e:
            print(f"\n Erro ao inserir recheio: {e}")

    def atualizar_recheio(self):
        print("\n--- ATUALIZAR RECHEIO ---")
        id_recheio = input("ID do recheio: ").strip()
        recheio = self.repo.buscar_recheio_por_id(id_recheio)
        
        if not recheio:
            print("\n Recheio não encontrado!")
            return
        
        print(f"\nDados atuais: {recheio.nome} | R$ {recheio.valor_adc:.2f} | Disponível: {recheio.status_disponibilidade}")
        nome = input("Novo nome (Enter para manter): ").strip() or recheio.nome
        valor_input = input("Novo valor adicional (Enter para manter): ").strip()
        valor_adc = float(valor_input) if valor_input else recheio.valor_adc
        status_input = input("Disponível? (s/n/Enter para manter): ").strip().lower()
        status = recheio.status_disponibilidade if status_input == '' else (status_input == 's')
        
        recheio_atualizado = Recheio(nome, status, valor_adc, id_recheio)
        try:
            self.repo.atualizar_recheio(recheio_atualizado)
            print("\n Recheio atualizado com sucesso!")
        except Exception as e:
            print(f"\n Erro ao atualizar recheio: {e}")

    def deletar_recheio(self):
        id_recheio = input("\nDigite o ID do recheio a deletar: ").strip()
        confirma = input(f"Confirma a exclusão do recheio '{id_recheio}'? (s/n): ").strip().lower()
        
        if confirma == 's':
            try:
                self.repo.deletar_recheio(id_recheio)
                print("\n Recheio deletado com sucesso!")
            except Exception as e:
                print(f"\n Erro ao deletar recheio: {e}")
        else:
            print("\nOperação cancelada.")

    # ==================== COBERTURAS ====================
    def menu_coberturas(self):
        while True:
            print("\n" + "="*50)
            print("   GERENCIAR COBERTURAS")
            print("="*50)
            print("1 - Listar todas as coberturas")
            print("2 - Buscar cobertura por ID")
            print("3 - Inserir nova cobertura")
            print("4 - Atualizar cobertura")
            print("5 - Deletar cobertura")
            print("0 - Voltar")
            print("="*50)
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.listar_coberturas()
            elif opcao == "2":
                self.buscar_cobertura()
            elif opcao == "3":
                self.inserir_cobertura()
            elif opcao == "4":
                self.atualizar_cobertura()
            elif opcao == "5":
                self.deletar_cobertura()
            elif opcao == "0":
                break
            else:
                print("\n Opção inválida!")

    def listar_coberturas(self):
        print("\n--- LISTA DE COBERTURAS ---")
        coberturas = self.repo.listar_coberturas()
        if not coberturas:
            print("Nenhuma cobertura cadastrada.")
            return
        for c in coberturas:
            status = " Disponível" if c.status_disponibilidade else " Indisponível"
            print(f"ID: {c.id_cobertura} | Nome: {c.nome} | Status: {status}")

    def buscar_cobertura(self):
        id_cobertura = input("\nDigite o ID da cobertura: ").strip()
        cobertura = self.repo.buscar_cobertura_por_id(id_cobertura)
        if cobertura:
            status = " Disponível" if cobertura.status_disponibilidade else " Indisponível"
            print(f"\nID: {cobertura.id_cobertura}")
            print(f"Nome: {cobertura.nome}")
            print(f"Status: {status}")
        else:
            print("\n Cobertura não encontrada!")

    def inserir_cobertura(self):
        print("\n--- INSERIR NOVA COBERTURA ---")
        nome = input("Nome: ").strip()
        status = input("Disponível? (s/n): ").strip().lower() == 's'
        
        cobertura = Cobertura(nome, status)
        try:
            self.repo.inserir_cobertura(cobertura)
            print("\n Cobertura inserida com sucesso!")
        except Exception as e:
            print(f"\n Erro ao inserir cobertura: {e}")

    def atualizar_cobertura(self):
        print("\n--- ATUALIZAR COBERTURA ---")
        id_cobertura = input("ID da cobertura: ").strip()
        cobertura = self.repo.buscar_cobertura_por_id(id_cobertura)
        
        if not cobertura:
            print("\n Cobertura não encontrada!")
            return
        
        print(f"\nDados atuais: {cobertura.nome} | Disponível: {cobertura.status_disponibilidade}")
        nome = input("Novo nome (Enter para manter): ").strip() or cobertura.nome
        status_input = input("Disponível? (s/n/Enter para manter): ").strip().lower()
        status = cobertura.status_disponibilidade if status_input == '' else (status_input == 's')
        
        cobertura_atualizada = Cobertura(nome, status, id_cobertura)
        try:
            self.repo.atualizar_cobertura(cobertura_atualizada)
            print("\n Cobertura atualizada com sucesso!")
        except Exception as e:
            print(f"\n Erro ao atualizar cobertura: {e}")

    def deletar_cobertura(self):
        id_cobertura = input("\nDigite o ID da cobertura a deletar: ").strip()
        confirma = input(f"Confirma a exclusão da cobertura '{id_cobertura}'? (s/n): ").strip().lower()
        
        if confirma == 's':
            try:
                self.repo.deletar_cobertura(id_cobertura)
                print("\n✓ Cobertura deletada com sucesso!")
            except Exception as e:
                print(f"\n❌ Erro ao deletar cobertura: {e}")
        else:
            print("\nOperação cancelada.")

    # ==================== TOPPINGS ====================
    def menu_toppings(self):
        while True:
            print("\n" + "="*50)
            print("   GERENCIAR TOPPINGS")
            print("="*50)
            print("1 - Listar todos os toppings")
            print("2 - Buscar topping por ID")
            print("3 - Inserir novo topping")
            print("4 - Atualizar topping")
            print("5 - Deletar topping")
            print("0 - Voltar")
            print("="*50)
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.listar_toppings()
            elif opcao == "2":
                self.buscar_topping()
            elif opcao == "3":
                self.inserir_topping()
            elif opcao == "4":
                self.atualizar_topping()
            elif opcao == "5":
                self.deletar_topping()
            elif opcao == "0":
                break
            else:
                print("\nOpção inválida!")

    def listar_toppings(self):
        print("\n--- LISTA DE TOPPINGS ---")
        toppings = self.repo.listar_toppings()
        if not toppings:
            print("Nenhum topping cadastrado.")
            return
        for t in toppings:
            status = " Disponível" if t.status_disponibilidade else " Indisponível"
            print(f"ID: {t.id_topping} | Nome: {t.nome} | Valor Adicional: R$ {t.valor_adc:.2f} | Status: {status}")

    def buscar_topping(self):
        id_topping = input("\nDigite o ID do topping: ").strip()
        topping = self.repo.buscar_topping_por_id(id_topping)
        if topping:
            status = " Disponível" if topping.status_disponibilidade else " Indisponível"
            print(f"\nID: {topping.id_topping}")
            print(f"Nome: {topping.nome}")
            print(f"Valor Adicional: R$ {topping.valor_adc:.2f}")
            print(f"Status: {status}")
        else:
            print("\n Topping não encontrado!")

    def inserir_topping(self):
        print("\n--- INSERIR NOVO TOPPING ---")
        nome = input("Nome: ").strip()
        valor_adc = float(input("Valor adicional: ").strip())
        status = input("Disponível? (s/n): ").strip().lower() == 's'
        
        topping = Topping(nome, status, valor_adc)
        try:
            self.repo.inserir_topping(topping)
            print("\n Topping inserido com sucesso!")
        except Exception as e:
            print(f"\n Erro ao inserir topping: {e}")

    def atualizar_topping(self):
        print("\n--- ATUALIZAR TOPPING ---")
        id_topping = input("ID do topping: ").strip()
        topping = self.repo.buscar_topping_por_id(id_topping)
        
        if not topping:
            print("\n Topping não encontrado!")
            return
        
        print(f"\nDados atuais: {topping.nome} | R$ {topping.valor_adc:.2f} | Disponível: {topping.status_disponibilidade}")
        nome = input("Novo nome (Enter para manter): ").strip() or topping.nome
        valor_input = input("Novo valor adicional (Enter para manter): ").strip()
        valor_adc = float(valor_input) if valor_input else topping.valor_adc
        status_input = input("Disponível? (s/n/Enter para manter): ").strip().lower()
        status = topping.status_disponibilidade if status_input == '' else (status_input == 's')
        
        topping_atualizado = Topping(nome, status, valor_adc, id_topping)
        try:
            self.repo.atualizar_topping(topping_atualizado)
            print("\n Topping atualizado com sucesso!")
        except Exception as e:
            print(f"\n Erro ao atualizar topping: {e}")

    def deletar_topping(self):
        id_topping = input("\nDigite o ID do topping a deletar: ").strip()
        confirma = input(f"Confirma a exclusão do topping '{id_topping}'? (s/n): ").strip().lower()
        
        if confirma == 's':
            try:
                self.repo.deletar_topping(id_topping)
                print("\n✓ Topping deletado com sucesso!")
            except Exception as e:
                print(f"\n Erro ao deletar topping: {e}")
        else:
            print("\nOperação cancelada.")
