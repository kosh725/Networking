from socket import *
#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 80 #Assigning port number
serverSocket.bind(('', serverPort)) #Binding the address of server to the port no.
serverSocket.listen(1) #Only listen to one connection at a time

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Creating new connection from client
    try:
        message = connectionSocket.recv(1024).decode() #Receives message from client
        filename = message.split()[1]
        f = open(filename[1:])
        outputData = f.read() #Read the file and store temporarily
        #Send one HTTP header line into socket
        success = 'HTTP/1.1 200 OK\n'
        connectionSocket.send(success.encode())
        # Send the content of the requested file to the client
        for i in range(0, len(outputData)):
            connectionSocket.send(outputData[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close() #Close client socket
    except IOError:
        #Send response message for file not found
        error = str('404 not found')
        print("Error occurred:" + str(IOError))
        connectionSocket.send(error.encode())
        # Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
