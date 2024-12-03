class Venda:
    def __init__(self, data_venda, hora_venda):
        self.data_venda = data_venda
        self.hora_venda = hora_venda

    @staticmethod
    def registrar_venda(db):
        data = input("Data da Venda (YYYY-MM-DD): ")
        hora = input("Hora da Venda (HH:MM:SS): ")
        db.execute_query("INSERT INTO Venda (DataVenda, HoraVenda) VALUES (%s, %s)", (data, hora))

    @staticmethod
    def listar(db):
        vendas = db.fetch_all("SELECT * FROM Venda")
        for venda in vendas:
            print(venda)
