import socket
import ssl

def send_email():

    context = ssl.create_default_context()
    server = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname='smtp.gmail.com')
    server.connect(('smtp.gmail.com', 465))

    server.recv(1024)

    server.send(b'EHLO localhost\r\n')
    server.recv(1024)

    server.send(b'AUTH LOGIN\r\n')
    server.recv(1024)

    server.send(b'ZmFydWs1MzA4YXRpa0BnbWFpbC5jb20=\r\n')  
    server.recv(1024)

    server.send(b'cGt0aSBndG92IHl4Y2sgZWN4eA==\r\n') 
    server.recv(1024)

    server.send(b'MAIL FROM: <faruk5308atik@gmail.com>\r\n')
    server.recv(1024)

    server.send(b'RCPT TO: <faruk.atik@bil.omu.edu.tr>\r\n')
    server.recv(1024)

    server.send(b'DATA\r\n')
    server.recv(1024)

    message = "Subject: dünya2\r\n\r\nBu bir test mailidir.\r\n.\r\n"
    server.send(message.encode())
    server.recv(1024)

    server.send(b'QUIT\r\n')
    server.recv(1024)

    server.close()

if __name__ == '__main__':
    send_email()
