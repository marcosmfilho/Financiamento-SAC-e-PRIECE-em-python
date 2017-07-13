# PRECISAMOS SABER:
# O Sistema de Amortização Constante (SAC) é o tipo de financiamento mais usado pelos bancos atualmente.
# Nesse sistema, o valor da dívida amortizado mês a mês é constante, mas os juros pagos nas parcelas iniciais
# são maiores e vão diminuindo ao longo do tempo. Assim, os valores das prestações - que incluem a amortização
# do saldo devedor, os juros e outros encargos-, são decrescentes.

#Usaremos as variáveis:
# totalFinanciamento = Valor total do financiamento
# quantidadePeriodos = Quantidade de períodos
# taxaJuros = Taxa de juros
# amortizacao = Valor de Amortização Constante
# periodoAtual = Período
# decrescimoJuros = Valor de decréscimo constante de juros a cada período
# jurosNoPeriodo = Valor dos juros referente ao período k
# prestacao =  Prestação (Amortização + Juros do período)

#Onde:
# amortizacao = totalFinanciamento / quantidadePeriodos
# jurosNoPeriodo = (quantidadePeriodos - periodoAtual + 1) * taxaJuros * amortizacao
# decrescimoJuros = jurosNoPeriodo(periodoAtual) - jurosNoPeriodo(periodoAtual + 1)
# prestacao = amortizacao + jurosNoPeriodo(periodoAtual)

def financiamentoSAC(valorTotal, valorEntrada, taxaJuros, quantidadePeriodos):
    prestacoes = []
    jurosPeriodos = []
    saldosDevedoresPeriodo = []
    acumulado = 0
    totalFinanciamento = valorTotal - valorEntrada
    amortizacao = totalFinanciamento/quantidadePeriodos
    print("*************************************************")
    print("********* FINANCIAMENTO IMOBILIÁRIO SAC *********")
    print("*************************************************\n")
    print("Valor do imóvel: %d" % valorTotal)
    print("Valor de entrada: %d" % valorEntrada)
    print("Total Financiado: %d" % totalFinanciamento)
    print("Taxa de juros: %.3f" % taxaJuros+'%')
    print("Quantidade de períodos: %d" % quantidadePeriodos, '\n')
    #loop que percorre cada período
    for i in range(1, quantidadePeriodos + 1):
        # calcula a taxa de juros atual e joga na lista de juros por período
        jurosAtual = jurosPorPeriodoSAC(quantidadePeriodos, i, taxaJuros, amortizacao)
        # print(quantidadePeriodos, i, taxaJuros, amortizacao, jurosAtual, "\n")
        jurosPeriodos.append(jurosAtual)

        # calcula a prestação somando a amoritzação + juros atual e joga na lista de prestações
        prestacao = amortizacao + jurosAtual
        acumulado = acumulado + prestacao
        prestacoes.append(prestacao)

        #calcula o saldo devedor atual e joga na lista de saldos devidos por período
        saldoDevedorAtual = totalFinanciamento - (amortizacao * i)
        saldosDevedoresPeriodo.append(saldoDevedorAtual)
        print("Amortização: %d" % amortizacao," | Juros: %.2f" % jurosAtual, "| Parcela %d:" % i, "%.2f" % prestacao, "| Saldo devedor: %.2f" % saldoDevedorAtual)

    #Salvando todas as informações num array(table) caso queira salvar as informações num arquivo.
    print("\nO total pago, levando em consideração a taxa de juros, no modelo SAC foi de %.2f reais" % acumulado)
    tabelaFinanciamento = [[prestacoes], [jurosPeriodos], [saldosDevedoresPeriodo]]
    return tabelaFinanciamento

def jurosPorPeriodoSAC(quantidadePeriodos, periodoAtual, taxaJuros, amortizacao):
    juros = ((quantidadePeriodos - periodoAtual + 1) * taxaJuros * amortizacao)
    return juros

