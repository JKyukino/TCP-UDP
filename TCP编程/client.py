import socket

def clint():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 10001))    # 建立连接
    print(s.recv(1024).decode('utf-8'))    # 接收消息
    for data in [b'Michael', b'Tracy', b'Sarah']:
        s.send(data)    # 发送数据
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

if __name__ == '__main__':
    clint()