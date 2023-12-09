from datetime import datetime, timedelta
from cs50 import SQL

# Cursor para a base de dados
db = SQL("sqlite:///biblioteca.db")

def formatarData(data):
    return data[8:10] + '/' + data[5:7] + '/' + data[0:4]


def gerarDataAtual(adicionarDias):
    return datetime.now() + timedelta(days = adicionarDias)


def gerarHorarioAtual():
    return datetime.now().time()