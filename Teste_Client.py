import requests

# Número a ser enviado
numero = 143

# URL do servidor e parâmetros da solicitação
url = 'http://localhost:8000'  # substitua pelo URL correto do servidor
params = {'numero': numero}

# Envio da solicitação GET
response = requests.get(url, params=params)

# Verificação da resposta do servidor
if response.status_code == 200:
    # A solicitação foi bem-sucedida
    print('Resposta do servidor:', response.text)
else:
    # O servidor retornou um código de status de erro
    print('Erro na solicitação:', response.status_code)
