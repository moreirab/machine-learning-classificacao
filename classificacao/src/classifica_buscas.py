# importa a biblioteca pandas que eh utilizada para analise de dados
import pandas

# le o arquivo csv e obtem o data frame (df)
df = pandas.read_csv('classificacao/resources/busca.csv')

# por convencao, o sufixo 'df' indica que o objeto eh um data frame
X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

# obtem as variaveis categoricas como variaveis binarias
Xdummies_df = pandas.get_dummies(X_df)
Ydummies_df = Y_df

# converte o data frame em array
X = Xdummies_df.values
Y = Ydummies_df.values