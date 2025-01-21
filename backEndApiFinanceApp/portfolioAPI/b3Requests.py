import requests
import base64
from . models import AtivosModels
from datetime import datetime

def b3BalancosContabeisParaAcoesCrawler(ativoStock: str):
    ''' 
    
    Coloca o codigo do ativo que lhe interessa e retorna:
    
    dataInicial, dataFinal, balancoPatrimonial, demonstracaoDoResultadoExercicio,
    fluxoDeCaixa, freeFloat,shareholders, capitalStockComposition 
    
    Como usar:

    di, df, bp, dre, fc, ff, sh, csc = b3BalancosContabeisParaAcoesCrawler(ativo)

    '''

    cookies = {
        'OptanonAlertBoxClosed': '2025-01-17T23:10:14.293Z',
        '_gcl_au': '1.1.714280146.1737155437',
        '_gid': 'GA1.3.508604040.1737155437',
        '_tt_enable_cookie': '1',
        '_ttp': 'BDJGbTSYYqdm7jdfbqitp3k8xtT.tt.2',
        '_ga_5E2DT9ZLVR': 'GS1.1.1737200305.1.1.1737200331.34.0.0',
        'dtCookie': 'v_4_srv_33_sn_15BDB07D8FAC02EBBFF16040AFD775DB_perc_100000_ol_0_mul_1_app-3Afd69ce40c52bd20e_1_rcs-3Acss_0',
        'TS01871345': '016e3b076f14128a42392ecbef9506bb1a7471e4af4fb13d2c35e6808fa01b385517be149a2a70f91b24473e325e6092548a6e1003',
        'TS0134a800': '016e3b076f14128a42392ecbef9506bb1a7471e4af4fb13d2c35e6808fa01b385517be149a2a70f91b24473e325e6092548a6e1003',
        '__cf_bm': 'twxFItfWLHMxtffhDRHWicHV4tjlq4SosSHmyQ1K.O0-1737251813-1.0.1.1-lM0OiCdoh2mU5xIEJlEYL_qIqcJxe8fZUrXWD.ic.e6dzONcawkwXKQTju.Djqz2VSPkvZwc9EWoVo.lzImvaw',
        'BIGipServerpool_sistemaswebb3-listados_8443_WAF': '1329140746.64288.0000',
        'rxVisitor': '17372519102867UN0FLHBF6A1HVL9GFEGDC7EV8DQUOMF',
        'cf_clearance': '9.alNrkFrBnz3FxxGyVTjS5kplFGX0g5Dw5CDwW6gvY-1737251914-1.2.1.1-lwDcZLu_Qsbw6yh8nF7GywkhhyHcfVsQ9bqfKA5bvgtbhLJcBTV6.lXt8HRKlv4ao5.cYcIB.PXKukIjtLr3PgA27j5SlnObEIxTyLNFNKGKpNmxwkUhGtmVK7OrHbpKnd0DhORB_pGrwjvOMUVRKpKZMxwdQuN8jNTAxvKqplQgCGO1ttJFbtdiDvv1pyhCm23EaZubScnm7SsyiKZpHvlc8sUiKsH2A1AbKdeopibUUW0DbA_.YrybQpP9xv9YZ0TU1YhjBLwLbLc6P7C1la4mCUIL3cEy8L1XUNon9vM',
        '_clck': '12mjrd2%7C2%7Cfsp%7C0%7C1843',
        '_ga_FTT9L7SR7B': 'GS1.1.1737251914.3.0.1737251922.52.0.0',
        'TS0171d45d': '011d592ce1f587cd69926ecbdc8fbce204c1ac1542067321d20611e5029df2068eb8cf9abb628295b0f5195bca4ff1d1408305187c',
        '_gat_UA-94042116-2': '1',
        'dtSa': '-',
        '_ga_SS7FXRTPP3': 'GS1.1.1737251923.5.1.1737251932.51.0.0',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Jan+18+2025+22%3A58%3A53+GMT-0300+(Hor%C3%A1rio+Padr%C3%A3o+de+Bras%C3%ADlia)&version=6.21.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0003%3A1%2CC0001%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=%3B&AwaitingReconsent=false',
        '_gat_gtag_UA_94042116_5': '1',
        '_ga_CNJN5WQC5G': 'GS1.1.1737251933.4.0.1737251933.60.0.0',
        '_ga': 'GA1.1.1940968619.1737155361',
        '_clsk': '1hr9bh7%7C1737251933746%7C4%7C1%7Cn.clarity.ms%2Fcollect',
        'rxvt': '1737253741606|1737251910288',
        'dtPC': '33$251932674_539h14vMVKCCFVKOCKWAJBUSBAMQKVKFMCULKUH-0e0',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookies': 'OptanonAlertBoxClosed=2025-01-17T23:10:14.293Z; _gcl_au=1.1.714280146.1737155437; _gid=GA1.3.508604040.1737155437; _clck=12mjrd2%7C2%7Cfso%7C0%7C1843; dtCookie=v_4_srv_24_sn_BB46C80902D2C129AFCFB42F6D1D9748_perc_100000_ol_0_mul_1_app-3Afd69ce40c52bd20e_0_rcs-3Acss_0; cf_clearance=jOa_NrB8pZ3pQMoTQTM9aFgzh2u2n_R93b3mD.mFnsE-1737200201-1.2.1.1-1jIRjE_WUWM6kaK2Bzjjgh7YgrjzZjGTJsMxhuP4UQjRWkVPkD0tvf3huQhz3M6xpjF2LGD7vm50fAJGd6fHOwB.a0E6VeTM2WUIi.LodJxY1o35p4u3nLKDrizADSOBa7vFlR0WfeViY7YclijI9lCx8N19nsg3k1Yuj6Nbn5sOQFftwO99XCwN6SQAfx8Fj32bnAu2SSkBATGeVMbFRYMm7KnIxkYo6E3.DO4HqxDPG5eNMcym81kM2kfH.87sY1_bcAA.pLhW1.XEBtXcxOOcn2RnXDrDZJYt47uBu3Y; __gtm_referrer=https%3A%2F%2Fwww.google.com%2F; _tt_enable_cookie=1; _ttp=BDJGbTSYYqdm7jdfbqitp3k8xtT.tt.2; _ga_5E2DT9ZLVR=GS1.1.1737200305.1.1.1737200331.34.0.0; __cf_bm=Opj3qFlSP5NvmZLmXTqO01ZBxAfv87G.MF5t1.fO2mw-1737200371-1.0.1.1-6YsDckzY.2iRmP9LcivIJRljYv8lWb49B8eXUpZFpCnJrudcnkIgahH6hn2BDBkpykhv0_ccpaNi2ty7w4160g; TS0171d45d=011d592ce1b74392ba056e2b614cfa0e70381835f2b0b14d00eee7a928d02e8f8192338047f6291c3c19574a9ed5fe338778970ed7; TS01871345=016e3b076fbc5328e45d5f42c493ad61da27b52b1f2e992d35ba87f720afb8bc5e55ff9adc8ffbc370da0a6b2dab923615737cfaeb; _ga_FTT9L7SR7B=GS1.1.1737199448.2.1.1737200671.32.0.0; _ga_SS7FXRTPP3=GS1.1.1737199462.4.1.1737200809.60.0.0; _gat_UA-94042116-2=1; BIGipServerpool_sistemaswebb3-listados_8443_WAF=1329145866.64288.0000; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Jan+18+2025+08%3A46%3A50+GMT-0300+(Hor%C3%A1rio+Padr%C3%A3o+de+Bras%C3%ADlia)&version=6.21.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0003%3A1%2CC0001%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=%3B&AwaitingReconsent=false; _ga_CNJN5WQC5G=GS1.1.1737199711.3.1.1737200810.59.0.0; _ga=GA1.3.1940968619.1737155361; _gat_gtag_UA_94042116_5=1',
        'priority': 'u=1, i',
        'referer': 'https://sistemaswebb3-listados.b3.com.br/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-dtpc': '24$200809804_61h13vURKCNMFAQLQQPPPKFKPCVARJKLOFQPVQ-0e0',
        'x-dtreferer': 'https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/?language=pt-br',
    }

    # Selecionar o Ativo e pegando seu codCVM
    ativo = ativoStock

    paramsToCod = {"language": "pt-br", "pageNumber": 1,
                   "pageSize": 20, "company": f"{ativo}"}

    # Os dados estao codados em BASE64
    paramsDecodeToCod = base64.b64encode(
        str(paramsToCod).encode('ASCII')).decode('UTF-8')

    cod = requests.get(
        f'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetInitialCompanies/{paramsDecodeToCod}',
        cookies=cookies,
        headers=headers,
    )

    # Pegando dados
    params = {
        "codeCVM": f"{cod.json()['results'][0]['codeCVM']}", "language": "pt-br"}

    # Os dados estao codados em BASE64
    paramsEncode = base64.b64encode(
        str(params).encode('ASCII')).decode('utf-8')

    response = requests.get(
        f'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetListedFinancial/{paramsEncode}',
        cookies=cookies,
        headers=headers,
    )

    # DataInicial e DataFinal
    dataInicial =  datetime.strptime(response.json()['consolidated'][0]['dateInicial'],'%d/%m/%Y')
    dataFinal = datetime.strptime(response.json()['consolidated'][0]['dateFinal'], '%d/%m/%Y') 

    # Balanço Patrimonial - Consolidado, Value2 é o mais recente e Value1 o mais antigo
    balancoPatrimonial = response.json()['consolidated'][0]['results']
    for item in balancoPatrimonial:
        item['value'] = item['value'].replace('-','').replace('.', '').replace(',', '.').replace('(','-').replace(')','')
        item['value2'] = item['value2'].replace('-','').replace('.', '').replace(',', '.').replace('(','-').replace(')','')

    # Demonstração do Resultado - Consolidado
    demonstracaoDoResultadoExercicio = response.json()['consolidated'][1]['results']
    for item in demonstracaoDoResultadoExercicio:
        item['value'] = item['value'].replace('-','').replace('.', '').replace(',', '.').replace('(','-').replace(')','')
        item['value2'] = item['value2'].replace('-','').replace('.', '').replace(',', '.').replace('(','-').replace(')','')

    # Demonstração do Fluxo de Caixa - Consolidado
    fluxoDeCaixa = response.json()['consolidated'][2]['results']
    for item in fluxoDeCaixa:
        item['value'] = item['value'].replace('-','').replace('.', '').replace(',', '.').replace('(','-').replace(')','')
        item['value2'] = item['value2'].replace('-','').replace('.', '').replace(',', '.').replace('(','-').replace(')','')

    # freeFloatResult
    freeFloat = response.json()['freeFloatResult']['results']
    for item in freeFloat:
        item['value'] = item['value'].replace('-','').replace('.', '').replace(',', '.').replace('(','-').replace(')','')
        item['value2'] = item['value2'].replace('-','').replace('.', '').replace(',', '.').replace('(','-').replace(')','')

    # positionShareholders
    shareholders = response.json()['positionShareholders']['results']
    for item in shareholders:
        item['on'] = item['on'].replace('-','').replace('.', '').replace(',', '.').replace('(','-').replace(')','')
        item['pn'] = item['pn'].replace('-','').replace('.', '').replace(',', '.').replace('(','-').replace(')','')
        item['total'] = item['total'].replace('-','').replace('.', '').replace(',', '.').replace('(','-').replace(')','')

    # capitalStockComposition
    capitalStockComposition = response.json()['capitalStockComposition']['results']
    for item in capitalStockComposition:
        item['value'] = float(item['value'].replace('.', '').replace(',', '.').replace('(','-').replace(')',''))
  
    

    return dataInicial, dataFinal, balancoPatrimonial, demonstracaoDoResultadoExercicio, fluxoDeCaixa, freeFloat, shareholders, capitalStockComposition



ativos = AtivosModels.objects.filter(tipo='Acoes')

for ativo in ativos:

    
    dataInicial, dataFinal, balancoPatrimonial, demonstracaoDoResultadoExercicio, fluxoDeCaixa, freeFloat, shareholders, capitalStockComposition = b3BalancosContabeisParaAcoesCrawler(ativo)

    ativo.dataInicial = dataInicial
    ativo.dataFinal = dataFinal
    ativo.balancoPatrimonial = balancoPatrimonial
    ativo.demonstracaoDoResultadoDoExercicio = demonstracaoDoResultadoExercicio
    ativo.demonstracaoDoFluxoDeCaixa = fluxoDeCaixa
    ativo.freeFloatResult = freeFloat
    ativo.positionShareholders = shareholders
    ativo.capitalStockComposition = capitalStockComposition

    ativo.save()