import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import warnings
from collections import Counter

warnings.filterwarnings('ignore', category=FutureWarning)

path = os.getcwd()
path = path[0:87]
path +='/archives/DadosTratadosDolar.csv'

dataFrame = pd.read_csv(path, sep = ',', encoding='iso-8859-1')

dataFrame.datas = dataFrame.datas.astype(str)

for i in range(0,7):
    valor = dataFrame.loc[i, 'datas']
    dataFrame.loc[i, 'datas'] = '0' + valor

dataFrame.datas = dataFrame.datas.apply(lambda x: x[:2] + '/' + x[2:4] + '/' + x[4:])
dataFrame.datas = pd.to_datetime(dataFrame.datas, format='%d/%m/%Y')

compra = dataFrame.compra

freq_absoluta = Counter(compra)

tabela = pd.DataFrame.from_dict(freq_absoluta, orient='index')
tabela = tabela.sort_index(ascending=True)
tabela.reset_index(inplace=True)
tabela = tabela.rename(columns={'index':'valor'})
tabela = tabela.rename(columns={0:'freq_abs'})

tabela['freq_rel'] = tabela.freq_abs/tabela.freq_abs.sum()
tabela['freq_acum'] = tabela.freq_abs.cumsum()
print('Entrada mínima:',tabela.valor.min())
print('Entrada máxima:',tabela.valor.max())
print('',tabela.valor.max()-tabela.valor.min())

classes = [5.3,5.4,5.5,5.6,5.7]
labels = ['5.3 - 5.4', '5.4 - 5.5', '5.5 - 5.6', '5.6 - 5.7']

intervalos = pd.cut(x = tabela.valor, bins = classes, labels = labels, include_lowest = True)

freq_abs = pd.value_counts(intervalos)
freq_rel = pd.value_counts(intervalos, normalize = True)

dist_freq = pd.DataFrame({'Frequência absoluta': freq_abs, 'Frequência relativa': freq_rel})
dist_freq.sort_index(ascending = True, inplace = True)
dist_freq['freq_rel_perc'] = np.round(dist_freq['Frequência relativa']*100,2)
dist_freq['freq_acum'] = dist_freq['Frequência absoluta'].cumsum()


#Histogrma com matplotlib
plt.hist(dataFrame.compra, bins = 5, color = 'red')
plt.title('Histograma')
plt.xlabel('Compra')
plt.ylabel('Frequência')
plt.show()