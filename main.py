from biblioteca import Biblioteca
from livro import Livro

def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar livro")
    print("2. Emprestar livro")
    print("3. Devolver livro")
    print("4. Listar livros disponíveis")
    print("5. Sair")


if __name__ == "__main__":
    biblioteca = Biblioteca()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            ano = input("Digite o ano de publicação: ")
            livro = Livro(titulo, autor, ano)
            biblioteca.adicionar_livro(livro)
            print("Livro adicionado com sucesso.")

        elif escolha == "2":
            titulo = input("Digite o título do livro que deseja emprestar: ")
            biblioteca.emprestar_livro(titulo)

        elif escolha == "3":
            titulo = input("Digite o título do livro que deseja devolver: ")
            biblioteca.devolver_livro(titulo)

        elif escolha == "4":
            biblioteca.listar_livros_disponiveis()

        elif escolha == "5":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")
