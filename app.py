from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def show_ip():
    user_ipv4 = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    try:
        addr_info = socket.getaddrinfo(user_ipv4, None, socket.AF_INET6)
        user_ipv6 = addr_info[0][4][0] if addr_info else None
    except:
        user_ipv6 = 0

    return f"Your IPv4 address is: {user_ipv4}<br>Your IPv6 address is: {user_ipv6}"

if __name__ == '__main__':
    app.run()
