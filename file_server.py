import sys
import socket
from lib import Lib

HOST = ''
PORT = 9000
BUFSIZE = 1000

def main(argv):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(1)
    print 'Server setup done'
    while (True):
        connectionSocket, addr = serverSocket.accept()
        fileName = Lib.readTextTCP(connectionSocket)
        fileSize = Lib.check_File_Exists(fileName)
        sendFile(fileName, fileSize, connectionSocket);
        connectionSocket.close()


def sendFile(fileName,  fileSize,  conn):
    Lib.writeTextTCP(str(fileSize), conn)

    if fileSize != 0:
        fileHandle = open(fileName, "rb")
        toSendBytes = fileSize
        print "Sending file: " + fileName
        print "With size: " + str(fileSize)

        while toSendBytes > 0:
            toSend = fileHandle.read(BUFSIZE)
            toSendBytes -= len(toSend)
            conn.send(toSend)

        print "Finished sending..."
        fileHandle.close()

if __name__ == "__main__":
    main(sys.argv[1:])
