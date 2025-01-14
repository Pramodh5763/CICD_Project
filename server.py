from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Kenny! Welcome to your CICD project."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

