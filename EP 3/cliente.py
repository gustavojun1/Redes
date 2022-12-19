import socket

# informações DO SERVIDOR (e não do cliente)
ip = "127.0.0.1"
porta = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # conectando com o servidor
    s.connect((ip, porta))
    # enviando dados para o servidor
    s.sendall(b"Hello World")
    # recebendo e imprimindo a resposta do servidor
    resposta = s.recv(1024)
    print(f"Recebido {resposta!r}")