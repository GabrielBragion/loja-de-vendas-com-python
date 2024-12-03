from src.db_connection import DatabaseConnection
from src.produto import Produto
from src.venda import Venda
from src.detalhe_venda import DetalheVenda

def menu_principal():
    print("\nMenu Principal")
    print("1. Gestão de Produtos")
    print("2. Gestão de Vendas")
    print("3. Sair")
    return int(input("Escolha uma opção: "))

def menu_produtos():
    print("\nGestão de Produtos")
    print("1. Inserir Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Preço")
    print("4. Repor Produto")
    print("5. Eliminar Produto")
    print("6. Voltar")
    return int(input("Escolha uma opção: "))

def menu_vendas():
    print("\nGestão de Vendas")
    print("1. Registrar Venda")
    print("2. Listar Vendas")
    print("3. Voltar")
    return int(input("Escolha uma opção: "))

def main():
    db = DatabaseConnection(host="localhost", user="root", password="Ga130196#", database="VendaProduto")

    while True:
        escolha = menu_principal()
        if escolha == 1:
            while True:
                opcao = menu_produtos()
                if opcao == 1:
                    nome = input("Nome do Produto: ")
                    quantidade = int(input("Quantidade: "))
                    preco = float(input("Preço: "))
                    iva = float(input("IVA: "))
                    produto = Produto(nome, quantidade, preco, iva)
                    produto.inserir(db)
                elif opcao == 2:
                    Produto.listar(db)
                elif opcao == 3:
                    nome_produto = input("Digite o nome do produto:")
                    novo_preco = int(input("Novo preço: "))
                    Produto.atualizar_preco(db, nome_produto ,novo_preco)
                elif opcao == 4:
                    Produto.reposicao(db)
                elif opcao == 5:
                    Produto.eliminar(db)
                elif opcao == 6:
                    break
        elif escolha == 2:
            while True:
                opcao = menu_vendas()
                if opcao == 1:
                    Venda.registrar_venda(db)
                elif opcao == 2:
                    Venda.listar(db)
                elif opcao == 3:
                    break
        elif escolha == 3:
            db.close()
            break

if __name__ == "__main__":
    main()
