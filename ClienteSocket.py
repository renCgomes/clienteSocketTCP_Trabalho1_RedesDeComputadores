import socket
import threading

PORTA = 18000 # Porta do servidor
#ENDERECO = '10.20.30.8' # Endereço IP do servido
ENDERECO = '127.0.0.1' 
CONFIG = (ENDERECO, PORTA) # Tupla com as informações de endereço e porta para conectar o servidor  
HEADER = 64 # Cabeçalho com número de bytes que a mensagem possui
FORMATO = 'utf-8' # formatação da mensagem 
DISCONNECT = ':D' #Brincadeirinha


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(CONFIG)

def receberMensagem():
    
    while True:
   
        try:
    
            mensagem = cliente.recv(HEADER).decode(FORMATO)
            
            print(mensagem)
            
        except:
            
            # Fecha a conexão caso ocorra um erro
            print("An error occured!")
            cliente.close() # Fecha o cliente
            
            break


def enviarMensagem():

    while True:

        mensagem = '{}'.format(input(''))
        tamanhoMensagem = str(len(mensagem))

        cliente.send(tamanhoMensagem.encode(FORMATO))
        cliente.send(mensagem.encode(FORMATO))

''' 
Comecando as duas threads, uma para recbimento de mensagens
do servidor e outra para envio de mensagens do cliente para
o servidor 
'''
receive_thread = threading.Thread(target=receberMensagem)
receive_thread.start()

write_thread = threading.Thread(target=enviarMensagem)
write_thread.start()

