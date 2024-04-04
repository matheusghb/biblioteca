from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.esta_disponivel():
                    livro.alterar_status("emprestado")
                    print(f"{livro.titulo} foi emprestado.")
                else:
                    print("Este livro já está emprestado.")
                return
        print("Livro não encontrado na biblioteca.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if not livro.esta_disponivel():
                    livro.alterar_status("disponível")
                    print(f"{livro.titulo} foi devolvido.")
                else:
                    print("Este livro já está disponível.")
                return
        print("Livro não encontrado na biblioteca.")

    def listar_livros_disponiveis(self):
        print("Livros disponíveis na biblioteca:")
        for livro in self.livros:
            if livro.esta_disponivel():
                print(f"- {livro.titulo} (Autor: {livro.autor}, Ano: {livro.ano_publicacao})")
