from ex115M.lib.interface import *
from ex115M.arquivo.arquivos import *
from time import sleep

arq = "CEV.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoa',  'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do programa
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        # Opção caso usuário digite errado no menu.
        print('\033[31mErro! Digite uma opção válida!\033[m')
        continue
    sleep(1.5)
