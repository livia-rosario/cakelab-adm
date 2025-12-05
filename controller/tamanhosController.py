from repository.tamanhoRepository import TamanhoRepository
from model.tamanhoModel import Tamanho

class TamanhoController:
    def __init__(self, db):
        self.repo = TamanhoRepository(db)

    def menu_tamanhos(self):
        while True:
            print("\n" + "="*50)
            print("   GERENCIAR TAMANHOS")
            print("="*50)
            print("1 - Listar todos os tamanhos")
            print("2 - Buscar tamanho")
            print("3 - Inserir novo tamanho")
            print("4 - Atualizar tamanho")
            print("5 - Deletar tamanho")
            print("0 - Voltar")
            print("="*50)
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.listar_tamanhos()
            elif opcao == "2":
                self.buscar_tamanho()
            elif opcao == "3":
                self.inserir_tamanho()
            elif opcao == "4":
                self.atualizar_tamanho()
            elif opcao == "5":
                self.deletar_tamanho()
            elif opcao == "0":
                break
            else:
                print("\n Opção inválida!")

    def listar_tamanhos(self):
        print("\n--- LISTA DE TAMANHOS ---")
        tamanhos = self.repo.listar_tamanhos()
        if not tamanhos:
            print("Nenhum tamanho cadastrado.")
            return
        for t in tamanhos:
            status = " Disponível" if t.status_disponibilidade else " Indisponível"
            print(f"Nome: {t.nome_tamanho} | Valor Base: R$ {t.valor_base:.2f} | Status: {status}")

    def buscar_tamanho(self):
        nome = input("\nDigite o nome do tamanho (P/M/G): ").strip().upper()
        tamanho = self.repo.buscar_tamanho(nome)
        if tamanho:
            status = " Disponível" if tamanho.status_disponibilidade else " Indisponível"
            print(f"\nNome: {tamanho.nome_tamanho}")
            print(f"Valor Base: R$ {tamanho.valor_base:.2f}")
            print(f"Status: {status}")
        else:
            print("\n Tamanho não encontrado!")

    def inserir_tamanho(self):
        print("\n--- INSERIR NOVO TAMANHO ---")
        nome = input("Nome do tamanho (ex: P, M, G): ").strip().upper()
        valor_base = float(input("Valor base: ").strip())
        status = input("Disponível? (s/n): ").strip().lower() == 's'
        
        tamanho = Tamanho(nome, valor_base, status)
        try:
            self.repo.inserir_tamanho(tamanho)
            print("\n Tamanho inserido com sucesso!")
        except Exception as e:
            print(f"\n Erro ao inserir tamanho: {e}")

    def atualizar_tamanho(self):
        print("\n--- ATUALIZAR TAMANHO ---")
        nome = input("Nome do tamanho: ").strip().upper()
        tamanho = self.repo.buscar_tamanho(nome)
        
        if not tamanho:
            print("\n Tamanho não encontrado!")
            return
        
        print(f"\nDados atuais: {tamanho.nome_tamanho} | R$ {tamanho.valor_base:.2f} | Disponível: {tamanho.status_disponibilidade}")
        
        valor_input = input("Novo valor base (Enter para manter): ").strip()
        valor_base = float(valor_input) if valor_input else tamanho.valor_base
        
        status_input = input("Disponível? (s/n/Enter para manter): ").strip().lower()
        status = tamanho.status_disponibilidade if status_input == '' else (status_input == 's')
        
        tamanho_atualizado = Tamanho(nome, valor_base, status)
        try:
            self.repo.atualizar_tamanho(tamanho_atualizado)
            print("\n Tamanho atualizado com sucesso!")
        except Exception as e:
            print(f"\n Erro ao atualizar tamanho: {e}")

    def deletar_tamanho(self):
        nome = input("\nDigite o nome do tamanho a deletar: ").strip().upper()
        confirma = input(f"Confirma a exclusão do tamanho '{nome}'? (s/n): ").strip().lower()
        
        if confirma == 's':
            try:
                self.repo.deletar_tamanho(nome)
                print("\n Tamanho deletado com sucesso!")
            except Exception as e:
                print(f"\n Erro ao deletar tamanho: {e}")
        else:
            print("\nOperação cancelada.")
