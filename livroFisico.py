from livro import Livro
from helpers import *

class LivroFisico(Livro):
    def __init__ (self, titulo, id, autor, anoPublicacao, numCopiasDisp):
        super().__init__(titulo, id, autor, anoPublicacao)
        self.numCopiasDisp = numCopiasDisp

    def emprestarLivro(self, titulo, idUsuario):
        id = db.execute('''
                        SELECT id
                        FROM livros
                        WHERE titulo = ?
                        ''', titulo).fetchone()
        
        if id == None:
            print('Livro não encontrado')
            return False
        
        if self.numCopiasDisp == 0:
            print('Não há cópias disponíveis deste livro. Tente outro livro ou volte mais tarde.')
            return False
        
        else:
            db.execute('''
                        INSERT INTO emprestimos (idUsuario, idLivro, dataEmprestimo, dataDevolucao)
                        VALUES (?, ?, ?, ?)
                        ''', idUsuario, id, formatarData(gerarDataAtual(0)), formatarData(gerarDataAtual(0)))
            
            self.numCopiasDisp -= 1

        return True
    

    def devolverLivro(self, titulo, idUsuario):
        id = db.execute('''
                        SELECT id
                        FROM livros
                        WHERE titulo = ?
                        ''', titulo).fetchone()
        
        if id == None:
            print('Livro não encontrado')
            return False
        
        else:
            db.execute('''
                        DELETE FROM emprestimos
                        WHERE idUsuario = ? AND idLivro = ?
                        ''', idUsuario, id)
            
            self.numCopiasDisp += 1

        dataDevolucao1 = db.execute('''
                                    SELECT dataDevolucao
                                    FROM emprestimos
                                    WHERE idUsuario = ? AND idLivro = ?
                                    ''', idUsuario, id).fetchone()
        
        dataDevolucao2 = gerarDataAtual(0)

        if dataDevolucao1 > dataDevolucao2:
            print('Você devolveu o livro com atraso. Pague a multa de R$ 5,00.')

        elif dataDevolucao1 < dataDevolucao2:
            print('Você devolveu o livro com antecedência. Obrigado!')

        elif dataDevolucao1 == dataDevolucao2:
            print('Você devolveu o livro na data certa. Obrigado!')

        else:
            print('Erro ao devolver o livro. Tente novamente.')
            return False

        return True