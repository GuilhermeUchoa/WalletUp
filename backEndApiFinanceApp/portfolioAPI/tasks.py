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

        try: #AVALIAR SE ESSE TRY É UTIL

            if ativo.tipo != 'Tesouro Direto':

                ticker = yf.Ticker(f"{ativo.ativoPrincipal}.SA")

                atributos = {
                    "longBusinessSummary":"ativo.longBusinessSummary",
                    "dividendYield":"ativo.dy",
                    "trailingPE":"ativo.pl",
                    "enterpriseValue":"ativo.enterpriseValue",
                    "freeCashflow":"ativo.freeCashflow",
                    "revenueGrowth":"ativo.revenueGrowth",
                    "debtToEquity":"ativo.debtToEquity",
                    "earningsQuarterlyGrowth":"ativo.earningsQuarterlyGrowth",
                    "twoHundredDayAverage":"ativo.twoHundredDayAverage",
                    "fiftyTwoWeekLow":"ativo.fiftyTwoWeekLow",
                    "fiftyTwoWeekHigh":"ativo.fiftyTwoWeekHigh"
                }

                for key, atributo in atributos.items():

                    try:
                        valor = ticker.info.get(key)
                        if valor is not None:
                            setattr(ativo, key, valor)
                            # exec(f'{atributo} = {valor}') # exec() é uma forma de fazer atribuicao com dicionario
                        else:
                            print(f'{key}: Dado nao encontrado: {ativo.ativoPrincipal}')
                    except:
                        print(f'{ativo.tipo}: Dado nao existente: {ativo.ativoPrincipal} key:{key}')


                #Forma de atribuir a cotação separado das informações, pois o mais importante é a cotacao
                ativo.cotacao = round(ticker.history(period="1d")["Close"].iloc[-1], 2)
                ativo.save()
                print(f'ativo: {ativo.ativoPrincipal} preco: {ativo.cotacao} salvo.')

            else:
                print(f'Não há suporte para {ativo.tipo}: {ativo.ativoPrincipal} no momento.')

            
        except:
            print(f'Erro ao baixar informacoes do ativo: {ativo.ativoPrincipal}')
    
    return "Ativos atualizados com sucesso"
