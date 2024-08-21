import numpy as np
import pandas as pd
import pathlib as pth


dir = pth.Path().parent.resolve()
print(dir)

df = pd.read_csv('./archives/DadosTratadosDolar.csv', sep = ',', encoding = 'iso-8859-1')

d = df.head()
print(d)