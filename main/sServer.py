import socket, threading
from IndState import IndState as iD
from main.Library import Library

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
    _state = iD.LOGIN #All connected clients are in login mode
    def __init__(self, socket, clintAdd):
        threading.Thread.__init__(self)
        self._mainSocket = socket
        self._clientAdd = clintAdd

    def run(self):
        print("Client : "+str(self._clientAdd)+" has connected, Thread_ID: "+str(threading.get_ident()))
        mToS = None # Messageto be sent to the client
        while mToS != iD.TERMINATE_CONN:
            receivedMsg = self._mainSocket.recv(2048)
            dataReceived = iD.breakData(receivedMsg.decode('utf-8')) ##Server/Client always commun
            if dataReceived[0].casefold() == str(iD.TERMINATE_CONN):
                mToS = iD.TERMINATE_CONN
                self._mainSocket.sendall(bytes(dataReceived[0],'utf-8'))
                self._mainSocket.close()
                break
            if self._state == iD.LOGIN: ## Check
                #TODO
                checking = Library().userLogin(dataReceived)
                if checking == iD.INCORRECT_INPUT: ##Inputted incorrect we cant just pass this without checking
                    mToS = str(iD.INCORRECT_INPUT)
                else:
                    self._state = checking
                    if self._state == iD.A_MENU:
                        mToS = str(checking)+','+str("Welcome to Admin menu")
                    elif self._state == iD.S_MENU:
                        mToS = str(checking)+','+str("Welcome to Admin menu")
                    elif self._state == iD.P_MENU:
                        mToS = str(checking)+','+str("Welcome to Admin menu")


            self._mainSocket.sendall(bytes(mToS,'utf-8'))
        print("Client : "+str(self._clientAdd)+" closing com, Thread_ID: "+str(threading.get_ident()))
        self._mainSocket.close()



def main():
    sSocket = sServer()
    sSocket.close()


if __name__ == '__main__':
    main()