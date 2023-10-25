import socket
import time

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 5555              # Arbitrary non-privileged port

with open('token.txt', 'r') as f:
    token = f.read()

remote_closed = False
local_closed = False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        c = socket.create_connection(('prob05.geekgame.pku.edu.cn', 10005))
        c.sendall(token.encode())
        time.sleep(1)
        conn.setblocking(False)
        # "Please input your token:"
        # print(f'Received {c.recv(1024)}')
        c.setblocking(False)
        while True:
            try:
                rdata = c.recv(1024)
            except BlockingIOError:
                pass
            else:
                if not rdata:
                    if not remote_closed:
                        print('Remote closed')
                        remote_closed = True
                else:
                    b = b'Please input your token: '
                    if rdata.startswith(b):
                        rdata = rdata[len(b):]
                        print('Replaced')
                    print(f'Remote: {rdata}')
                    conn.sendall(rdata)
            try:
                data = conn.recv(1024)
            except BlockingIOError:
                pass
            else:
                if not data:
                    if not local_closed:
                        print('Local closed')
                        local_closed = True
                else:
                    print(f'Local: {data}')
                    c.sendall(data)
            if local_closed and remote_closed:
                print('exiting')
                break
