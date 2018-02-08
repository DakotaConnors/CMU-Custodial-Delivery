#http://flask.pocoo.org/docs/0.12/quickstart/

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

app.run()
