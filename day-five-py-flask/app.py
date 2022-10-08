from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>The  script is running on [port]</h1>'

@app.route('/fibonacci')
def fibonacci():
    prv1 = nxt = 0
    prv2 = 1
    i = 2
    nums = [prv1, prv2]

    while(i < 99):
        nxt = prv1 + prv2
        nums.append(nxt)

        prv1 = prv2
        prv2 = nxt
        i += 1

    return nums