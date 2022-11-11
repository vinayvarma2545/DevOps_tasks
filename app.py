from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                        #  username='root', 
                        #  password='pass',
                        # authSource="admin"
                        )
    db = client["test_db"]
    return db

@app.route('/')
def ping_server():
    return "Welcome to testlist."

@app.route('/test')
def get_stored_test():
    db=""
    try:
        db = get_db()
        _tests = db.test_tb.find()
        tests = [{"testno": test["testno"], "name": test["name"], "type": test["type"]} for test in _tests]
        return jsonify({"tests": tests})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
