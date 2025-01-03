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
            cotacao = ticker.history(period="1d")["Close"].iloc[-1]
            dividendYield = ticker.info['dividendYield']
            ativo.dy = dividendYield
            ativo.cotacao = round(cotacao, 2)
            ativo.save()
            print(f'ativo: {ativo.ativoPrincipal} preco: {ativo.cotacao}')
        except:
            pass
    return "Ativos atualizados com sucesso"
