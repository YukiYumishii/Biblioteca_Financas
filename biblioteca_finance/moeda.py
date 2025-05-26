import requests

def converter_moeda(valor, moeda_origem, moeda_final):
    if valor <= 0:
        return 'O valor a ser convertido deve ser maior que zero.'
    
    else:
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_final}"
        r = requests.get(url).json()
        taxa = float(r[f'{moeda_origem}{moeda_final}']['bid'])
        return valor * taxa