#!flask/bin/python
from flask import Flask, jsonify, send_file, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/get_image/<image_id>')
def get_image(image_id):
    filename = "myImage"+image_id+".gif"
    # return filename
    return send_file(filename, mimetype='image/gif')

if __name__ == '__main__':
    app.run(debug=True)
