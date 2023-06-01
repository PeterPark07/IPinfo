from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def show_ip():
    user_ipv4 = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    try :
        user_ipv6 = request.headers.get(socket.getaddrinfo(user_ipv4, None)[-1][-1][0])
    except:
        user_ipv6 = 0000

    return f"Your IPv4 address is: {user_ipv4}<br>Your IPv6 address is: {user_ipv6}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
