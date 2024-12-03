class DetalheVenda:
    def __init__(self, id_venda, id_produto, quantidade_vendida):
        self.id_venda = id_venda
        self.id_produto = id_produto
        self.quantidade_vendida = quantidade_vendida

    def registrar(self, db):
        query = "INSERT INTO DetalheVenda (IDVenda, IDProduto, QuantidadeVendida) VALUES (%s, %s, %s)"
        db.execute_query(query, (self.id_venda, self.id_produto, self.quantidade_vendida))
