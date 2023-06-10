import http.server
from urllib.parse import urlparse, parse_qs


class MyRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Analisar o caminho da URL e obter os parâmetros
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        if 'numero' in params:

            # Executar uma consulta
            numero = int(params['numero'][0])

            result = f"Numero recebido corretamente, voce enviou: {numero}"

            # Enviar a resposta ao cliente
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(result).encode())

        else:
            # Enviar uma resposta de erro se o parâmetro 'numero' estiver ausente
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Parâmetro "numero" ausente'.encode('utf-8'))


# Criar e iniciar o servidor HTTP
server_address = ('', 8000)
httpd = http.server.HTTPServer(server_address, MyRequestHandler)
print('Servidor iniciado na porta 8000...')
httpd.serve_forever()


"""'user': 'seu_usuario',
    'password': 'sua_senha',
    'host': 'localhost',
    'database': 'seu_banco_de_dados',"""
