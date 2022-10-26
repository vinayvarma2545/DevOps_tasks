from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
import json
from healthcheck import HealthCheck
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


health = HealthCheck()

metrics.info('app_info', 'Application info', version='1.0.3')

app.config['MONGODB_SETTINGS'] = {
  'db': 'DevOps',
  'host': 'localhost',
  'port': 27017
}

db = MongoEngine()
db.init_app(app)

class Workers(db.Document):
  Names = db.StringField()
  Work = db.StringField()
  WorkerId = db.IntField()
  def to_json(self):
    return {"Names": self.Names,
        "Work": self.Work,
        "WorkerId" : self.WorkerId}

@app.route("/")
def root_path():
  return("Welcome")




@app.route('/getw/', methods=['GET'])
def get_user():
  workerdata = Workers.objects()
  print(workerdata)
  if not workerdata:
    return jsonify({'error': 'data not found'})
  else:
    return  jsonify(workerdata)



@app.route('/postw/', methods=['POST'])
def add_user():
  record = json.loads(request.data)
  workerdata = Workers(Names=record['Names'],
        Work=record['Work'],
        WorkerId=record["WorkerId"])
  workerdata.save()
  return jsonify(workerdata)



@app.route('/putw/<id>', methods=['PUT'])
def Update_user(id):
  record = json.loads(request.data)
  workerdata = Workers.objects.get_or_404(id=id)
  if not workerdata:
    return jsonify({'error': 'data not found'})
  else:
    workerdata.update(Names=record['Names'],
          Work=record['Work'],
          WorkerId=record["WorkerId"])
  return jsonify(workerdata)

    
@app.route('/delw/<id>/d', methods=['DELETE'])
def delete_user(id):
  workerdata = Workers.objects(id=id)
  if not workerdata:
    return jsonify({'error': 'data not found'})
  else:
    workerdata.delete()
  return jsonify(workerdata)





class Batch1(db.Document):
  Names = db.StringField()
  Course = db.StringField()
  def to_json(self):
    return {"Names": self.Names,
        "Course": self.Course,}

@app.route('/getb/', methods=['GET'])
def get_batch():
  batch1data = Batch1.objects()
  if not batch1data:
    return jsonify({'error': 'data not found'})
  else:
    return jsonify(batch1data)

@app.route('/postb/', methods=['POST'])
def add_batch():
  record = json.loads(request.data)
  batch1data = Batch1(Names=record['Names'],
        Course=record['Course'])
  batch1data.save()
  return jsonify(batch1data)


@app.route('/putb/<id>', methods=['PUT'])
def Update_batch(id):
  record = json.loads(request.data)
  batch1data = Batch1.objects.get_or_404(id=id)
  if not batch1data:
    return jsonify({'error': 'data not found'})
  else:
    batch1data.update(Names=record['Names'],
          Course=record['Course'])
  return jsonify(batch1data)

    
@app.route('/delb/<id>/d', methods=['DELETE'])
def delete_batch(id):
  batch1data = Batch1.objects(id=id)
  if not batch1data:
    return jsonify({'error': 'data not found'})
  else:
    batch1data.delete()
  return jsonify(batch1data)  



app.add_url_rule('/healthcheck', 'healthcheck', view_func=lambda: health.run())

if __name__ == "__main__":
  app.run(debug=True)
