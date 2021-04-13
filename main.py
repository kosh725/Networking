from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 80
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputData = f.read()
        success = 'HTTP/1.1 200 OK\n'
        connectionSocket.send(success.encode())
        for i in range(0, len(outputData)):
            connectionSocket.send(outputData[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        error = str('404 not found')
        print("Error occurred:" + str(IOError))
        connectionSocket.send(error.encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()