#Vamos agora adentrar no modo Price
#O modo Price utliza juros compostos e tem como característica apresentar parcelas iguais
#A prestacao é combinada utilizando a fórmula dos juros compostos combinada com a progressão geométrica
#parcela = valorAtual * ((((1+taxaJuros)**quantidadePeriodos)*taxaJuros)/(((1 + taxaJuros)**quantidadePeriodos) - 1))
#o juros é calculado saldoDevedor do mês anterior * taxaJuros
#A amortização é prestação - jurosAtual
#Saldo devedor é o saldo devedor do mês anterior subtraída da atual amortização
#sendo assim, vamos lá...

import sys

def parcelaPriece(valorAtual, taxaJuros, quantidadePeriodos):
    parcela = valorAtual * ((((1+taxaJuros)**quantidadePeriodos)*taxaJuros)/(((1 + taxaJuros)**quantidadePeriodos) - 1))
    return parcela

def fincanciamentoPriece(valorTotal, valorEntrada, taxaJuros, quantidadePeriodos):
        amortizacoes = []
        jurosPeriodos = []
        saldosDevedoresPeriodo = []
        totalFinanciamento = valorTotal - valorEntrada
        saldoDevedor = totalFinanciamento
        print("*************************************************")
        print("******* FINANCIAMENTO IMOBILIÁRIO PRIECE ********")
        print("*************************************************\n")
        print("Valor do imovel: %d" % valorTotal)
        print("Valor de entrada: %d" % valorEntrada)
        print("Total Financiado: %d" % totalFinanciamento)
        print("Taxa de juros: %.3f" % taxaJuros+'%')
        print("Quantidade de periodos: %d" % quantidadePeriodos, '\n')

        parcela = parcelaPriece(totalFinanciamento, taxaJuros, quantidadePeriodos)

        #loop que percorre cada período
        for i in range(1, quantidadePeriodos + 1):
            #calculando o jurosAtual
            jurosAtual = saldoDevedor*taxaJuros
            jurosPeriodos.append(jurosAtual)

            #amortização
            amortizacaoAtual = parcela - jurosAtual
            amortizacoes.append(amortizacaoAtual)

            saldoDevedor = abs(saldoDevedor - amortizacaoAtual)
            print("Amortizacao: %d" % amortizacaoAtual," | Juros: %.2f" % jurosAtual, "| Parcela %d:" % i, "%.2f" % parcela, "| Saldo devedor: %.2f" % saldoDevedor)
        #salvando as informações numa tabela(array)
        tabelaPriece = [parcela, amortizacoes, jurosPeriodos, saldosDevedoresPeriodo]
        return tabelaPriece

def main():
    while True:
       print("Bem vindo ao nosso sistema de ficanciamento!")
       print("Escolha entre o financiamento SAC e o financiamento PRIECE:\n")
       print("Digite 1 para SAC e tecle ENTER")
       print("Digite 2 para PRIECE e tecle ENTER")
       print("Digite 3 para e tecle ENTER sair do sistema")

       opcaoEscolhida = input("Digite a opção escolhida: ")
       if opcaoEscolhida == '1':
            print("Você escolheu o ficanciamento SAC")
            print("Escolha os valores do financiamento:\n")
            valorTotal = float(input("Valor total do finaciamento: "))
            valorEntrada = float(input("Valor de entrada: "))
            juros = float(input("Juros (Exemplo: 0.01 para 1% ): "))
            parcela = int(input("Número de parcelas: "))
            print("")
            financiamentoSAC(valorTotal,valorEntrada, juros,parcela)
       elif opcaoEscolhida == '2':
            print("Você escolheu o fincanciamento PRIECE")
            print("Escolha os valores do financiamento:\n")
            valorTotal = float(input("Valor total do finaciamento: "))
            valorEntrada = float(input("Valor de entrada: "))
            juros = float(input("Juros (Exemplo: 0.01 para 1% ): "))
            parcela = int(input("Número de parcelas: "))
            print("")
            fincanciamentoPriece(valorTotal, valorEntrada, juros, parcela)
       elif opcaoEscolhida == '3':
           print('saindo....')
           sys.exit()
       else:
            print("Opção inválida, escolha novamente")
       print("\n")

main()
