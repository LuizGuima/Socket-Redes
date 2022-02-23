import socket
import threading
import time

PORT = 5050
FORMATO = 'utf-8'
SERVER = "localhost"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(mensagem):
    client.send(mensagem.encode(FORMATO))

def sendMsg():
    mensagem = input()
    send("msg=" + mensagem)

def sendName():
    nome = input('Digite seu nome: ')
    send("nome=" + nome)

def handle_msgs():
    while(True):
        msg = client.recv(1024).decode()
        mensagem_splitada = msg.split("=")
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2])

def startShipping():
    sendName()
    sendMsg()

def iniciar():
    thread1 = threading.Thread(target=handle_msgs)
    thread2 = threading.Thread(target=startShipping)
    thread1.start()
    thread2.start()

iniciar()