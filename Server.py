import socket
import time

print("Сервер запущен")
time.sleep(0.5)
print("Поиск соединения...")

srv = socket.socket()
srv.bind(('', 9090))
srv.listen(1)
conn, addr = srv.accept()

print('connected:', addr)

while True:
    data_rcv = conn.recv(1024).decode('utf-8')
    if data_rcv == "Client closed connection":
        print("Клиент разорвал соединие...")
        conn.close()
        break
    else:
        print("Клиент:", data_rcv)
    if not data_rcv:
        break
    data_snd = input("Вы: ").encode('utf-8')
    if data_snd.decode('utf-8') == "конец":
        conn.send("Server closed connection".encode('utf-8'))
        conn.close()
        break
    else:
        conn.send(data_snd)

conn.close()
