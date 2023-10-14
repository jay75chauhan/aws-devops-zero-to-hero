from flask import Flask , redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, jay @@!</p>"
    
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name   

    

if __name__ == '__main__':
    app.run()

