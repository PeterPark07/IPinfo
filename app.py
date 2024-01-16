from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def show_ip():
    user_ipv4 = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    return f"Your IPv4 address is: {user_ipv4}"

@app.route('/ip')
def get_user_ip():
    user_ip = request.remote_addr
    return f'Your IP address is: {user_ip}'

if __name__ == '__main__':
    app.run()
