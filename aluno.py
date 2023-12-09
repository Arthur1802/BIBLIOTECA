from usuario import Usuario

class Aluno(Usuario):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email)
        self.matricula = matricula