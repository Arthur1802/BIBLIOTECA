from usuario import Usuario

class Professor(Usuario):
    def __init__(self, nome, email, codigo):
        super().__init__(nome, email)
        self.codigo = codigo