from flask import Flask, request, render_template
import urllib.request
import json

app = Flask(__name__)

url = "http://www.omdbapi.com/?apikey=362eab03&t=Forrest%20Gump"

response = urllib.request.urlopen(url)
data = response.read()
dict = json.loads(data)


@app.route('/', methods=['GET'])
def index():
    return render_template("base.html", data=dict)


if __name__ == "__main__":
    app.run(debug=True)
