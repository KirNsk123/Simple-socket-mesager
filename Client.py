import socket
import time

running = True
connected = False
start_time = time.time()

def send_data():
    data_snd = input("Вы: ")
    if data_snd == "конец":
        clt.send("Client closed connection".encode('utf-8'))
        clt.close()
        return 1
    else:
        return data_snd.encode('utf-8')

def receive_data():
    data_rcv = clt.recv(1024).decode('utf-8')
    if data_rcv == "Server closed connection":
        print("Сервер разрвал соединение...")
        clt.close()
        return 1
    elif not data_rcv:
        return 1
    else:
        return f"Сервер: {data_rcv}"

def main():
    global running
    data_snd = send_data()
    if data_snd == 1:
        running = False
        return "stop"
    else:
        clt.send(data_snd)
    data_rcv = receive_data()
    if data_rcv == 1:
        running = False
        return "stop"
    else:
        print(data_rcv)


clt = socket.socket()
clt.connect(('localhost', 9090))


while running:
    main()
    if not running:
        break

clt.close()
