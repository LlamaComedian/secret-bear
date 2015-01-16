from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
  return "<h1>Hello World! LOL!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8042)

#run at http://localhost:5000/hello unless 'port' defined in app.run above
#in which case http://localhost:8042/hello
