from banco import *
from pessoa import *

login = '111'
senha = '123'
p1 = Pessoa('joao', '111', '01/01/2001', senha)
p2 = Pessoa('maria', '222', '02/02/2002', 'admin')
c1 = Banco('11111', p1, 100.0)
c2 = Banco('22222', p2, 100.0)

if __name__ == '__main__':

    loginEntrada = login
    senhaEntrada = senha

    if loginEntrada == login and senhaEntrada == senha:
        print('Logado no sistema!')
        c1.sacar(10)
        c1.extrato()
        print('\n')
        c1.transfere_para(c2,20)
        c1.extrato()
        print( '\n' )
        c2.extrato()
    else:
        print('Login ou Senha incorretos!')
