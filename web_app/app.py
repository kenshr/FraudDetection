from flask import Flask, request, render_template
# from flask_pymongo import pymongo
from pymongo import MongoClient
app = Flask(__name__)


@app.route('/')
def home():
  # Initialize MongoDB database objects
  client = MongoClient('localhost', 27017)
  db = client['fraud']
  collection = db['event']

  # Show 10 most recent events pulled from API
  cursor = collection.find({}).sort([("_id",-1)])
  pred_dict = dict()
  output_str = '10 Most Recent Events:<br/>'

  ct = 0
  for idx, document in enumerate(cursor, 1):
    if ct == 10:
      break
    risk = ''
    if document['prediction'][0][1] < 0.2:
      risk = 'Low'
    elif document['prediction'][0][1] < 0.5:
      risk = 'Medium'
    else:
      risk = 'High'

    output_str += f'Event {idx}: {document["prediction"][0][1]}, Risk: {risk}<br/>'
    ct += 1

  labels = pred_dict.keys()
  values = pred_dict.values()

  return output_str

@app.route('/dashboard')
def dashboard():
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
  app.run(host='0.0.0.0', port=8000, debug=True)