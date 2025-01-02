from celery import shared_task
import yfinance as yf
from .models import AtivosModels

@shared_task()
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
            ativo.cotacao = round(yf.download(
                f"{ativo.ativoPrincipal}.SA")["Close"].iloc[-1], 2)
            ativo.save()
            print(f'ativo: {ativo.ativoPrincipal} preco: {ativo.cotacao}')
        except:
            pass
    return "Ativos atualizados com sucesso"
