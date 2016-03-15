import socket
import time

website = 'www.py4inf.com'
websiteSendRequest = 'GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n'

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((website, 80))
mysock.send(websiteSendRequest)

count = 0
picture = "";
while True:
    data = mysock.recv(5120)
    if(len(data)<1):
        break
    time.sleep(0.25)
    count += len(data)
    print len(data),count
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find("\r\n\r\n");
print 'Header length', pos
print picture[:pos]

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg","w")
fhand.write(picture);
fhand.close()
