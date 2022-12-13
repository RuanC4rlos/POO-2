
class Pessoa:
    __slots__ = ['_nome','_cpf','_nascimento','_senha']

    def __init__(self,nome,cpf,nascimento,senha):
        self._nome = nome
        self._cpf = cpf
        self._nascimento = nascimento
        self._senha = senha

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, name):
        self._nome = name

    @property
    def senha(self):
        return self._senha

    @property
    def cpf(self):
        return self._cpf

    @property
    def nascimento(self):
        return self._nascimento






