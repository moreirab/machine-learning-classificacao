from dados import carregar_acessos

# carrega todos os dados
X,Y = carregar_acessos()

# separa as primeiras 90 linhas para treinar o algoritmo
treino_dados = X[:90]
treino_marcacoes = Y[:90]

# separa as 9 ultimas linhas para testar o algoritmo
teste_dados = X[-9:]
teste_marcacoes = Y[-9:]

# cria o modelo e treina com os dados e marcacoes que foram separadas acima
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

# testa o algoritmo com os dados separados para teste
resultado_teste = modelo.predict(teste_dados)
diferencas = resultado_teste - teste_marcacoes
acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(taxa_de_acerto)
print(total_de_elementos)