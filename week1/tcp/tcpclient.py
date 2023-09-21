import socket

HOST = '192.168.30.62'
PORT = 6000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'www.baidu.com')
    data = s.recv(1024)

print('received', repr(data))
