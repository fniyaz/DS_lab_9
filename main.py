from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


def generate_messages(messages):
    return "<br>".join(["{}: {}".format(m[0], m[1]) for m in messages])


msgs = []
def get_msgs():
    return msgs

def append_msg(msg):
    msgs.append(msg)


@app.route('/index.html', methods=['POST'])
def put():
    append_msg((request.form['name'], request.form['message']))
    return redirect(url_for('hello'))


@app.route('/')
def hello():
    msgs = get_msgs()
    return render_template("index.html", messages=generate_messages(msgs))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
