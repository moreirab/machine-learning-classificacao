# [1] eh gordinho?
# [2] tem perna curta?
# [3] ele late?
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

# adiciona os elementos em um array
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
# define o que cada dado do array anterior eh; 1 = porco e -1 = cachorro
marcacoes = [1, 1, 1, -1, -1, -1]

# cria os elementos que nao sabemos identificar o que eh
misterioso1 = [0, 0, 0]
misterioso2 = [0, 0, 1]
misterioso3 = [0, 1, 0]
misterioso4 = [0, 1, 1]
misterioso5 = [1, 0, 0]
misterioso6 = [1, 0, 1]
misterioso7 = [1, 1, 0]
misterioso8 = [1, 1, 1]
# adiciona os elementos em um array para testa-lo na funcao predict
testes = [misterioso1, misterioso2, misterioso3, misterioso4, misterioso5, misterioso6, misterioso7, misterioso8]
marcacoes_teste = [1, -1, 1, -1, 1, -1, 1, -1]

from sklearn.naive_bayes import MultinomialNB
# instancia um modelo
modelo = MultinomialNB()
# treina o modelo baseado nos dados e marcacoes existentes
modelo.fit(dados, marcacoes)
# obtem o resultado do algoritmo de predicao do modelo
resultado = modelo.predict(testes)

diferencas = resultado - marcacoes_teste

acertos = [d for d in diferencas if d==0]
total_de_acertos = len(acertos)
total_de_elementos = len(testes)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
print('Taxa de acerto')
print(taxa_de_acerto)
