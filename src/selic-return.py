# 1. Instalar e importar os módulos e bibliotecas.
from datetime import datetime, date
from matplotlib import pyplot as plt
from bcb import sgs

# 2. Coletar os dados do usuário.
capital = float(input("Digite o capital investido: "))
frequencia = input("Digite a frequência do período (Y, M, D): ")
inicio = input(
    "Digite a data inicial maior do que 1995/01/01 no formato YYYY/MM/DD: ")
final = input("Digite a data final no seguinte formato YYYY/MM/DD: ")
# 3. Tratar dados coletados.
data_inicial = datetime.strptime(inicio, "%Y/%m/%d").date()
data_final = datetime.strptime(final, "%Y/%m/%d").date()
# 4. Pegar dados da SELIC no banco central.
taxas_selic = sgs.get({"selic": 11}, start=data_inicial, end=data_final)
taxas_selic = taxas_selic/100
# 5. Calcular retorno do período.
capital_acumulado = capital * (1 + taxas_selic["selic"]).cumprod() - 1
capital_com_frequencia = capital_acumulado.resample(frequencia).last()
