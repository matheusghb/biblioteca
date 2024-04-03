class biblio:
    def __init__ (self, titulo, autor, ano, status):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = status

biblioteca = []
alt = ''

while (alt != 's'):
    alt = input("Adicionar - a - emprestar - e - devolver - d - sair - s - ")

