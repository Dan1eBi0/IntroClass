class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def info(self):
        print(f"O nome do autor é: {self.autor} e o título é: {self.titulo}")


livro1 = Livro("A montanha mágica", "Thomas Mann")
livro2 = Livro("Ensaio sobre a cegueira", "José Saramago")

livro1.info()
livro2.info()