class Livro:
    def __init__ (self, titulo, autor, ano, status):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = status

    def verif_disp (self):
        if (self.status == 1):
            print ("O livro atualmente está indisponível, emprestado. ")
        else:
            print ("O livro está disponível. ")

    def alter_disp (self):
        if (self.status == 1):
            self.status = 0
        else:
            self.status = 1
    def 
