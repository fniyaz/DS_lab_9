from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient

app = Flask(__name__)
mongo = MongoClient('mongodb://node1:27017,node2:27018,node3:27019/?replicaSet=rs0')
m_coll = mongo.testdb.messages


def generate_messages(messages):
    return "<br>".join(["{}: {}".format(m['name'], m['msg']) for m in messages])


def get_msgs():
    return list(m_coll.find())


def append_msg(msg):
    m_coll.insert({'name': msg[0], 'msg': msg[1]})


@app.route('/index.html', methods=['POST'])
def put():
    append_msg((request.form['name'], request.form['message']))
    return redirect(url_for('hello'))


@app.route('/')
def hello():
    msgs = get_msgs()
    return render_template("index.html", messages=generate_messages(msgs))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
