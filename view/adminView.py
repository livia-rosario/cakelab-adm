from database.conexao import Database
from controller.ingredientesController import IngredientesController
from controller.produtosController import ProdutosController
from controller.tamanhosController import TamanhoController

class MenuAdmin:
    def __init__(self):
        self.db = Database()
        self.ingredientes_controller = IngredientesController(self.db)
        self.produtos_controller = ProdutosController(self.db)
        self.tamanho_controller = TamanhoController(self.db)

    def exibir_menu_principal(self):
        while True:
            print("\n" + "="*50)
            print("   SISTEMA ADMINISTRATIVO - CONFEITARIA")
            print("="*50)
            print("1 - Gerenciar Ingredientes")
            print("2 - Gerenciar Produtos")
            print("3 - Gerenciar Tamanhos")
            print("0 - Sair")
            print("="*50)
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.menu_ingredientes()
            elif opcao == "2":
                self.menu_produtos()
            elif opcao == "3":
                self.menu_tamanhos()
            elif opcao == "0":
                print("\nSaindo do sistema...")
                break
            else:
                print("\nOpção inválida! Tente novamente.")

    def menu_ingredientes(self):
        while True:
            print("\n" + "="*50)
            print("   GERENCIAR INGREDIENTES")
            print("="*50)
            print("1 - Gerenciar Massas")
            print("2 - Gerenciar Recheios")
            print("3 - Gerenciar Coberturas")
            print("4 - Gerenciar Toppings")
            print("0 - Voltar")
            print("="*50)
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.ingredientes_controller.menu_massas()
            elif opcao == "2":
                self.ingredientes_controller.menu_recheios()
            elif opcao == "3":
                self.ingredientes_controller.menu_coberturas()
            elif opcao == "4":
                self.ingredientes_controller.menu_toppings()
            elif opcao == "0":
                break
            else:
                print("\nOpção inválida! Tente novamente.")

    def menu_produtos(self):
        while True:
            print("\n" + "="*50)
            print("   GERENCIAR PRODUTOS")
            print("="*50)
            print("1 - Produtos Personalizáveis")
            print("2 - Produtos Não Personalizáveis")
            print("0 - Voltar")
            print("="*50)
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.produtos_controller.menu_personalizaveis()
            elif opcao == "2":
                self.produtos_controller.menu_nao_personalizaveis()
            elif opcao == "0":
                break
            else:
                print("\nOpção inválida! Tente novamente.")

    def menu_tamanhos(self):
        self.tamanho_controller.menu_tamanhos()


if __name__ == "__main__":
    menu = MenuAdmin()
    menu.exibir_menu_principal()