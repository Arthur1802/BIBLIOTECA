class Livro:

    def __init__(self, titulo, ano_publicacao, autor):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.autor = autor

class LivroFisico(Livro):

    def __init__(self, titulo, ano_publicacao, autor, copias_disponiveis):
        super().__init__(titulo, ano_publicacao, autor)
        self.copias_disponiveis = copias_disponiveis
        self.livros_emprestados = []

    def emprestar(self, livro):
        if self.copias_disponiveis > 0:
            self.copias_disponiveis -= 1
            self.livros_emprestados.append(livro)
            return True
        else:
            return False

    def devolver(self, livro):
        self.copias_disponiveis += 1
        self.livros_emprestados.remove(livro)

class LivroDigital(Livro):

    def __init__(self, titulo, ano_publicacao, autor, formato, tamanho, url):
        super().__init__(titulo, ano_publicacao, autor)
        self.formato = formato
        self.tamanho = tamanho
        self.url = url

    def baixar_livro(self):
        # Logic to download the book based on the URL
        # This could involve making an HTTP request to the URL and saving the data to a file
        pass

class Biblioteca:

    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_livro(self, titulo):
        return [livro for livro in self.livros if livro.titulo == titulo]

    def realizar_emprestimo(self, usuario, livro):
        if isinstance(livro, LivroFisico):
            if livro.emprestar(usuario):
                # Update the usuario's list of borrowed books
                usuario.livros_em_posse.append(livro)
                return True
            else:
                return False
        else:
            # Download the book and add it to the usuario's list of downloaded books
            usuario.livros_baixados.append(livro.baixar_livro())
            return True

    def devolver_emprestimo(self, usuario, livro):
        if isinstance(livro, LivroFisico):
            livro.devolver(usuario)
            usuario.livros_em_posse.remove(livro)

    def buscar_usuario(self, id_busca):
        for usuario in self.usuarios:
            if usuario.codigo == id_busca or usuario.matricula == id_busca:
                return usuario

class Usuario:

    def __init__(self, nome, codigo_ou_matricula):
        self.nome = nome
        self.codigo = codigo_ou_matricula if isinstance(codigo_ou_matricula, int) else None
        self.matricula = codigo_ou_matricula if isinstance(codigo_ou_matricula, str) else None
        self.livros_baixados = []
        self.livros_em_posse = []

# Example usage
biblioteca = Biblioteca()

livro1 = LivroFisico("O Senhor dos Anéis", 1954, "J.R.R. Tolkien", 5)
livro2 = LivroDigital("A Metamorfose", 1915, "Franz Kafka", "epub", 1024, "https://www.example.com/a-metamorfose.epub")

biblioteca.livros.append(livro1)
biblioteca.livros.append(livro2)

usuario1 = Usuario("João", 12345)
biblioteca.cadastrar_usuario(usuario1)

biblioteca.realizar_emprestimo(usuario1, livro1)
biblioteca.realizar_emprestimo(usuario1, livro2)

biblioteca.devolver_emprestimo(usuario1, livro1)

usuario2 = biblioteca.buscar_usuario(12345)

print(f"Livros baixados por {usuario2.nome}: {usuario2.livros_baixados}")
print(f"Livros em posse de {usuario2.nome}: {usuario2.livros_em_posse}")
