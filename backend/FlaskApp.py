from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://yaz:1234@cluster0.uspsoud.mongodb.net/Schedule_Optimization'

mongo = PyMongo(app)

@app.route('/get_data', methods=['GET'])
def get_data():
    collection = mongo.db.ScheduleCollectionName

    data = list(collection.find({}, {'_id': 0}))

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
