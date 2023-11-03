#ömerfarukatik
import socket
import ssl
import base64

def get_user_input():
    gmail_address = input("Gmail adresinizi girin(kodlanmamış hali): ")
    password = input("Uygulama şifrenizi girin: kodlanmamış halini('Uygulamaya Tanımlı Şifre Yöntemi ile olan')")
    from_address = input("Gönderici adresi belirtin (örneğin: <faruk...@gmail.com>): ")
    to_address = input("Alıcı adresi belirtin (örneğin: <faru...@bil.omu.edu.tr>): ")
    subject = input("E-posta konusunu belirtin: ")
    body = input("E-posta gövdesini belirtin: ")

    # Gmail şifresini base64 ile kodla
    encoded_password = base64.b64encode(password.encode()).decode()

    return gmail_address, encoded_password, from_address, to_address, subject, body

def send_email():
    gmail_address, encoded_password, from_address, to_address, subject, body = get_user_input()

    context = ssl.create_default_context()
    server = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname='smtp.gmail.com')
    server.connect(('smtp.gmail.com', 465))

    response = server.recv(1024)
    print(response.decode())

    server.send(b'EHLO localhost\r\n')
    response = server.recv(1024)
    print(response.decode())

    server.send(b'AUTH LOGIN\r\n')
    response = server.recv(1024)
    print(response.decode())

    server.send((base64.b64encode(gmail_address.encode()) + b'\r\n'))
    response = server.recv(1024)
    print(response.decode())

    server.send((encoded_password + '\r\n').encode())
    response = server.recv(1024)
    print(response.decode())

    server.send(('MAIL FROM: ' + from_address + '\r\n').encode())
    response = server.recv(1024)
    print(response.decode())

    server.send(('RCPT TO: ' + to_address + '\r\n').encode())
    response = server.recv(1024)
    print(response.decode())

    server.send(b'DATA\r\n')
    response = server.recv(1024)
    print(response.decode())

    message = "Subject: " + subject + "\r\n\r\n" + body + "\r\n.\r\n"
    server.send(message.encode())
    response = server.recv(1024)
    print(response.decode())

    server.send(b'QUIT\r\n')
    response = server.recv(1024)
    print(response.decode())

    server.close()

if __name__ == '__main__':
    send_email()
