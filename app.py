from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def show_ip():
    user_ipv4 = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    print(request.headers.get('X-Forwarded-For'))
    return f"Your IPv4 address is: {user_ipv4}"

if __name__ == '__main__':
    app.run()
