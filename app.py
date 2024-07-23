from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """Hello, hello, my name is Alice.
                Hopefully this works now!"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Remember to add the . at the end while build, it signals the current directory