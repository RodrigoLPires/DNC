class calculo_financeiro:

    def calculo_sac(valor_total, prazo_meses, taxa_anual, nominal_efetiva):
        saldo_sac = valor_total
        amortizacao = valor_total / prazo_meses

        if nominal_efetiva == 'E':
            taxa_mensal = (1+taxa_anual/100)**(1/12)-1
        elif nominal_efetiva == 'N':
            taxa_mensal = taxa_anual / 12 / 100
        
        contagem = 1
        total_juros = 0
        total_amortizacao = 0
        pgto_acumulado = 0
        dicionario = {}
        lista_parcela = []
        lista_valor_contratado = []
        lista_saldo_devedor = []
        lista_percentual_saldo_devedor = []
        lista_juros = []
        lista_juros_acumulados = []
        lista_amortizacao = []
        lista_amortizacao_acumulada = []
        lista_pgto = []
        lista_pgto_acumulado = []

        while contagem <= prazo_meses:
            juros = saldo_sac * taxa_mensal
            pgto = amortizacao + juros
            pgto_acumulado += pgto
            total_juros += juros
            saldo_sac -= amortizacao
            total_amortizacao += amortizacao
            
            lista_parcela.append(contagem)
            lista_valor_contratado.append(valor_total)
            lista_saldo_devedor.append(saldo_sac)
            lista_percentual_saldo_devedor.append(saldo_sac/valor_total)
            lista_juros.append(juros)
            lista_juros_acumulados.append(total_juros)
            lista_amortizacao.append(amortizacao)
            lista_amortizacao_acumulada.append(total_amortizacao)
            lista_pgto.append(pgto)
            lista_pgto_acumulado.append(pgto_acumulado)

            dicionario['Parcela'] = lista_parcela
            dicionario['Valor Contratado'] = lista_valor_contratado
            dicionario['Saldo Devedor'] = lista_saldo_devedor
            dicionario['% Saldo Devedor'] = lista_percentual_saldo_devedor
            dicionario['Juros'] = lista_juros
            dicionario['Juros Acum'] = lista_juros_acumulados
            dicionario['Amortizacao'] = lista_amortizacao
            dicionario['Amort Acum'] = lista_amortizacao_acumulada
            dicionario['Pgto'] = lista_pgto
            dicionario['Pgto Acum'] = lista_pgto_acumulado

            contagem += 1
        return dicionario

    def calculo_price(valor_total, prazo_meses, taxa_anual, nominal_efetiva):
        saldo_price = valor_total

        if nominal_efetiva == 'E':
            taxa_mensal = (1+taxa_anual/100)**(1/12)-1
        elif nominal_efetiva == 'N':
            taxa_mensal = taxa_anual / 12 / 100

        pgto_simulado = valor_total * taxa_mensal
        amortizacao = 0
        
        while saldo_price > 0:
            saldo_price = valor_total
            pgto_simulado += 0.01
            for i in range(prazo_meses):
                juros = saldo_price * taxa_mensal
                amortizacao = pgto_simulado - juros
                saldo_price -= amortizacao

        pgto = pgto_simulado

        contagem = 1
        saldo_price = valor_total
        total_juros = 0
        total_amortizacao = 0
        pgto_acumulado = 0

        dicionario = {}
        lista_parcela = []
        lista_valor_contratado = []
        lista_saldo_devedor = []
        lista_percentual_saldo_devedor = []
        lista_juros = []
        lista_juros_acumulados = []
        lista_amortizacao = []
        lista_amortizacao_acumulada = []
        lista_pgto = []
        lista_pgto_acumulado = []

        while contagem <= prazo_meses:
            juros = saldo_price * taxa_mensal
            total_juros += juros
            if contagem == prazo_meses:
                amortizacao = saldo_price
                pgto = amortizacao + juros
            else:
                amortizacao = pgto - juros
            pgto_acumulado += pgto
            total_amortizacao += amortizacao
            saldo_price -= amortizacao

            lista_parcela.append(contagem)
            lista_valor_contratado.append(valor_total)
            lista_saldo_devedor.append(saldo_price)
            lista_percentual_saldo_devedor.append(saldo_price/valor_total)
            lista_juros.append(juros)
            lista_juros_acumulados.append(total_juros)
            lista_amortizacao.append(amortizacao)
            lista_amortizacao_acumulada.append(total_amortizacao)
            lista_pgto.append(pgto)
            lista_pgto_acumulado.append(pgto_acumulado)

            dicionario['Parcela'] = lista_parcela
            dicionario['Valor Contratado'] = lista_valor_contratado
            dicionario['Saldo Devedor'] = lista_saldo_devedor
            dicionario['% Saldo Devedor'] = lista_percentual_saldo_devedor
            dicionario['Juros'] = lista_juros
            dicionario['Juros Acum'] = lista_juros_acumulados
            dicionario['Amortizacao'] = lista_amortizacao
            dicionario['Amort Acum'] = lista_amortizacao_acumulada
            dicionario['Pgto'] = lista_pgto
            dicionario['Pgto Acum'] = lista_pgto_acumulado

            contagem += 1
        return dicionario
