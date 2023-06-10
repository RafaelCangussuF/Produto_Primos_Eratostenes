import http.server
import mysql.connector
from urllib.parse import urlparse, parse_qs

# Configurações do banco de dados
db_config = {
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'host': 'localhost',
    'database': 'seu_banco_de_dados',
}


# Classe para manipular as requisições HTTP
class MyRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Analisar o caminho da URL e obter os parâmetros
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        if 'numero' in params:
            # Conectar ao banco de dados MySQL
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Executar uma consulta
            numero = int(params['numero'][0])
            query = "SELECT Pi,Pj FROM tabela_primos WHERE Produto = %s"
            cursor.execute(query, (numero,))

            # Obter o resultado da consulta
            result = cursor.fetchall()

            # Enviar a resposta ao cliente
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(result).encode())

            # Fechar a conexão com o banco de dados
            cursor.close()
            connection.close()
        else:
            # Enviar uma resposta de erro se o parâmetro 'numero' estiver ausente
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Parametro "numero" ausente'.encode('utf-8'))


# Criar e iniciar o servidor HTTP
server_address = ('', 8000)
httpd = http.server.HTTPServer(server_address, MyRequestHandler)
print('Servidor iniciado na porta 8000...')
httpd.serve_forever()

