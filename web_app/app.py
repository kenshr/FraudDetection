from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  return '''<p> test </p>'''

@app.route('/hello', methods=['GET'])
def hello_world():
  return '''<h1> Hello, World!</h1>'''

@app.route('/form_example', methods=['GET'])
def form_display():
  return ''' <form action="/string_reverse" method="POST">
             <input type="text" name="some_string" />
             <input type="submit" />'''

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)