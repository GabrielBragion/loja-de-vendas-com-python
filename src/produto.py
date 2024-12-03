# produto.py
class Produto:
    def __init__(self, nome, quantidade, preco, iva):
        self._nome = nome
        self._quantidade = quantidade
        self._preco = preco
        self._iva = iva

    # Getters
    def get_nome(self):
        return self._nome

    def get_quantidade(self):
        return self._quantidade

    def get_preco(self):
        return self._preco

    def get_iva(self):
        return self._iva

    # Setters
    def set_nome(self, nome):
        self._nome = nome

    def set_quantidade(self, quantidade):
        self._quantidade = quantidade

    def set_preco(self, preco):
        self._preco = preco

    def set_iva(self, iva):
        self._iva = iva

    def inserir(self, db):
        query = "INSERT INTO Produto (NomeProduto, QuantidadeInventario, Preco, IVA) VALUES (%s, %s, %s, %s)"
        values = (self._nome, self._quantidade, self._preco, self._iva)
        db.execute_query(query, values)

    def atualizar_preco(db,nome_produto, novo_preco):
        query = "UPDATE Produto SET Preco = %s WHERE NomeProduto = %s"
        values = ( novo_preco,nome_produto)
        db.execute_query(query, values)

    def reposicao(self, db, quantidade):
        self.set_quantidade(self.get_quantidade() + quantidade)
        query = "UPDATE Produto SET QuantidadeInventario = %s WHERE NomeProduto = %s"
        values = (self.get_quantidade(), self._nome)
        db.execute_query(query, values)

    def eliminar(self, db):
        query = "DELETE FROM Produto WHERE NomeProduto = %s"
        values = (self._nome,)
        db.execute_query(query, values)

    def listar(db):
        produtos = db.fetch_all("SELECT * FROM Produto")
        for produto in produtos:
            print(produto)