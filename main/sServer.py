import socket, threading

class sServer():
    _mainSocket = None
    _port = 8096
    _localAdd = '127.0.0.1'
    _connected = []

    def __init__(self):
        if self._mainSocket is None:
            #Creating socket using ipv4 and TCP
            self._mainSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ## This is added for the future upgrade to multithreaded server
            self._mainSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            ##Binding the server to be the main reciever of requests
            self._mainSocket.bind((self._localAdd,self._port))
        ## Server socket has been initilized there for we begin looping for requests
        self._mainSocket.listen()
        while True:
            clientSock, clientAdd = self._mainSocket.accept()
            x = asyncClient(clientSock,clientAdd)
            self._connected.append(x)
            x.start()

    def close(self):
        self._mainSocket.close()

##MULTI THREADED Communication line to client
class asyncClient(threading.Thread, sServer):
    _clientAdd = None
    _previousRes = None #This is used to keep previous responses, to reduce data sent between server and client
    def __init__(self, socket, clintAdd):
        threading.Thread.__init__(self)
        self._mainSocket = socket
        self._clientAdd = clintAdd

    def run(self):
        print("Client : "+str(self._clientAdd)+" has connected, Thread_ID: "+str(threading.get_ident()))
        receivedMsg = self._mainSocket.recv(2048)
        actualMsg = receivedMsg.decode('utf-8')
        if actualMsg.casefold() == 'hi':
            self._previousRes = actualMsg.casefold()
        self._mainSocket.sendall(bytes("Hi Received",'utf-8'))



def main():
    sSocket = sServer()
    sSocket.close()


if __name__ == '__main__':
    main()