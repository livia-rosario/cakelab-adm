# Sistema de Gerenciamento de Confeitaria Personalizada

## 📋 Descrição do Projeto

O **Sistema de Gerenciamento de Confeitaria Personalizada** é uma aplicação de desktop desenvolvida para facilitar a gestão administrativa de uma confeitaria. O sistema permite:

- **Gerenciar Ingredientes**: Controlar massas, recheios, coberturas e toppings
- **Gerenciar Produtos**: Administrar produtos personalizáveis (bolos com seleção de ingredientes) e não personalizáveis (bebidas, itens para festa, bolos prontos)
- **Gerenciar Tamanhos**: Configurar diferentes tamanhos de produtos com seus respectivos valores base
- **Controlar Disponibilidade**: Marcar ingredientes e produtos como disponíveis ou indisponíveis

A aplicação utiliza um banco de dados relacional para armazenar todas as informações e oferece uma interface de menu de texto interativa para facilitar o uso.

## 🛠️ Tecnologias Utilizadas

### Linguagem
- **Python 3.8+**: Linguagem de programação principal

### Frameworks e Bibliotecas
- **psycopg2**: Driver PostgreSQL para conexão com banco de dados
- **python-dotenv**: Gerenciamento de variáveis de ambiente

### Banco de Dados
- **PostgreSQL/Supabase**: Banco de dados relacional para armazenar informações da confeitaria

### Arquitetura
- **Padrão MVC (Model-View-Controller)**: 
  - **Models**: Definição das entidades (Massa, Recheio, Produto, etc.)
  - **Controllers**: Lógica de negócios e fluxo de interação
  - **Repositories**: Acesso aos dados no banco de dados
  - **Views**: Interface de usuário (menu administrativo)

## 📁 Estrutura do Projeto

```
confeitaria_personalizada/
├── main.py                           # Ponto de entrada da aplicação
├── requirements.txt                  # Dependências do projeto
├── .env                             # Variáveis de ambiente (não incluir no git)
│
├── database/
│   ├── __init__.py
│   └── conexao.py                   # Classe de conexão com banco de dados
│
├── model/                           # Modelos de dados
│   ├── __init__.py
│   ├── ingredientesModel.py         # Massa, Recheio, Cobertura, Topping
│   ├── produtoModel.py              # Modelo genérico de Produto
│   ├── produtoPersonalizavelModel.py # Produtos personalizáveis
│   ├── produtoNaoPersonalizavelModel.py # Bebidas, Bolos prontos, Itens festa
│   └── tamanhoModel.py              # Modelo de Tamanho
│
├── repository/                      # Repositórios de acesso a dados
│   ├── __init__.py
│   ├── ingredientesRepository.py    # Operações CRUD de ingredientes
│   ├── produtoRepository.py         # Repositório genérico de produtos
│   ├── produtoPersonalizadoRepo.py  # Operações de produtos personalizáveis
│   ├── produtoNaoPersonalizadoRepo.py # Operações de produtos não personalizáveis
│   └── tamanhoRepository.py         # Operações CRUD de tamanhos
│
├── controller/                      # Controllers
│   ├── __init__.py
│   ├── ingredientesController.py    # Controle de ingredientes
│   ├── produtosController.py        # Controle de produtos
│   └── tamanhosController.py        # Controle de tamanhos
│
└── view/
    ├── __init__.py
    └── adminView.py                 # Interface de menu administrativo
```

## 🚀 Como Executar o Programa

### Pré-requisitos
- Python 3.8 ou superior instalado
- PostgreSQL ou acesso a um banco Supabase
- Git (para clonar o repositório)

### Passo 1: Clonar o Repositório
```bash
git clone https://github.com/juliaborgesc/confeitaria_personalizada.git
cd confeitaria_personalizada
```

### Passo 2: Instalar Dependências
```bash
pip install -r requirements.txt
```

### Passo 3: Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
SUPABASE_HOST=seu_host_aqui
SUPABASE_DB=seu_database_aqui
SUPABASE_USER=seu_usuario_aqui
SUPABASE_PASSWORD=sua_senha_aqui
SUPABASE_PORT=5432
```

### Passo 4: Executar a Aplicação
```bash
python main.py
```

A aplicação abrirá um menu interativo onde você pode:
1. **Gerenciar Ingredientes**: Adicionar, editar, deletar e listar massas, recheios, coberturas e toppings
2. **Gerenciar Produtos**: Administrar produtos personalizáveis e não personalizáveis
3. **Gerenciar Tamanhos**: Configurar tamanhos disponíveis

## 📦 Dependências

As dependências estão listadas em `requirements.txt`:
- psycopg2==2.9.11
- psycopg2-binary==2.9.10
- python-dotenv==1.0.1

## 🔗 Repositório GitHub

O código completo está disponível em:
```
https://github.com/juliaborgesc/confeitaria_personalizada
```

## 📝 Notas Importantes

- Certifique-se de que o banco de dados está configurado corretamente antes de executar
- Todas as senhas e dados sensíveis devem estar no arquivo `.env` (não commitar no git)
- O banco de dados deve ter as tabelas criadas conforme o schema esperado pela aplicação

## 👨‍💻 Autor

Desenvolvido por: Cauã Gilberto, Julia Borges, Jullyana Breciani, Livia Rosário
