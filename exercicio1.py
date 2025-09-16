"from datetime import datetime

class Livro:
    def __init__(self, isbn, titulo, autor, copias_totais):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__copias_totais = copias_totais
        self.__copias_disponiveis = copias_totais
        self.__emprestimos = []

    def registrar_emprestimo(self, data=None):
        if data is None:
            data = datetime.now().isoformat(sep=' ', timespec='seconds')
        self.__emprestimos.append(data)

    def emprestar(self):
        if self.__copias_disponiveis > 0:
            self.__copias_disponiveis -= 1
            self.registrar_emprestimo()
            return True
        return False

    def devolver(self):
        if self.__copias_disponiveis < self.__copias_totais:
            self.__copias_disponiveis += 1
            return True
        return False

    def get_titulo(self):
        return self.__titulo

    def get_disponibilidade(self):
        return self.__copias_disponiveis

    def get_historico_emprestimos(self):
        return list(self.__emprestimos)

    def __str__(self):
        return f"'{self.__titulo}' de {self.__autor} (ISBN: {self.__isbn}) - Disponíveis: {self.__copias_disponiveis}/{self.__copias_totais}"


biblioteca = []

livro1 = Livro("9788574801414", "Dom Casmurro", "Machado de Assis", 3)
livro2 = Livro("9788535914849", "1984", "George Orwell", 5)

biblioteca.append(livro1)
biblioteca.append(livro2)

print(f"Emprestando '{livro1.get_titulo()}': {livro1.emprestar()}")
print(f"Disponibilidade: {livro1.get_disponibilidade()}")
print(f"Emprestando '{livro1.get_titulo()}': {livro1.emprestar()}")
print(f"Disponibilidade: {livro1.get_disponibilidade()}")
print(f"Devolvendo '{livro1.get_titulo()}': {livro1.devolver()}")
print(f"Disponibilidade: {livro1.get_disponibilidade()}")
print(f"Total de empréstimos: {livro1.get_historico_emprestimos()}")
print()
print("Representação do livro:", livro1) " o que é pra aparecer
