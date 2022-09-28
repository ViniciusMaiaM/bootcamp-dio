import pandas

df = pandas.read_csv("/home/viniciusm/Documents/python/bootcamp-dio/Cusro_Python_Pandas_Digital_Innovation-master/datasets/Gapminder.csv", on_bad_lines='skip',sep=';')
# on_bad_lines='skip', funciona como um substituto do error_on_bad_lines e ignora os erros da tabela
# sep=';', faz com que haja uma separação de linhas onde houver um ';'

print("\n",df.head()) #.head() faz uma listagem dos cinco primeiros itens do csv

df = df.rename(columns={"country":"Pais","continent":"Continente","year":"Ano","lifeExp":"Expectativa de vida","pop":"Pop Total","gdpPercap":"PIB"})
# .renamem faz a renomeação das colunas da tabela
#determinando df = df.rename faz com que a tabela receba as modificações determinadas

print("\n",df.head())

print("\n",df.shape) #retorna o total de linhas e colunas

print("\n",df.columns) #retorna apenas o nome das colunas

print("\n",df.dtypes) #retorna o tipo de dado armazenado em caad coluna