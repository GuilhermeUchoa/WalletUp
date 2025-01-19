from django.http import JsonResponse
from .models import AtivosModels, PortfolioModels
import pandas as pd


def adicionarAtivosDaCarteiraB3ParaPortfolioAppUsuario(request, file):
    xls = pd.ExcelFile(file)
    dictAtivo = {}
    listaCarteiraDF = []

    # Esse for faz leitura de todas as abas da planilha
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet_name).dropna()
        dictAtivo[sheet_name] = df

    mensagens = []  # Lista para armazenar as mensagens

    for chave, valor in dictAtivo.items():
        for i in range(len(valor)):
            # A intenção aqui é apenas definir o nome do ativo.
            if chave == 'Tesouro Direto':  # Se for Tesouro Direto o nome do ativo fica na coluna 'Produto'
                ativo = valor['Produto'].loc[i]
            else:
                ativo = valor['Código de Negociação'].loc[i]  # Se for outro ativo o nome do ativo fica na coluna 'Código de Negociação'

            # Add para lista de carteiras que tem no DataFrame para depois excluir ativos que não tem mais na carteira da B3
            listaCarteiraDF.append(ativo)

            try:  # Se for localizado o ativo na carteira do cliente, apenas atualiza a quantidade
                if PortfolioModels.objects.filter(ativo__ativoPrincipal=ativo, usuario=request.user).exists():
                    # Buscar a instância do AtivosModels associada ao ativo
                    ativo_obj = AtivosModels.objects.get(ativoPrincipal=ativo)
                    
                    # Atualizando a carteira se o ativo já existir
                    carteira = PortfolioModels.objects.get(ativo=ativo_obj, usuario=request.user)
                    carteira.quantidade = valor['Quantidade'].loc[i]
                    
                    if chave == 'Tesouro Direto':  # Atualizando cotação para Tesouro Direto
                        carteira.ativo.cotacao = float(valor['Valor Atualizado'].loc[i] / valor['Quantidade'].loc[i])
                    
                    carteira.save()
                    mensagens.append(f'Ativo {ativo} atualizado')

                else:  # Se o ativo não existir na carteira do usuário, criar um novo
                    # Buscar o ativo na carteira principal
                    carteiraPrincipal = AtivosModels.objects.get(ativoPrincipal=ativo)
                    
                    # Criar o novo ativo na carteira do usuário
                    carteiraUsuario = PortfolioModels.objects.create(
                        ativo=carteiraPrincipal,  # Atribui a instância do AtivosModels
                        quantidade=float(valor['Quantidade'].loc[i]),
                        cotacao=float(valor['Valor Atualizado'].loc[i] / valor['Quantidade'].loc[i]) if chave == 'Tesouro Direto' else None,
                        usuario=request.user
                    )
                    mensagens.append(f'Novo ativo {ativo} adicionado à carteira do usuário')

            except Exception as e:  # Se o ativo não for encontrado, cria um novo ativo na carteira do usuário
                if chave == 'Tesouro Direto':
                    # Criar o ativo na carteira principal se não existir
                    carteiraPrincipal = AtivosModels(
                        ativoPrincipal=ativo,
                        cotacao=float(valor['Valor Atualizado'].loc[i] / valor['Quantidade'].loc[i]),
                        tipo=chave
                    )
                    carteiraPrincipal.save()

                    # Criar o ativo na carteira do usuário
                    carteiraUsuario = PortfolioModels(
                        ativo=carteiraPrincipal,  # Atribui a instância do AtivosModels
                        cotacao=float(valor['Valor Atualizado'].loc[i] / valor['Quantidade'].loc[i]),
                        quantidade=valor['Quantidade'].loc[i],
                        usuario=request.user
                    )
                    carteiraUsuario.save()

                elif chave != 'Tesouro Direto':
                    # Criar o ativo na carteira principal se não existir
                    carteiraPrincipal = AtivosModels(
                        ativoPrincipal=ativo,
                        tipo=chave
                    )
                    carteiraPrincipal.save()

                    # Criar o ativo na carteira do usuário
                    carteiraUsuario = PortfolioModels(
                        ativo=carteiraPrincipal,  # Atribui a instância do AtivosModels
                        quantidade=valor['Quantidade'].loc[i],
                        usuario=request.user
                    )
                    carteiraUsuario.save()

                mensagens.append(f'Novo ativo {ativo} adicionado à carteira')

    # Compara a carteira da B3 com a do APP, se tiver algo a mais na carteira do APP significa que me desfiz do ativo na corretora e então ele exclui o ativo da carteira do app
    listaCarteiraBD = [i.ativo.ativoPrincipal for i in PortfolioModels.objects.filter(usuario=request.user)]
    listaDeExclusao = list(set(listaCarteiraBD).difference(set(listaCarteiraDF)))
    
    for ativo in listaDeExclusao:
        # Excluir o ativo da carteira do usuário
        PortfolioModels.objects.filter(ativo__ativoPrincipal=ativo, usuario=request.user).delete()
        mensagens.append(f'Ativo {ativo} foi excluído da carteira')

    return JsonResponse({'messages': mensagens})