from celery import shared_task
from .models import AtivosModels, PortfolioModels
import yfinance as yf



@shared_task()
def atualizar_ativos(bind=True):
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

