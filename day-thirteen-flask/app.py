from flask import Flask, render_template, redirect, url_for, request
import json
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '64ef30c6776ffc97344ea0552f668cc392c6220e064e27af'


@app.route("/")
def index():
    return redirect(url_for('home'))


@app.route("/google", methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        query = request.form['query']

        if not query:
            return render_template("base.html")
        else:
            with open('record.json', 'r') as openfile:
                logs = json.load(openfile)

            logs.append(
                {'query': query, 'time': str(datetime.datetime.now())})

            with open('record.json', "w") as file:
                json.dump(logs, file)

            return redirect(url_for('search'))

    return render_template("base.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/logs")
def logs():
    with open('record.json', 'r') as openfile:
        logs = json.load(openfile)

    return render_template("records.html", logs=logs)


if __name__ == "__main__":
    app.run(debug=True)
