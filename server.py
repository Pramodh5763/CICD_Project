from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Bangalore! Welcome to your second CICD project dude ."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

