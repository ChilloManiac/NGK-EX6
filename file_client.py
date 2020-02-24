import sys
from socket import *
from lib import Lib

PORT = 9000
BUFSIZE = 1000

def main(argv):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((argv[0], PORT))
    filename = argv[1]
    receiveFile(filename, clientSocket)
    clientSocket.close()

def receiveFile(fileName,  conn):
    Lib.writeTextTCP(fileName, conn)
    fileSize = Lib.getFileSizeTCP(conn)
    if fileSize != 0:
        fileHandle = open(fileName, "wb")
        toReceive = fileSize

        while toReceive > 0:
            received = conn.recv(min(toReceive, BUFSIZE))
            fileHandle.write(received)
            toReceive -= len(received)
        print "Finished getting file"
        fileHandle.close()
    else:
        print "File '" + fileName + "' did not exist on the server"

if __name__ == "__main__":
   main(sys.argv[1:])
