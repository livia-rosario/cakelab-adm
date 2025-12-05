import tkinter as tk
from tkinter import ttk, messagebox, font

# Tente importar os módulos do seu projeto. 
# Se der erro, verifique se as pastas 'database', 'controller' e 'model' existem.
try:
    from database.conexao import Database
    from controller.ingredientesController import IngredientesController
    from controller.produtosController import ProdutosController
    from controller.tamanhosController import TamanhoController
    from model.tamanhoModel import Tamanho
    from model.ingredientesModel import Massa, Recheio, Cobertura, Topping
    from model.produtoNaoPersonalizavelModel import ProdutoNaoPersonalizavel
except ImportError as e:
    print(f"Erro de importação: {e}")
    print("Verifique se a estrutura de pastas está correta.")

class MenuAdminGUI:
    # Paleta de Cores
    COR_FUNDO = "#F9FAFB"
    COR_CARD = "#FFFFFF"
    COR_PRIMARIA = "#0F80C1"
    COR_SECUNDARIA = "#F4B400"
    COR_PERIGO = "#D7266A"
    COR_SUCESSO = "#10B981"
    COR_TEXTO_PRINCIPAL = "#1F2937"
    COR_TEXTO_SECUNDARIO = "#6B7280"
    COR_INPUT_BG = "#F3F4F6"
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Administrativo - Confeitaria")
        self.root.geometry("900x700")
        self.root.configure(bg=self.COR_FUNDO)
        
        # Fontes
        self.fonte_titulo = font.Font(family="Segoe UI", size=24, weight="bold")
        self.fonte_subtitulo = font.Font(family="Segoe UI", size=14)
        self.fonte_botao = font.Font(family="Segoe UI", size=11, weight="bold")
        self.fonte_normal = font.Font(family="Segoe UI", size=10)
        
        # Inicializar controllers (Assumindo que as classes existem)
        try:
            self.db = Database()
            self.ingredientes_controller = IngredientesController(self.db)
            self.produtos_controller = ProdutosController(self.db)
            self.tamanho_controller = TamanhoController(self.db)
        except Exception as e:
            messagebox.showerror("Erro de Conexão", f"Não foi possível conectar ao banco ou controllers: {e}")

        self.criar_menu_principal()
    
    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def criar_botao(self, parent, texto, comando, cor_bg, largura=30):
        btn = tk.Button(
            parent, text=texto, command=comando, bg=cor_bg, fg="white",
            font=self.fonte_botao, relief="flat", bd=0, padx=20, pady=12,
            width=largura, cursor="hand2"
        )
        btn.bind("<Enter>", lambda e: btn.config(bg=self._escurecer_cor(cor_bg)))
        btn.bind("<Leave>", lambda e: btn.config(bg=cor_bg))
        return btn
    
    def _escurecer_cor(self, cor_hex):
        cor_hex = cor_hex.lstrip('#')
        r, g, b = tuple(int(cor_hex[i:i+2], 16) for i in (0, 2, 4))
        r, g, b = int(r * 0.85), int(g * 0.85), int(b * 0.85)
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def criar_header_voltar(self, parent, comando_voltar):
        header = tk.Frame(parent, bg=self.COR_FUNDO)
        header.pack(fill="x", pady=(0, 20))
        btn_voltar = tk.Button(
            header, text="← Voltar", command=comando_voltar,
            bg=self.COR_FUNDO, fg=self.COR_TEXTO_SECUNDARIO,
            font=("Segoe UI", 11), relief="flat", bd=0, cursor="hand2"
        )
        btn_voltar.pack(side="left")
    
    def criar_menu_principal(self):
        self.limpar_tela()
        container = tk.Frame(self.root, bg=self.COR_FUNDO)
        container.pack(expand=True, fill="both", padx=40, pady=40)
        
        titulo = tk.Label(container, text="🍰 Sistema Administrativo",
                         font=self.fonte_titulo, bg=self.COR_FUNDO, fg=self.COR_TEXTO_PRINCIPAL)
        titulo.pack(pady=(0, 5))
        
        subtitulo = tk.Label(container, text="CakeLab",
                            font=self.fonte_subtitulo, bg=self.COR_FUNDO, fg=self.COR_TEXTO_SECUNDARIO)
        subtitulo.pack(pady=(0, 30))
        
        card = tk.Frame(container, bg=self.COR_CARD, padx=40, pady=30)
        card.pack()
        
        self.criar_botao(card, "🧁 Gerenciar Ingredientes", self.menu_ingredientes, self.COR_PRIMARIA).pack(pady=6)
        self.criar_botao(card, "🎂 Gerenciar Produtos", self.menu_produtos, self.COR_SECUNDARIA).pack(pady=6)
        self.criar_botao(card, "📏 Gerenciar Tamanhos", lambda: self.tela_crud_tamanhos(), self.COR_SUCESSO).pack(pady=6)
        tk.Frame(card, bg=self.COR_CARD, height=15).pack()
        self.criar_botao(card, "✖ Sair", self.root.quit, self.COR_PERIGO).pack(pady=6)
    
    def menu_ingredientes(self):
        self.limpar_tela()
        container = tk.Frame(self.root, bg=self.COR_FUNDO)
        container.pack(expand=True, fill="both", padx=40, pady=40)
        
        self.criar_header_voltar(container, self.criar_menu_principal)
        
        titulo = tk.Label(container, text="Gerenciar Ingredientes",
                         font=self.fonte_titulo, bg=self.COR_FUNDO, fg=self.COR_TEXTO_PRINCIPAL)
        titulo.pack(pady=(0, 30))
        
        card = tk.Frame(container, bg=self.COR_CARD, padx=40, pady=30)
        card.pack()
        
        self.criar_botao(card, "🍞 Massas", lambda: self.tela_crud_massas(), self.COR_PRIMARIA).pack(pady=5)
        self.criar_botao(card, "🍫 Recheios", lambda: self.tela_crud_recheios(), self.COR_PRIMARIA).pack(pady=5)
        self.criar_botao(card, "🍯 Coberturas", lambda: self.tela_crud_coberturas(), self.COR_PRIMARIA).pack(pady=5)
        self.criar_botao(card, "✨ Toppings", lambda: self.tela_crud_toppings(), self.COR_PRIMARIA).pack(pady=5)
    
    def menu_produtos(self):
        self.limpar_tela()
        container = tk.Frame(self.root, bg=self.COR_FUNDO)
        container.pack(expand=True, fill="both", padx=40, pady=40)
        
        self.criar_header_voltar(container, self.criar_menu_principal)
        
        titulo = tk.Label(container, text="Gerenciar Produtos",
                         font=self.fonte_titulo, bg=self.COR_FUNDO, fg=self.COR_TEXTO_PRINCIPAL)
        titulo.pack(pady=(0, 30))
        
        card = tk.Frame(container, bg=self.COR_CARD, padx=40, pady=30)
        card.pack()
        
        self.criar_botao(card, "🎨 Produtos Personalizáveis", lambda: self.tela_crud_personalizaveis(), self.COR_SECUNDARIA).pack(pady=8)
        self.criar_botao(card, "📦 Produtos Não Personalizáveis", lambda: self.tela_crud_nao_personalizaveis(), self.COR_SECUNDARIA).pack(pady=8)
    
    # ==================== TELA CRUD GENÉRICA ====================
    def tela_crud_generica(self, titulo, lista_func, adicionar_func, editar_func, deletar_func, colunas, voltar_func):
        self.limpar_tela()
        container = tk.Frame(self.root, bg=self.COR_FUNDO)
        container.pack(expand=True, fill="both", padx=30, pady=30)
        
        self.criar_header_voltar(container, voltar_func)
        
        tk.Label(container, text=titulo, font=self.fonte_titulo,
                bg=self.COR_FUNDO, fg=self.COR_TEXTO_PRINCIPAL).pack(pady=(0, 20))
        
        # Card com tabela e botões
        card = tk.Frame(container, bg=self.COR_CARD, padx=20, pady=20)
        card.pack(fill="both", expand=True)
        
        # Frame da tabela
        frame_tabela = tk.Frame(card, bg=self.COR_CARD)
        frame_tabela.pack(fill="both", expand=True, pady=(0, 15))
        
        # Scrollbar
        scroll_y = tk.Scrollbar(frame_tabela)
        scroll_y.pack(side="right", fill="y")
        
        # Treeview
        tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings",
                           yscrollcommand=scroll_y.set, height=12)
        scroll_y.config(command=tree.yview)
        
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=120)
        
        tree.pack(fill="both", expand=True)
        
        # Botões de ação
        frame_botoes = tk.Frame(card, bg=self.COR_CARD)
        frame_botoes.pack(pady=10)
        
        self.criar_botao(frame_botoes, "➕ Adicionar", lambda: adicionar_func(tree), self.COR_SUCESSO, 15).pack(side="left", padx=5)
        self.criar_botao(frame_botoes, "✏️ Editar", lambda: editar_func(tree), self.COR_PRIMARIA, 15).pack(side="left", padx=5)
        self.criar_botao(frame_botoes, "🗑️ Deletar", lambda: deletar_func(tree), self.COR_PERIGO, 15).pack(side="left", padx=5)
        self.criar_botao(frame_botoes, "🔄 Atualizar", lambda: lista_func(tree), self.COR_SECUNDARIA, 15).pack(side="left", padx=5)
        
        # Carregar dados
        try:
            lista_func(tree)
        except Exception as e:
            print(f"Erro ao carregar lista: {e}")
    
    # ==================== TAMANHOS ====================
    def tela_crud_tamanhos(self):
        self.tela_crud_generica(
            "Gerenciar Tamanhos",
            self.listar_tamanhos,
            self.adicionar_tamanho,
            self.editar_tamanho,
            self.deletar_tamanho,
            ("Nome", "Valor Base", "Status"),
            self.criar_menu_principal
        )
    
    def listar_tamanhos(self, tree):
        for item in tree.get_children():
            tree.delete(item)
        tamanhos = self.tamanho_controller.repo.listar_tamanhos()
        for t in tamanhos:
            status = "✓ Disponível" if t.status_disponibilidade else "✗ Indisponível"
            tree.insert("", "end", values=(t.nome_tamanho, f"R$ {t.valor_base:.2f}", status))
    
    def adicionar_tamanho(self, tree):
        # Esta função foi reconstruída pois estava faltando no código original
        janela = tk.Toplevel(self.root)
        janela.title("Adicionar Tamanho")
        janela.geometry("400x300")
        janela.configure(bg=self.COR_FUNDO)
        
        frame = tk.Frame(janela, bg=self.COR_CARD, padx=30, pady=30)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Nome (P/M/G):", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_nome = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_nome.pack(fill="x", pady=(0, 15))
        
        tk.Label(frame, text="Valor Base:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_valor = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_valor.pack(fill="x", pady=(0, 15))
        
        var_status = tk.BooleanVar(value=True)
        tk.Checkbutton(frame, text="Disponível", variable=var_status, bg=self.COR_CARD,
                      font=self.fonte_normal, selectcolor=self.COR_SUCESSO).pack(anchor="w", pady=(0, 20))
        
        def salvar():
            try:
                tamanho = Tamanho(entry_nome.get().strip().upper(), float(entry_valor.get()), var_status.get())
                self.tamanho_controller.repo.inserir_tamanho(tamanho)
                messagebox.showinfo("Sucesso", "Tamanho adicionado!")
                janela.destroy()
                self.listar_tamanhos(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        
        self.criar_botao(frame, "Salvar", salvar, self.COR_SUCESSO, 15).pack()

    def editar_tamanho(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um tamanho!")
            return
        
        valores = tree.item(selecionado[0])['values']
        nome_original = valores[0]
        
        tamanho = self.tamanho_controller.repo.buscar_tamanho(nome_original)
        if not tamanho:
            messagebox.showerror("Erro", "Tamanho não encontrado!")
            return
        
        janela = tk.Toplevel(self.root)
        janela.title("Editar Tamanho")
        janela.geometry("400x300")
        janela.configure(bg=self.COR_FUNDO)
        
        frame = tk.Frame(janela, bg=self.COR_CARD, padx=30, pady=30)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Nome (P/M/G):", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_nome = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_nome.insert(0, tamanho.nome_tamanho)
        entry_nome.pack(fill="x", pady=(0, 15))
        
        tk.Label(frame, text="Valor Base:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_valor = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_valor.insert(0, str(tamanho.valor_base))
        entry_valor.pack(fill="x", pady=(0, 15))
        
        var_status = tk.BooleanVar(value=tamanho.status_disponibilidade)
        tk.Checkbutton(frame, text="Disponível", variable=var_status, bg=self.COR_CARD,
                      font=self.fonte_normal, selectcolor=self.COR_SUCESSO).pack(anchor="w", pady=(0, 20))
        
        def salvar():
            try:
                tamanho_atualizado = Tamanho(entry_nome.get().strip().upper(), float(entry_valor.get()), var_status.get())
                self.tamanho_controller.repo.atualizar_tamanho(tamanho_atualizado)
                messagebox.showinfo("Sucesso", "Tamanho atualizado!")
                janela.destroy()
                self.listar_tamanhos(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        
        self.criar_botao(frame, "Salvar", salvar, self.COR_PRIMARIA, 15).pack()
    
    def deletar_tamanho(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um tamanho!")
            return
        
        valores = tree.item(selecionado[0])['values']
        nome = valores[0]
        
        if messagebox.askyesno("Confirmar", f"Deletar tamanho '{nome}'?"):
            try:
                self.tamanho_controller.repo.deletar_tamanho(nome)
                messagebox.showinfo("Sucesso", "Tamanho deletado!")
                self.listar_tamanhos(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    # ==================== MASSAS ====================
    def tela_crud_massas(self):
        self.tela_crud_generica(
            "Gerenciar Massas",
            self.listar_massas,
            self.adicionar_massa,
            self.editar_massa,
            self.deletar_massa,
            ("ID", "Nome", "Status"),
            self.menu_ingredientes
        )
    
    def listar_massas(self, tree):
        for item in tree.get_children():
            tree.delete(item)
        massas = self.ingredientes_controller.repo.listar_massas()
        for m in massas:
            status = "✓ Disponível" if m.status_disponibilidade else "✗ Indisponível"
            tree.insert("", "end", values=(m.id_massa, m.nome, status))
    
    def adicionar_massa(self, tree):
        janela = tk.Toplevel(self.root)
        janela.title("Adicionar Massa")
        janela.geometry("400x250")
        janela.configure(bg=self.COR_FUNDO)
        
        frame = tk.Frame(janela, bg=self.COR_CARD, padx=30, pady=30)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Nome:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_nome = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_nome.pack(fill="x", pady=(0, 15))
        
        var_status = tk.BooleanVar(value=True)
        tk.Checkbutton(frame, text="Disponível", variable=var_status, bg=self.COR_CARD,
                      font=self.fonte_normal, selectcolor=self.COR_SUCESSO).pack(anchor="w", pady=(0, 20))
        
        def salvar():
            try:
                massa = Massa(entry_nome.get().strip(), var_status.get())
                self.ingredientes_controller.repo.inserir_massa(massa)
                messagebox.showinfo("Sucesso", "Massa adicionada!")
                janela.destroy()
                self.listar_massas(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        
        self.criar_botao(frame, "Salvar", salvar, self.COR_SUCESSO, 15).pack()
    
    def editar_massa(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma massa!")
            return
        
        valores = tree.item(selecionado[0])['values']
        id_massa = valores[0]
        
        massa = self.ingredientes_controller.repo.buscar_massa_por_id(id_massa)
        if not massa:
            messagebox.showerror("Erro", "Massa não encontrada!")
            return
        
        janela = tk.Toplevel(self.root)
        janela.title("Editar Massa")
        janela.geometry("400x250")
        janela.configure(bg=self.COR_FUNDO)
        
        frame = tk.Frame(janela, bg=self.COR_CARD, padx=30, pady=30)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Nome:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_nome = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_nome.insert(0, massa.nome)
        entry_nome.pack(fill="x", pady=(0, 15))
        
        var_status = tk.BooleanVar(value=massa.status_disponibilidade)
        tk.Checkbutton(frame, text="Disponível", variable=var_status, bg=self.COR_CARD,
                      font=self.fonte_normal, selectcolor=self.COR_SUCESSO).pack(anchor="w", pady=(0, 20))
        
        def salvar():
            try:
                massa_atualizada = Massa(entry_nome.get().strip(), var_status.get(), id_massa)
                self.ingredientes_controller.repo.atualizar_massa(massa_atualizada)
                messagebox.showinfo("Sucesso", "Massa atualizada!")
                janela.destroy()
                self.listar_massas(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        
        self.criar_botao(frame, "Salvar", salvar, self.COR_PRIMARIA, 15).pack()
    
    def deletar_massa(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma massa!")
            return
        
        valores = tree.item(selecionado[0])['values']
        id_massa = valores[0]
        
        if messagebox.askyesno("Confirmar", f"Deletar massa ID {id_massa}?"):
            try:
                self.ingredientes_controller.repo.deletar_massa(id_massa)
                messagebox.showinfo("Sucesso", "Massa deletada!")
                self.listar_massas(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    # ==================== RECHEIOS ====================
    def tela_crud_recheios(self):
        self.tela_crud_generica(
            "Gerenciar Recheios",
            self.listar_recheios,
            self.adicionar_recheio,
            self.editar_recheio,
            self.deletar_recheio,
            ("ID", "Nome", "Valor Adicional", "Status"),
            self.menu_ingredientes
        )
    
    def listar_recheios(self, tree):
        for item in tree.get_children():
            tree.delete(item)
        recheios = self.ingredientes_controller.repo.listar_recheios()
        for r in recheios:
            status = "✓ Disponível" if r.status_disponibilidade else "✗ Indisponível"
            tree.insert("", "end", values=(r.id_recheio, r.nome, f"R$ {r.valor_adc:.2f}", status))
    
    def adicionar_recheio(self, tree):
        janela = tk.Toplevel(self.root)
        janela.title("Adicionar Recheio")
        janela.geometry("400x320")
        janela.configure(bg=self.COR_FUNDO)
        
        frame = tk.Frame(janela, bg=self.COR_CARD, padx=30, pady=30)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Nome:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_nome = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_nome.pack(fill="x", pady=(0, 15))
        
        tk.Label(frame, text="Valor Adicional:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_valor = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_valor.pack(fill="x", pady=(0, 15))
        
        var_status = tk.BooleanVar(value=True)
        tk.Checkbutton(frame, text="Disponível", variable=var_status, bg=self.COR_CARD,
                      font=self.fonte_normal, selectcolor=self.COR_SUCESSO).pack(anchor="w", pady=(0, 20))
        
        def salvar():
            try:
                recheio = Recheio(entry_nome.get().strip(), var_status.get(), float(entry_valor.get()))
                self.ingredientes_controller.repo.inserir_recheio(recheio)
                messagebox.showinfo("Sucesso", "Recheio adicionado!")
                janela.destroy()
                self.listar_recheios(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        
        self.criar_botao(frame, "Salvar", salvar, self.COR_SUCESSO, 15).pack()
    
    def editar_recheio(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um recheio!")
            return
        
        valores = tree.item(selecionado[0])['values']
        id_recheio = valores[0]
        
        recheio = self.ingredientes_controller.repo.buscar_recheio_por_id(id_recheio)
        if not recheio:
            messagebox.showerror("Erro", "Recheio não encontrado!")
            return
        
        janela = tk.Toplevel(self.root)
        janela.title("Editar Recheio")
        janela.geometry("400x320")
        janela.configure(bg=self.COR_FUNDO)
        
        frame = tk.Frame(janela, bg=self.COR_CARD, padx=30, pady=30)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Nome:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_nome = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_nome.insert(0, recheio.nome)
        entry_nome.pack(fill="x", pady=(0, 15))
        
        tk.Label(frame, text="Valor Adicional:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_valor = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_valor.insert(0, str(recheio.valor_adc))
        entry_valor.pack(fill="x", pady=(0, 15))
        
        var_status = tk.BooleanVar(value=recheio.status_disponibilidade)
        tk.Checkbutton(frame, text="Disponível", variable=var_status, bg=self.COR_CARD,
                      font=self.fonte_normal, selectcolor=self.COR_SUCESSO).pack(anchor="w", pady=(0, 20))
        
        def salvar():
            try:
                recheio_atualizado = Recheio(entry_nome.get().strip(), var_status.get(), float(entry_valor.get()), id_recheio)
                self.ingredientes_controller.repo.atualizar_recheio(recheio_atualizado)
                messagebox.showinfo("Sucesso", "Recheio atualizado!")
                janela.destroy()
                self.listar_recheios(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        
        self.criar_botao(frame, "Salvar", salvar, self.COR_PRIMARIA, 15).pack()
    
    def deletar_recheio(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um recheio!")
            return
        
        valores = tree.item(selecionado[0])['values']
        id_recheio = valores[0]
        
        if messagebox.askyesno("Confirmar", f"Deletar recheio ID {id_recheio}?"):
            try:
                self.ingredientes_controller.repo.deletar_recheio(id_recheio)
                messagebox.showinfo("Sucesso", "Recheio deletado!")
                self.listar_recheios(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    # ==================== COBERTURAS ====================
    def tela_crud_coberturas(self):
        self.tela_crud_generica(
            "Gerenciar Coberturas",
            self.listar_coberturas,
            self.adicionar_cobertura,
            self.editar_cobertura,
            self.deletar_cobertura,
            ("ID", "Nome", "Status"),
            self.menu_ingredientes
        )
    
    def listar_coberturas(self, tree):
        for item in tree.get_children():
            tree.delete(item)
        coberturas = self.ingredientes_controller.repo.listar_coberturas()
        for c in coberturas:
            status = "✓ Disponível" if c.status_disponibilidade else "✗ Indisponível"
            tree.insert("", "end", values=(c.id_cobertura, c.nome, status))
    
    def adicionar_cobertura(self, tree):
        janela = tk.Toplevel(self.root)
        janela.title("Adicionar Cobertura")
        janela.geometry("400x250")
        janela.configure(bg=self.COR_FUNDO)
        
        frame = tk.Frame(janela, bg=self.COR_CARD, padx=30, pady=30)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Nome:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_nome = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_nome.pack(fill="x", pady=(0, 15))
        
        var_status = tk.BooleanVar(value=True)
        tk.Checkbutton(frame, text="Disponível", variable=var_status, bg=self.COR_CARD,
                      font=self.fonte_normal, selectcolor=self.COR_SUCESSO).pack(anchor="w", pady=(0, 20))
        
        def salvar():
            try:
                cobertura = Cobertura(entry_nome.get().strip(), var_status.get())
                self.ingredientes_controller.repo.inserir_cobertura(cobertura)
                messagebox.showinfo("Sucesso", "Cobertura adicionada!")
                janela.destroy()
                self.listar_coberturas(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        
        self.criar_botao(frame, "Salvar", salvar, self.COR_SUCESSO, 15).pack()
    
    def editar_cobertura(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma cobertura!")
            return
        
        valores = tree.item(selecionado[0])['values']
        id_cobertura = valores[0]
        
        cobertura = self.ingredientes_controller.repo.buscar_cobertura_por_id(id_cobertura)
        if not cobertura:
            messagebox.showerror("Erro", "Cobertura não encontrada!")
            return
        
        janela = tk.Toplevel(self.root)
        janela.title("Editar Cobertura")
        janela.geometry("400x250")
        janela.configure(bg=self.COR_FUNDO)
        
        frame = tk.Frame(janela, bg=self.COR_CARD, padx=30, pady=30)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Nome:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_nome = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_nome.insert(0, cobertura.nome)
        entry_nome.pack(fill="x", pady=(0, 15))
        
        var_status = tk.BooleanVar(value=cobertura.status_disponibilidade)
        tk.Checkbutton(frame, text="Disponível", variable=var_status, bg=self.COR_CARD,
                      font=self.fonte_normal, selectcolor=self.COR_SUCESSO).pack(anchor="w", pady=(0, 20))
        
        def salvar():
            try:
                cobertura_atualizada = Cobertura(entry_nome.get().strip(), var_status.get(), id_cobertura)
                self.ingredientes_controller.repo.atualizar_cobertura(cobertura_atualizada)
                messagebox.showinfo("Sucesso", "Cobertura atualizada!")
                janela.destroy()
                self.listar_coberturas(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        
        self.criar_botao(frame, "Salvar", salvar, self.COR_PRIMARIA, 15).pack()
    
    def deletar_cobertura(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma cobertura!")
            return
        
        valores = tree.item(selecionado[0])['values']
        id_cobertura = valores[0]
        
        if messagebox.askyesno("Confirmar", f"Deletar cobertura ID {id_cobertura}?"):
            try:
                self.ingredientes_controller.repo.deletar_cobertura(id_cobertura)
                messagebox.showinfo("Sucesso", "Cobertura deletada!")
                self.listar_coberturas(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    # ==================== TOPPINGS ====================
    def tela_crud_toppings(self):
        self.tela_crud_generica(
            "Gerenciar Toppings",
            self.listar_toppings,
            self.adicionar_topping,
            self.editar_topping,
            self.deletar_topping,
            ("ID", "Nome", "Valor Adicional", "Status"),
            self.menu_ingredientes
        )
    
    def listar_toppings(self, tree):
        for item in tree.get_children():
            tree.delete(item)
        toppings = self.ingredientes_controller.repo.listar_toppings()
        for t in toppings:
            status = "✓ Disponível" if t.status_disponibilidade else "✗ Indisponível"
            tree.insert("", "end", values=(t.id_topping, t.nome, f"R$ {t.valor_adc:.2f}", status))
    
    def adicionar_topping(self, tree):
        janela = tk.Toplevel(self.root)
        janela.title("Adicionar Topping")
        janela.geometry("400x320")
        janela.configure(bg=self.COR_FUNDO)
        
        frame = tk.Frame(janela, bg=self.COR_CARD, padx=30, pady=30)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Nome:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_nome = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_nome.pack(fill="x", pady=(0, 15))
        
        tk.Label(frame, text="Valor Adicional:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_valor = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_valor.pack(fill="x", pady=(0, 15))
        
        var_status = tk.BooleanVar(value=True)
        tk.Checkbutton(frame, text="Disponível", variable=var_status, bg=self.COR_CARD,
                      font=self.fonte_normal, selectcolor=self.COR_SUCESSO).pack(anchor="w", pady=(0, 20))
        
        def salvar():
            try:
                topping = Topping(entry_nome.get().strip(), var_status.get(), float(entry_valor.get()))
                self.ingredientes_controller.repo.inserir_topping(topping)
                messagebox.showinfo("Sucesso", "Topping adicionado!")
                janela.destroy()
                self.listar_toppings(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        
        self.criar_botao(frame, "Salvar", salvar, self.COR_SUCESSO, 15).pack()
    
    def editar_topping(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um topping!")
            return
        
        valores = tree.item(selecionado[0])['values']
        id_topping = valores[0]
        
        topping = self.ingredientes_controller.repo.buscar_topping_por_id(id_topping)
        if not topping:
            messagebox.showerror("Erro", "Topping não encontrado!")
            return
        
        janela = tk.Toplevel(self.root)
        janela.title("Editar Topping")
        janela.geometry("400x320")
        janela.configure(bg=self.COR_FUNDO)
        
        frame = tk.Frame(janela, bg=self.COR_CARD, padx=30, pady=30)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Nome:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_nome = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_nome.insert(0, topping.nome)
        entry_nome.pack(fill="x", pady=(0, 15))
        
        tk.Label(frame, text="Valor Adicional:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_valor = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_valor.insert(0, str(topping.valor_adc))
        entry_valor.pack(fill="x", pady=(0, 15))
        
        var_status = tk.BooleanVar(value=topping.status_disponibilidade)
        tk.Checkbutton(frame, text="Disponível", variable=var_status, bg=self.COR_CARD,
                      font=self.fonte_normal, selectcolor=self.COR_SUCESSO).pack(anchor="w", pady=(0, 20))
        
        def salvar():
            try:
                topping_atualizado = Topping(entry_nome.get().strip(), var_status.get(), float(entry_valor.get()), id_topping)
                self.ingredientes_controller.repo.atualizar_topping(topping_atualizado)
                messagebox.showinfo("Sucesso", "Topping atualizado!")
                janela.destroy()
                self.listar_toppings(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        
        self.criar_botao(frame, "Salvar", salvar, self.COR_PRIMARIA, 15).pack()
    
    def deletar_topping(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um topping!")
            return
        
        valores = tree.item(selecionado[0])['values']
        id_topping = valores[0]
        
        if messagebox.askyesno("Confirmar", f"Deletar topping ID {id_topping}?"):
            try:
                self.ingredientes_controller.repo.deletar_topping(id_topping)
                messagebox.showinfo("Sucesso", "Topping deletado!")
                self.listar_toppings(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
    
    # ==================== PRODUTOS PERSONALIZÁVEIS ====================
    def tela_crud_personalizaveis(self):
        self.tela_crud_generica(
            "Produtos Personalizáveis",
            self.listar_personalizaveis,
            lambda tree: messagebox.showinfo("Info", "Produtos personalizáveis são criados pelos clientes!"),
            lambda tree: messagebox.showinfo("Info", "Produtos personalizáveis não podem ser editados!"),
            lambda tree: messagebox.showinfo("Info", "Produtos personalizáveis não podem ser deletados!"),
            ("ID", "Nome", "Tamanho", "Valor Base", "Valor Final", "Status"),
            self.menu_produtos
        )
    
    def listar_personalizaveis(self, tree):
        for item in tree.get_children():
            tree.delete(item)
        produtos = self.produtos_controller.repo.listar_personalizaveis()
        for p in produtos:
            status = "✓ Disponível" if p.status_disponibilidade else "✗ Indisponível"
            tree.insert("", "end", values=(
                p.id_produto, p.nome, p.tamanho,
                f"R$ {p.valor_base:.2f}", f"R$ {p.valor_final:.2f}", status
            ))
    
    # ==================== PRODUTOS NÃO PERSONALIZÁVEIS ====================
    def tela_crud_nao_personalizaveis(self):
        self.tela_crud_generica(
            "Produtos Não Personalizáveis",
            self.listar_nao_personalizaveis,
            self.adicionar_nao_personalizavel,
            self.editar_nao_personalizavel,
            self.deletar_nao_personalizavel,
            ("ID", "Nome", "Valor", "Status"),
            self.menu_produtos
        )
    
    def listar_nao_personalizaveis(self, tree):
        for item in tree.get_children():
            tree.delete(item)
        produtos = self.produtos_controller.repo.listar_nao_personalizaveis()
        for p in produtos:
            status = "✓ Disponível" if p.status_disponibilidade else "✗ Indisponível"
            tree.insert("", "end", values=(p.id_produto, p.nome, f"R$ {p.valor_base:.2f}", status))
    
    def adicionar_nao_personalizavel(self, tree):
        janela = tk.Toplevel(self.root)
        janela.title("Adicionar Produto Não Personalizável")
        janela.geometry("450x400")
        janela.configure(bg=self.COR_FUNDO)
        
        frame = tk.Frame(janela, bg=self.COR_CARD, padx=30, pady=30)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Nome:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_nome = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_nome.pack(fill="x", pady=(0, 10))
        
        tk.Label(frame, text="Descrição:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_descricao = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_descricao.pack(fill="x", pady=(0, 10))
        
        tk.Label(frame, text="Valor:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_valor = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_valor.pack(fill="x", pady=(0, 10))
        
        var_status = tk.BooleanVar(value=True)
        tk.Checkbutton(frame, text="Disponível", variable=var_status, bg=self.COR_CARD,
                      font=self.fonte_normal, selectcolor=self.COR_SUCESSO).pack(anchor="w", pady=(0, 20))
        
        def salvar():
            try:
                produto = ProdutoNaoPersonalizavel(
                    entry_nome.get().strip(),
                    entry_descricao.get().strip(),
                    float(entry_valor.get()),
                    var_status.get()
                )
                self.produtos_controller.repo.inserir_nao_personalizavel(produto)
                messagebox.showinfo("Sucesso", "Produto adicionado!")
                janela.destroy()
                self.listar_nao_personalizaveis(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        
        self.criar_botao(frame, "Salvar", salvar, self.COR_SUCESSO, 15).pack()
    
    def editar_nao_personalizavel(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um produto!")
            return
        
        valores = tree.item(selecionado[0])['values']
        id_produto = valores[0]
        
        produto = self.produtos_controller.repo.buscar_nao_personalizavel_por_id(id_produto)
        if not produto:
            messagebox.showerror("Erro", "Produto não encontrado!")
            return
        
        janela = tk.Toplevel(self.root)
        janela.title("Editar Produto Não Personalizável")
        janela.geometry("450x400")
        janela.configure(bg=self.COR_FUNDO)
        
        frame = tk.Frame(janela, bg=self.COR_CARD, padx=30, pady=30)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Nome:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_nome = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_nome.insert(0, produto.nome)
        entry_nome.pack(fill="x", pady=(0, 10))
        
        tk.Label(frame, text="Descrição:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_descricao = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_descricao.insert(0, produto.descricao)
        entry_descricao.pack(fill="x", pady=(0, 10))
        
        tk.Label(frame, text="Valor:", bg=self.COR_CARD, fg=self.COR_TEXTO_PRINCIPAL, font=self.fonte_normal).pack(anchor="w", pady=(0, 5))
        entry_valor = tk.Entry(frame, bg=self.COR_INPUT_BG, relief="flat", bd=5, font=self.fonte_normal)
        entry_valor.insert(0, str(produto.valor_base))
        entry_valor.pack(fill="x", pady=(0, 10))
        
        var_status = tk.BooleanVar(value=produto.status_disponibilidade)
        tk.Checkbutton(frame, text="Disponível", variable=var_status, bg=self.COR_CARD,
                      font=self.fonte_normal, selectcolor=self.COR_SUCESSO).pack(anchor="w", pady=(0, 20))
        
        def salvar():
            try:
                produto_atualizado = ProdutoNaoPersonalizavel(
                    entry_nome.get().strip(),
                    entry_descricao.get().strip(),
                    float(entry_valor.get()),
                    var_status.get()
                )
                produto_atualizado.id_produto = id_produto
                self.produtos_controller.repo.atualizar_nao_personalizavel(produto_atualizado)
                messagebox.showinfo("Sucesso", "Produto atualizado!")
                janela.destroy()
                self.listar_nao_personalizaveis(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        
        self.criar_botao(frame, "Salvar", salvar, self.COR_PRIMARIA, 15).pack()
    
    def deletar_nao_personalizavel(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um produto!")
            return
        
        valores = tree.item(selecionado[0])['values']
        id_produto = valores[0]
        
        if messagebox.askyesno("Confirmar", f"Deletar produto ID {id_produto}?"):
            try:
                self.produtos_controller.repo.deletar_produto(id_produto)
                messagebox.showinfo("Sucesso", "Produto deletado!")
                self.listar_nao_personalizaveis(tree)
            except Exception as e:
                messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuAdminGUI(root)
    root.mainloop()