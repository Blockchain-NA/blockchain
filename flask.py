from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'd'

if __name__ == '__main__':
    app.run()
    
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()