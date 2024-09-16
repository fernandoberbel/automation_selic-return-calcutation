from datetime import datetime, date
from matplotlib import pyplot as plt
import numpy as np
from bcb import sgs

# 1. Filtrar dados da selic no período da questão.
data_inicial = date(2000, 1, 1)
data_final = date(2022, 3, 31)

selic = sgs.get({"selic": 11}, start=data_inicial, end=data_final)/100
selic
# 2. Calcular rentabilidade das janelas de 500 dias.
janelas_500_dias = ((1 + selic).rolling(window=500).apply(np.prod) - 1)
janelas_500_dias = janelas_500_dias.reset_index()
# 3. Criar range de datas na tabela.
janelas_500_dias["data_inicial"] = janelas_500_dias["Date"].shift(500)
janelas_500_dias = janelas_500_dias.dropna()
janelas_500_dias.columns = ["data_final", "retorno_selic_500d", data_inicial]
janelas_500_dias
# 4. Pegar o maior retorno.
maior_retorno = janelas_500_dias["retorno_selic_500d"].max()
gabarito = janelas_500_dias[janelas_500_dias["retorno_selic_500d"]
                            == maior_retorno]
gabarito
