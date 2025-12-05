from view.adminView import MenuAdmin

if __name__ == "__main__":
    try:
        menu = MenuAdmin()
        menu.exibir_menu_principal()
    except Exception as e:
        print(f"\nErro: {e}")
    finally:
        print("\nPressione Enter para encerrar...")
        input()