#!/usr/bin/python3
 
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9988))
s.listen(1)
 
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    conn.close()
    my_function_that_handles_data(data)
