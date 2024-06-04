import socket

clt = socket.socket()
clt.connect(('localhost', 9090))
while True:
    data_snd = input("Вы: ").encode('utf-8')
    if data_snd.decode('utf-8') == "конец":
        clt.send("Client closed connection".encode('utf-8'))
        clt.close()
        break
    else:
        clt.send(data_snd)
    data_rcv = clt.recv(1024)
    if data_rcv.decode('utf-8') == "Server closed connection":
        print("Сервер разорвал соединие...")
        clt.close()
        break
    else:
        print("Сервер:", data_rcv.decode('utf-8'))
    if not data_rcv:
        break

clt.close()
