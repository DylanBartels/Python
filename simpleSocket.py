import socket

website = 'www.py4inf.com'
websiteSendRequest = 'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((website, 80))
mysock.send(websiteSendRequest)

while True:
    data = mysock.recv(512)
    if(len(data)<1):
        break
    print data

mysock.close()