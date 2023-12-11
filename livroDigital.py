from livro import Livro
from helpers import *

class LivroDigital(Livro):
    def __init__(self, titulo, id, autor, anoPublicacao, formato, tamanho, url):
        super().__init__(titulo, id, autor, anoPublicacao)
        self.formato = formato
        self.tamanho = tamanho
        self.url = url

    
    def baixarLivro(titulo):
        id = db.execute('''
                        SELECT id
                        FROM livros 
                        WHERE titulo = ?
                        ''', titulo).fetchone()
        
        if id == None:
            print('Livro não encontrado')
            return False
        
        else:
            print('Livro encontrado')
            # Implementar download do livro