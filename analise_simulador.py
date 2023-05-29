import simulador_financiamento as sf
import pandas as pd

valor_total = 200000
prazo = 360
taxa = 7.66

#sf.calculo_financeiro.calculo_price(valor_total=valor_total, prazo_meses=prazo, taxa_anual=taxa, nominal_efetiva='N')

financimaneto_SAC = sf.calculo_financeiro.calculo_sac(valor_total=valor_total, prazo_meses=prazo, taxa_anual=taxa, nominal_efetiva='N')
financiamento_PRICE = sf.calculo_financeiro.calculo_price(valor_total=valor_total, prazo_meses=prazo, taxa_anual=taxa, nominal_efetiva='N')

tabela_SAC = pd.DataFrame(financimaneto_SAC)
tabela_PRICE = pd.DataFrame(financiamento_PRICE)
pd.options.display.float_format = '{:2.4f}'.format

lista_SAC_Pgto_Acum = list(tabela_SAC['Pgto'])
lsita_PRICE_Pgto_Acum = list(tabela_PRICE['Pgto'])

dict_Pgto_Acum = {}

dict_Pgto_Acum['SAC'] = lista_SAC_Pgto_Acum
dict_Pgto_Acum['PRICE'] = lsita_PRICE_Pgto_Acum

novo_data_frame = pd.DataFrame(dict_Pgto_Acum)

novo_data_frame['Diferenca'] = novo_data_frame['SAC'] - novo_data_frame['PRICE']

valor_acumulado = 0
novo_data_frame['Diferenca Pgto Acum'] = 0
novo_data_frame['Juros'] = 0
for i in range(len(novo_data_frame)):
    valor_atual = novo_data_frame['Diferenca'][i]
    valor_acumulado += valor_atual
    #print(valor_acumulado)
    novo_data_frame['Diferenca Pgto Acum'][i] = valor_acumulado
    novo_data_frame['Juros'][i] = novo_data_frame['Diferenca Pgto Acum'][i] * (0.5/100)

# for i in range(len(novo_data_frame)):

print(novo_data_frame)
tabela_SAC.info()
novo_data_frame.info()
