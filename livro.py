class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.status = "disponível"

    def esta_disponivel(self):
        return self.status == "disponível"

    def alterar_status(self, novo_status):
        self.status = novo_status
