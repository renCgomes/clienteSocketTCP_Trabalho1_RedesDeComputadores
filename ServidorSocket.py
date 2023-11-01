import socket
import threading
import time

PORTA = 18000 # Porta do servidor
SERVER = '127.0.0.1' # Endereço IP do servidor
ADDR = (SERVER, PORTA) # Tupla com as informações de endereço e porta para conectar o servidor  
HEADER = 64 # Cabeçalho com número de bytes que a mensagem possui
FORMAT = 'utf-8' # formatação da mensagem 
DISCONNECT = ':D' #Brincadeirinha


# Define AF_INET como IPV4 e SOCK_STREAM co

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(ADDR) # Vinculando o servidor a porta e ao endereço

# Lista para armazenar todas as conexões
conexoes = [] #

def handler(cliente, addr):
    
    try:
        print(f'[NOVA CONEXÃO]: {addr} se conectou!') # mensagem de que algum cliente se conectou

        conectado = True 
        # Adiciona a nova conexão à lista
        conexoes.append(cliente)
        
        while conectado: #Enquanto estiver conectado...
        # Adiciona a nova conexão à lista
        #Decodifica a conexoes.append(co nn)
        
        # while conectado:
            msg_length = cliente.recv(HEADER).decode(FORMAT)
            
            if msg_length:
                
                msg_length = int(msg_length) #Convertendo o tamanho da mensagem para int
                msg = cliente.recv(msg_length).decode(FORMAT) # Decodifica a mensagem no header
                
                if msg == DISCONNECT: 
                    
                    conectado = False
                    print(f"Desconctando: {addr}") 
                    
                    continue

                print(f'[{time.ctime()}][{addr}]: {msg}') #Printa o horário da mensagem antes da mensagem
                
                # Envia a mensagem para todos os clientes
                for conexao in conexoes:
                    
                    conexao.send(f'[{time.ctime()}][{addr}]: {msg}'.encode(FORMAT))

    except Exception as e:

        print(f"Erro: {e}")

    finally:

        # Remove a conexão da lista após desconectar
        if cliente in conexoes:
            conexoes.remove(cliente)
        cliente.close()


def start():
    server.listen()
    print(f'O servidor está no endereço {SERVER}')
    
    while True:
        cliente, addr = server.accept()
        thread = threading.Thread(target=handler, args=(cliente, addr))
        thread.start()
        print(f'Conexões ativas: {threading.active_count() - 1}')

print('Iniciando o servidor ...')
print('--------------------------')
start()