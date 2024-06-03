import socket
import time

def recive_data():
    data_rcv = conn.recv(1024).decode('utf-8')
    if data_rcv == "Client closed connection":
        print("Клиент разорвал соединие...")
        conn.close()
        return 1
    elif not data_rcv:
        return 1
    else:
        return f"Клиент: {data_rcv}"

def send_data():
    data_snd = input("Вы: ").encode('utf-8')
    if data_snd.decode('utf-8') == "конец":
        conn.send("Server closed connection".encode('utf-8'))
        conn.close()
        return 1
    else:
        return data_snd


print("Сервер запущен")
time.sleep(0.5)
print("Поиск соединения...")

srv = socket.socket()
srv.bind(('', 9090))
srv.listen(1)
conn, addr = srv.accept()

print('Соединение найдено!', addr)

while True:
#    data_rcv = conn.recv(1024).decode('utf-8')
#    if data_rcv == "Client closed connection":
#        print("Клиент разорвал соединие...")
#        conn.close()
#        break
#    else:
#        print("Клиент:", data_rcv)
#    if not data_rcv:
#        break
    data_rcv = recive_data()
    print(data_rcv)
#    data_snd = input("Вы: ").encode('utf-8')
#    if data_snd.decode('utf-8') == "конец":
#        conn.send("Server closed connection".encode('utf-8'))
#        conn.close()
#        break
#    else:
#        conn.send(data_snd)
    data_snd = send_data()
    conn.send(data_snd)

conn.close()
