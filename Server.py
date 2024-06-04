import socket
import time

running = True

def receive_data():
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
    data_snd = input("Вы: ")
    if data_snd == "конец":
        conn.send("Server closed connection".encode('utf-8'))
        conn.close()
        return 1
    else:
        return data_snd.encode('utf-8')

def main():
    global running
    data_rcv = receive_data()
    if data_rcv == 1:
        running = False
        return "stop"
    else:
        print(data_rcv)
    data_snd = send_data()
    if data_snd == 1:
        running = False
        return "stop"
    else:
        conn.send(data_snd)


print("Сервер запущен")
time.sleep(0.5)
print("Поиск соединения...")

srv = socket.socket()
srv.bind(('', 9090))
srv.listen(1)
conn, addr = srv.accept()

print('Соединение найдено!', addr)

while running:
    main()
    if not running:
        break

conn.close()
