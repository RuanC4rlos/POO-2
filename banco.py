import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print('- Data abertura: {}'.format(self.data_abertura))
        print('Transações: ')
        for t in self.transacoes:
            print('-', t)

class Banco:
    __slots__ = ['_numero', '_cliente', '_saldo', '_limite','_historico','_data','contas']

    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self._numero = numero
        self._cliente = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        self._data = None
        self.contas = []

    def sacar(self, valor):
        if valor <= self._saldo + self._limite:
            self._saldo -= float(valor)
            self._data = datetime.datetime.today()
            self._historico.transacoes.append("Data do saque: {}\n- Saque de {}".format( self._data, valor))
        else:
            print('Saldo insuficiente!')


    def depositar(self, valor):
        self._saldo += valor
        self._data = datetime.datetime.today()
        self._historico.transacoes.append("Data do deposito: {}\n- Deposito de {}".format(self._data, valor))

    def extrato(self):
        self._data = datetime.datetime.today()
        self._historico.transacoes.append( "Data do extrato: {}\n*** EXTRATO ***\n- Saldo de {}".format(self._data, self._saldo))
        self._historico.imprime()

    def transfere_para(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)
        self._data = datetime.datetime.today()
        self._historico.transacoes.append("Data da transferencia: {}\n- Transferencia de {} para conta {}".format( self._data, valor,destino._numero))
