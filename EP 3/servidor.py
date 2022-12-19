import socket

# o ip determinado abaixo é o IPv4 padrão
ip = "127.0.0.1"
# a porta pode ser qualquer inteiro entre 1 e 65535
port = 65432

# criando e fechando um objeto socket, que representará o servidor
# passa-se como argumentos:
#   socket.AF_INET, que especifica o uso do IPv4
#   socket.SOCK_STREAM, que especifica o uso do TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # associando o socket criado com o endreço IP e a porta
    s.bind((ip, port))
    # liberando o socket para aceitar conexões
    s.listen()
    # pausando momentaneamente a execução para esperar uma conexão
    # quando conecta, o método retorna:
    #   um novo socket, representando o servidor na conexão com o novo cliente
    #   uma tupla, armazenando o endereço dessa nova conexão, no formato (host, port) no caso do IPv4
    conexao, endereco = s.accept()
    with conexao:
        print(f"Conectado pelo {endereco}")
        # o servidor irá receber pacotes de dados do cliente (de no máximo 1024 bytes) e repassa-los até que "conn.recv()" retorne um ponteiro nulo, o que significa o fim da conexão
        while True:
            dados = conexao.recv(1024)
            if not dados:
                break
            conexao.sendall(dados)