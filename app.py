from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def show_ip():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return f"Your IP address is: {user_ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
