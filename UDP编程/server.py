import socket
def server():
 s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 s.bind(('127.0.0.1',10001))
 print("UDP on 10001")
 while True:
     data,addr=s.recvfrom(1024)
     print("Receive from %s:%s" % addr)
     s.sendto(b'Hello,%s!' %data,addr)
if __name__ == '__main__':
    server()