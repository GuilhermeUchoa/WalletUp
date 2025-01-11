from celery import shared_task
import yfinance as yf
from .models import AtivosModels


@shared_task
def atualizar_ativos():
    """
    Atualiza os pre os dos ativos cadastrados no banco de dados

    Percorre todos os ativos cadastrados no banco de dados, atualiza a cota o
    de cada um com base nos dados da Yahoo! Finance e salva no banco de dados
    novamente.

    :return: uma string com a mensagem de sucesso
    """

    ativos = AtivosModels.objects.all()
    for ativo in ativos:
        try:

            ticker = yf.Ticker(f"{ativo.ativoPrincipal}.SA")

            ativo.cotacao = round(ticker.history(period="1d")["Close"].iloc[-1], 2)
            ativo.longBusinessSummary = ticker.info['longBusinessSummary']
            ativo.dy = ticker.info['dividendYield']
            ativo.pl = ticker.info['trailingPE']
            ativo.enterpriseValue = ticker.info['enterpriseValue']
            ativo.freeCashflow = ticker.info['freeCashflow']
            ativo.revenueGrowth = ticker.info['revenueGrowth']
            ativo.debtToEquity = ticker.info['debtToEquity']
            ativo.earningsQuarterlyGrowth = ticker.info['earningsQuarterlyGrowth']
            ativo.twoHundredDayAverage = ticker.info['twoHundredDayAverage']
            ativo.fiftyTwoWeekLow = ticker.info['fiftyTwoWeekLow']
            ativo.fiftyTwoWeekHigh = ticker.info['fiftyTwoWeekHigh']

            ativo.save()
   
            print(f'ativo: {ativo.ativoPrincipal} preco: {ativo.cotacao}')
            
        except:
            print(f'Erro ao baixar ativo: {ativo.ativoPrincipal}')
    return "Ativos atualizados com sucesso"
