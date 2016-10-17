import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.data.pr4e.org', 80))
mysock.send('GET http://www.data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

print '1'
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        print 'DONE'
        break
    print data;
print '2'
mysock.close()
