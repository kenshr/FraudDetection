from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
  data = [
    ("01-01-2020", 1597),
    ("02-01-2020", 1347),
    ("03-01-2020", 1359),
    ("04-01-2020", 1523),
    ("05-01-2020", 1657),
    ("06-01-2020", 3497),
  ]

  labels = [row[0] for row in data]
  values = [row[1] for row in data]

  return render_template("graph.html", labels=labels, values=values)

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