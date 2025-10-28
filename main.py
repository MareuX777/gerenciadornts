from func.funcitions import *
from tabulate import *

dicter = {
    'nome' : '',
    'notas' : [],
    'media' : [],
    'situação' : ''
}
lst = []



while True:
    inpat = int(input('~$ '))
    if inpat == 3:
        print('''
    1 – Cadastrar aluno e notas
    2 – Exibir relatório
    0 – Sair
''')
    elif inpat == 0:
        break
    elif inpat == 1:
        dicter['nome'] = str(input('~$(NOME) '))
        for x in range(3):
            nts = int(input('~$(NOTA) '))
            dicter['notas'].append(nts)
    elif inpat == 2:
        media = sum(dicter['notas']) / 3
        dicter['media'].append(media)
        dicter['situação'] = situation(media)
        lst.append(dicter)
        print(tabulate(lst))
        
        
        
        