import csv

def carregar_acessos():
    X = []
    Y = []

    # abre um arquivo
    arquivo = open('classificacao/resources/acesso.csv', 'rb')
    # cria um leitor baseado no arquivo passado como parametro
    leitor = csv.reader(arquivo)
    # ignora a primeira linha com o cabecalho do arquivo
    leitor.next()

    for home, como_funciona, contato, comprou in leitor:
        X.append([int(home), int(como_funciona), int(contato)])
        Y.append(int(comprou))
    return X, Y

def carregar_buscas():
        X = []
        Y = []

        arquivo = open('classificacao/resources/busca.csv', 'rb')
        leitor = csv.reader(arquivo)
        leitor.next()

        for home,busca,logado,comprou in leitor:
            X.append([int(home), busca, int(logado)])
            Y.append(int(comprou))
        return X, Y